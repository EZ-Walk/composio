import { ComposioToolSet as BaseComposioToolSet } from "../sdk/base.toolset";
import { OpenAI } from "openai";

import { COMPOSIO_BASE_URL } from "../sdk/client/core/OpenAPI";
import { WorkspaceConfig } from "../env/config";
import { Workspace } from "../env";
import logger from "../utils/logger";
import { ActionsListResponseDTO } from "../sdk/client";

type Optional<T> = T | null;
type Sequence<T> = Array<T>;

export class OpenAIToolSet extends BaseComposioToolSet {
    static FRAMEWORK_NAME = "openai";
    static DEFAULT_ENTITY_ID = "default";

    /**
     * Composio toolset for OpenAI framework.
     *
     * Example:
     * ```typescript
     * 
     * ```
     */
    constructor(
      config: {
        apiKey?: Optional<string>,
        baseUrl?: Optional<string>,
        entityId?: string,
        workspaceConfig?: WorkspaceConfig
      }={}
    ) {
        super(
            config.apiKey || null,
            config.baseUrl || COMPOSIO_BASE_URL,
            OpenAIToolSet.FRAMEWORK_NAME,
            config.entityId || OpenAIToolSet.DEFAULT_ENTITY_ID,
            config.workspaceConfig || Workspace.Host()
        );
    }

    async getTools(
        filters: {
            actions?: Sequence<string>;
            apps?: Sequence<string>;
            tags?: Optional<Array<string>>;
            useCase?: Optional<string>;
        },
        entityId?: Optional<string>
    ): Promise<Sequence<OpenAI.ChatCompletionTool>> {
        const mainActions = await this.getToolsSchema(filters, entityId);
        return mainActions.map((action: NonNullable<ActionsListResponseDTO["items"]>[0]) => {
            const formattedSchema: OpenAI.FunctionDefinition = {
                name: action.name!,
                description: action.description!,
                parameters: action.parameters!,
            };
            const tool: OpenAI.ChatCompletionTool = {
                type: "function",
                function: formattedSchema
            }
            return tool;
        }) || [];
    }


    async executeToolCall(
        tool: OpenAI.ChatCompletionMessageToolCall,
        entityId: Optional<string> = null
    ): Promise<string> {
        return JSON.stringify(await this.executeAction(
            tool.function.name,
            JSON.parse(tool.function.arguments),
            entityId || this.entityId
        ));
    }


    async handleToolCall(
        chatCompletion: OpenAI.ChatCompletion,
        entityId: Optional<string> = null
    ): Promise<Sequence<string>> {
        const outputs = [];
        for (const message of chatCompletion.choices) {
            if (message.message.tool_calls) {
                outputs.push(await this.executeToolCall(message.message.tool_calls[0], entityId));
            }
        }
        return outputs;
    }


    async handleAssistantMessage(
        run: OpenAI.Beta.Threads.Run,
        entityId: Optional<string> = null
    ): Promise<Array<OpenAI.Beta.Threads.Runs.RunSubmitToolOutputsParams.ToolOutput>> {
        const tool_calls = run.required_action?.submit_tool_outputs?.tool_calls || [];
        const tool_outputs: Array<OpenAI.Beta.Threads.Runs.RunSubmitToolOutputsParams.ToolOutput> = await Promise.all(
            tool_calls.map(async (tool_call) => {
                logger.debug(`Executing tool call with ID: ${tool_call.function.name} and parameters: ${JSON.stringify(tool_call.function.arguments)}`);
                const tool_response = await this.executeToolCall(
                    tool_call as OpenAI.ChatCompletionMessageToolCall,
                    entityId || this.entityId
                );
                logger.debug(`Received tool response: ${JSON.stringify(tool_response)}`);
                return {
                    tool_call_id: tool_call.id,
                    output: JSON.stringify(tool_response),
                };
            })
        );
        return tool_outputs;
    }



    async waitAndHandleAssistantToolCalls(
        client: OpenAI,
        run: OpenAI.Beta.Threads.Run,
        thread: OpenAI.Beta.Threads.Thread,
        entityId: Optional<string> = null
    ): Promise<OpenAI.Beta.Threads.Run> {
        while (["queued", "in_progress", "requires_action"].includes(run.status)) {
            logger.debug(`Current run status: ${run.status}`);
            const tool_outputs = await this.handleAssistantMessage(run, entityId || this.entityId);
            if (run.status === "requires_action") {
                logger.debug(`Submitting tool outputs for run ID: ${run.id} in thread ID: ${thread.id}`);
                run = await client.beta.threads.runs.submitToolOutputs(
                    thread.id,
                    run.id,
                    {
                        tool_outputs: tool_outputs
                    }
                );
            } else {
                run = await client.beta.threads.runs.retrieve(thread.id, run.id);
                await new Promise(resolve => setTimeout(resolve, 500));
            }
        }
        return run;
    }
}
