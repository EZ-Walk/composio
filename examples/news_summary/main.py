from langchain import hub
from langchain.agents import AgentExecutor, load_tools
from langchain.agents.format_scratchpad import format_log_to_str
from langchain.agents.output_parsers import (
    ReActJsonSingleInputOutputParser,
)
from langchain.tools.render import render_text_description
from langchain_community.utilities import SerpAPIWrapper
from langchain_community.llms import HuggingFaceEndpoint
from langchain_community.chat_models.huggingface import ChatHuggingFace
from composio_langchain import ComposioToolSet, Action, App
import os
import dotenv

dotenv.load_dotenv()

llm = HuggingFaceEndpoint(repo_id="HuggingFaceH4/zephyr-7b-beta", huggingfacehub_api_token=os.getenv("HUGGINGFACEHUB_API_TOKEN"))

chat_model = ChatHuggingFace(llm=llm,  huggingfacehub_api_token=os.getenv("HUGGINGFACEHUB_API_TOKEN"))
# Import from composio_langchain


# setup tools
composio_toolset = ComposioToolSet()
tools = composio_toolset.get_tools(apps=[App.SERPAPI])

# setup ReAct style prompt
prompt = hub.pull("hwchase17/react-json")
prompt = prompt.partial(
    tools=render_text_description(tools),
    tool_names=", ".join([t.name for t in tools]),
)

# define the agent
chat_model_with_stop = chat_model.bind(stop=["\nInvalidStop"])
agent = (
    {
        "input": lambda x: x["input"],
        "agent_scratchpad": lambda x: format_log_to_str(x["intermediate_steps"]),
    }
    | prompt
    | chat_model_with_stop
    | ReActJsonSingleInputOutputParser()
)

# instantiate AgentExecutor
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True, handle_parsing_errors=True)
agent_executor.return_intermediate_steps = True
res = agent_executor.invoke(
    {
        "input": "Use SERP to find the one latest AI news, take only description of article."
    }
)

res2 = agent_executor.invoke({
    "input": res['output']+' Summarize this'
})

