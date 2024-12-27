import axios from "axios";
import { z } from "zod";
import logger from "../utils/logger";
import { Entity } from "./models/Entity";
import { Actions } from "./models/actions";
import { ActiveTriggers } from "./models/activeTriggers";
import { Apps } from "./models/apps";
import { BackendClient } from "./models/backendClient";
import { ConnectedAccounts } from "./models/connectedAccounts";
import { Integrations } from "./models/integrations";
import { Triggers } from "./models/triggers";
import ComposioSDKContext from "./utils/composioContext";
import { getSDKConfig } from "./utils/config";
import { CEG } from "./utils/error";
import { COMPOSIO_SDK_ERROR_CODES } from "./utils/errors/src/constants";
import { isNewerVersion } from "./utils/other";
import { getPackageJsonDir } from "./utils/projectUtils";
import { TELEMETRY_LOGGER } from "./utils/telemetry";
import { TELEMETRY_EVENTS } from "./utils/telemetry/events";

import {
  ZGetExpectedParamsForUserParams,
  ZGetExpectedParamsRes,
} from "../types/composio";
import { getUUID } from "../utils/common";
import { ZAuthMode } from "./types/integration";

export type ComposioInputFieldsParams = z.infer<
  typeof ZGetExpectedParamsForUserParams
>;
export type ComposioInputFieldsRes = z.infer<typeof ZGetExpectedParamsRes>;

export class Composio {
  /**
   * The Composio class serves as the main entry point for interacting with the Composio SDK.
   * It provides access to various models that allow for operations on connected accounts, apps,
   * actions, triggers, integrations, and active triggers.
   */
  backendClient: BackendClient;
  connectedAccounts: ConnectedAccounts;
  apps: Apps;
  actions: Actions;
  triggers: Triggers;
  integrations: Integrations;
  activeTriggers: ActiveTriggers;

  fileName: string = "js/src/sdk/index.ts";

  /**
   * Initializes a new instance of the Composio class.
   *
   * @param {Object} config - Configuration object for the Composio SDK
   * @param {string} [config.apiKey] - The API key for authenticating with the Composio backend. Can also be set locally in an environment variable.
   * @param {string} [config.baseUrl] - The base URL for the Composio backend. By default, it is set to the production URL.
   * @param {string} [config.runtime] - The runtime environment for the SDK.
   */
  constructor(
    config: { apiKey?: string; baseUrl?: string; runtime?: string } = {}
  ) {
    // Parse the base URL and API key, falling back to environment variables or defaults if not provided
    const { baseURL: baseURLParsed, apiKey: apiKeyParsed } = getSDKConfig(
      config?.baseUrl,
      config?.apiKey
    );

    ComposioSDKContext.apiKey = apiKeyParsed;
    ComposioSDKContext.sessionId = getUUID();
    ComposioSDKContext.baseURL = baseURLParsed;
    ComposioSDKContext.frameworkRuntime = config?.runtime;

    //eslint-disable-next-line @typescript-eslint/no-require-imports
    ComposioSDKContext.composioVersion = require(
      getPackageJsonDir() + "/package.json"
    ).version;

    TELEMETRY_LOGGER.manualTelemetry(TELEMETRY_EVENTS.SDK_INITIALIZED, {});

    if (!apiKeyParsed) {
      throw CEG.getCustomError(
        COMPOSIO_SDK_ERROR_CODES.COMMON.API_KEY_UNAVAILABLE,
        {
          message: "🔑 API Key is not provided",
          description:
            "You need to provide it in the constructor or as an environment variable COMPOSIO_API_KEY",
          possibleFix:
            "Please provide a valid API Key. You can get it from https://app.composio.dev/settings OR Check if you are passing it as an object in the constructor like - { apiKey: 'your-api-key' }",
        }
      );
    }

    logger.info(
      `Initializing Composio w API Key: [REDACTED] and baseURL: ${baseURLParsed}`
    );

    // Initialize the BackendClient with the parsed API key and base URL.
    this.backendClient = new BackendClient(
      apiKeyParsed,
      baseURLParsed,
      config?.runtime
    );

    // Instantiate models with dependencies as needed.
    this.connectedAccounts = new ConnectedAccounts(this.backendClient);
    this.triggers = new Triggers(this.backendClient);
    this.apps = new Apps(this.backendClient);
    this.actions = new Actions(this.backendClient);
    this.integrations = new Integrations(this.backendClient);
    this.activeTriggers = new ActiveTriggers(this.backendClient);

    this.checkForLatestVersionFromNPM();
  }

  /**
   * Checks for the latest version of the Composio SDK from NPM.
   * If a newer version is available, it logs a warning to the console.
   */
  async checkForLatestVersionFromNPM() {
    try {
      const packageName = "composio-core";
      const packageJsonDir = getPackageJsonDir();

      // eslint-disable-next-line @typescript-eslint/no-require-imports
      const currentVersionFromPackageJson = require(
        packageJsonDir + "/package.json"
      ).version;

      const response = await axios.get(
        `https://registry.npmjs.org/${packageName}/latest`
      );
      const latestVersion = response.data.version;

      if (isNewerVersion(latestVersion, currentVersionFromPackageJson)) {
        // eslint-disable-next-line no-console
        console.warn(
          `🚀 Upgrade available! Your composio-core version (${currentVersionFromPackageJson}) is behind. Latest version: ${latestVersion}.`
        );
      }
    } catch (_error) {
      // Ignore and do nothing
    }
  }

  /**
   * Retrieves an Entity instance associated with a given ID.
   *
   * @param {string} [id='default'] - The ID of the entity to retrieve.
   * @returns {Entity} An instance of the Entity class.
   */
  getEntity(id: string = "default"): Entity {
    TELEMETRY_LOGGER.manualTelemetry(TELEMETRY_EVENTS.SDK_METHOD_INVOKED, {
      method: "getEntity",
      file: this.fileName,
      params: { id },
    });
    return new Entity(this.backendClient, id);
  }

  async getExpectedParamsForUser(
    params: ComposioInputFieldsParams
  ): Promise<ComposioInputFieldsRes> {
    TELEMETRY_LOGGER.manualTelemetry(TELEMETRY_EVENTS.SDK_METHOD_INVOKED, {
      method: "getExpectedParamsForUser",
      file: this.fileName,
      params: params,
    });
    const { app } = params;
    let { integrationId } = params;
    if (integrationId === null && app === null) {
      throw new Error("Both `integration_id` and `app` cannot be None");
    }

    if (!integrationId) {
      try {
        const integrations = await this.integrations.list({
          appName: app!,
          showDisabled: false,
        });
        if (params.authScheme && integrations) {
          integrations.items = integrations.items.filter(
            (integration) => integration.authScheme === params.authScheme
          );
        }
        integrationId = integrations?.items[0]?.id as string;
      } catch (_) {
        // do nothing
      }
    }

    let integration = integrationId
      ? await this.integrations.get({
          integrationId: integrationId!,
        })
      : undefined;

    if (integration) {
      return {
        expectedInputFields: integration.expectedInputFields,
        integrationId: integration.id!,
        authScheme: integration.authScheme as z.infer<typeof ZAuthMode>,
      };
    }

    const appInfo = await this.apps.get({
      appKey: app!.toLocaleLowerCase(),
    });

    const preferredAuthScheme = [
      "OAUTH2",
      "OAUTH1",
      "API_KEY",
      "BASIC",
      "BEARER_TOKEN",
      "BASIC_WITH_JWT",
    ];

    let schema: (typeof preferredAuthScheme)[number] | undefined =
      params.authScheme;

    if (!schema) {
      for (const scheme of preferredAuthScheme) {
        if (
          appInfo.auth_schemes
            ?.map((_authScheme) => _authScheme.mode)
            .includes(scheme)
        ) {
          schema = scheme;
          break;
        }
      }
    }

    const hasTestConnectors = (appInfo.testConnectors?.length ?? 0) > 0;
    const authSchemeFields = appInfo.auth_schemes?.find(
      (_authScheme) => _authScheme.mode === schema
    )?.fields;
    const requiredCustomerFields =
      (
        authSchemeFields as {
          expected_from_customer: boolean;
        }[]
      )?.filter((field) => !field.expected_from_customer)?.length ?? 0;

    const areNoFieldsRequiredForIntegration =
      hasTestConnectors || requiredCustomerFields === 0;

    if (!areNoFieldsRequiredForIntegration) {
      throw new Error(
        `No default credentials available for this app, please create new integration by going to app.composio.dev or through CLI - composio add ${appInfo.key}`
      );
    }

    const timestamp = new Date().toISOString().replace(/[-:.]/g, "");
    const hasRelevantTestConnectors = params.authScheme
      ? appInfo.testConnectors?.filter(
          (connector) => connector.authScheme === params.authScheme
        )?.length! > 0
      : appInfo.testConnectors?.length! > 0;
    if (hasRelevantTestConnectors) {
      integration = await this.integrations.create({
        appId: appInfo.appId,
        name: `integration_${timestamp}`,
        authScheme: schema as z.infer<typeof ZAuthMode>,
        authConfig: {},
        useComposioAuth: true,
      });

      return {
        expectedInputFields: integration?.expectedInputFields!,
        integrationId: integration?.id!,
        authScheme: integration?.authScheme as z.infer<typeof ZAuthMode>,
      };
    }

    if (!schema) {
      throw new Error(
        `No supported auth scheme found for \`${String(app)}\`, ` +
          "Please create an integration and use the ID to " +
          "get the expected parameters."
      );
    }

    integration = await this.integrations.create({
      appId: appInfo.appId,
      name: `integration_${timestamp}`,
      authScheme: schema as z.infer<typeof ZAuthMode>,
      authConfig: {},
      useComposioAuth: false,
    });

    if (!integration) {
      throw new Error(
        "An unexpected error occurred while creating the integration, please create an integration manually and use its ID to get the expected parameters"
      );
    }
    return {
      expectedInputFields: integration.expectedInputFields,
      integrationId: integration.id!,
      authScheme: integration.authScheme as z.infer<typeof ZAuthMode>,
    };
  }
}
