"""
Tag enums.
"""

from composio.client.enums.base import TAGS_CACHE, TagData, _AnnotatedEnum, enum


@enum
class Tag(_AnnotatedEnum[TagData], path=TAGS_CACHE):
    """Tag object."""

    ASANA_ALLOCATIONS: "Tag"
    ASANA_ATTACHMENTS: "Tag"
    ASANA_AUDIT_LOG_API: "Tag"
    ASANA_BATCH_API: "Tag"
    ASANA_CUSTOM_FIELDS: "Tag"
    ASANA_CUSTOM_FIELD_SETTINGS: "Tag"
    ASANA_EVENTS: "Tag"
    ASANA_GOALS: "Tag"
    ASANA_GOAL_RELATIONSHIPS: "Tag"
    ASANA_IMPORTANT: "Tag"
    ASANA_JOBS: "Tag"
    ASANA_MEMBERSHIPS: "Tag"
    ASANA_ORGANIZATION_EXPORTS: "Tag"
    ASANA_PORTFOLIOS: "Tag"
    ASANA_PORTFOLIO_MEMBERSHIPS: "Tag"
    ASANA_PROJECTS: "Tag"
    ASANA_PROJECT_BRIEFS: "Tag"
    ASANA_PROJECT_MEMBERSHIPS: "Tag"
    ASANA_PROJECT_STATUSES: "Tag"
    ASANA_PROJECT_TEMPLATES: "Tag"
    ASANA_RULES: "Tag"
    ASANA_SECTIONS: "Tag"
    ASANA_STATUS_UPDATES: "Tag"
    ASANA_STORIES: "Tag"
    ASANA_TAGS: "Tag"
    ASANA_TASKS: "Tag"
    ASANA_TASK_TEMPLATES: "Tag"
    ASANA_TEAMS: "Tag"
    ASANA_TEAM_MEMBERSHIPS: "Tag"
    ASANA_TIME_PERIODS: "Tag"
    ASANA_TIME_TRACKING_ENTRIES: "Tag"
    ASANA_TYPEAHEAD: "Tag"
    ASANA_USERS: "Tag"
    ASANA_USER_TASK_LISTS: "Tag"
    ASANA_WEBHOOKS: "Tag"
    ASANA_WORKSPACES: "Tag"
    ASANA_WORKSPACE_MEMBERSHIPS: "Tag"
    ATTIO_ATTRIBUTES: "Tag"
    ATTIO_COMMENTS: "Tag"
    ATTIO_ENTRIES: "Tag"
    ATTIO_IMPORTANT: "Tag"
    ATTIO_LISTS: "Tag"
    ATTIO_META: "Tag"
    ATTIO_NOTES: "Tag"
    ATTIO_OBJECTS: "Tag"
    ATTIO_RECORDS: "Tag"
    ATTIO_TASKS: "Tag"
    ATTIO_THREADS: "Tag"
    ATTIO_WEBHOOKS: "Tag"
    ATTIO_WORKSPACE_MEMBERS: "Tag"
    BAMBOOHR_ACCOUNT_INFORMATION: "Tag"
    BAMBOOHR_APPLICANT_TRACKING: "Tag"
    BAMBOOHR_BENEFITS: "Tag"
    BAMBOOHR_COMPANY_FILES: "Tag"
    BAMBOOHR_EMPLOYEES: "Tag"
    BAMBOOHR_EMPLOYEE_FILES: "Tag"
    BAMBOOHR_GOALS: "Tag"
    BAMBOOHR_HOURS: "Tag"
    BAMBOOHR_IMPORTANT: "Tag"
    BAMBOOHR_LAST_CHANGE_INFORMATION: "Tag"
    BAMBOOHR_LOGIN: "Tag"
    BAMBOOHR_PAYROLL: "Tag"
    BAMBOOHR_PHOTOS: "Tag"
    BAMBOOHR_REPORTS: "Tag"
    BAMBOOHR_TABULAR_DATA: "Tag"
    BAMBOOHR_TIME_OFF: "Tag"
    BAMBOOHR_TIME_TRACKING: "Tag"
    BAMBOOHR_TIME_TRACKING___PRIVATE_BETA: "Tag"
    BAMBOOHR_TRAINING: "Tag"
    BAMBOOHR_WEBHOOKS: "Tag"
    BREVO_ACCOUNT: "Tag"
    BREVO_COMPANIES: "Tag"
    BREVO_CONTACTS: "Tag"
    BREVO_CONVERSATIONS: "Tag"
    BREVO_COUPONS: "Tag"
    BREVO_DEALS: "Tag"
    BREVO_DOMAINS: "Tag"
    BREVO_ECOMMERCE: "Tag"
    BREVO_EMAIL_CAMPAIGNS: "Tag"
    BREVO_EVENT: "Tag"
    BREVO_EXTERNAL_FEEDS: "Tag"
    BREVO_FILES: "Tag"
    BREVO_IMPORTANT: "Tag"
    BREVO_INBOUND_PARSING: "Tag"
    BREVO_MASTER_ACCOUNT: "Tag"
    BREVO_NOTES: "Tag"
    BREVO_PROCESS: "Tag"
    BREVO_RESELLER: "Tag"
    BREVO_SENDERS: "Tag"
    BREVO_SMS_CAMPAIGNS: "Tag"
    BREVO_TASKS: "Tag"
    BREVO_TRANSACTIONAL_EMAILS: "Tag"
    BREVO_TRANSACTIONAL_SMS: "Tag"
    BREVO_TRANSACTIONAL_WHATSAPP: "Tag"
    BREVO_USER: "Tag"
    BREVO_WEBHOOKS: "Tag"
    BREVO_WHATSAPP_CAMPAIGNS: "Tag"
    CLICKUP_ATTACHMENTS: "Tag"
    CLICKUP_AUTHORIZATION: "Tag"
    CLICKUP_COMMENTS: "Tag"
    CLICKUP_CUSTOM_FIELDS: "Tag"
    CLICKUP_CUSTOM_TASK_TYPES: "Tag"
    CLICKUP_FOLDERS: "Tag"
    CLICKUP_GOALS: "Tag"
    CLICKUP_GUESTS: "Tag"
    CLICKUP_IMPORTANT: "Tag"
    CLICKUP_LISTS: "Tag"
    CLICKUP_MEMBERS: "Tag"
    CLICKUP_ROLES: "Tag"
    CLICKUP_SHARED_HIERARCHY: "Tag"
    CLICKUP_SPACES: "Tag"
    CLICKUP_TAGS: "Tag"
    CLICKUP_TASKS: "Tag"
    CLICKUP_TASK_CHECKLISTS: "Tag"
    CLICKUP_TASK_RELATIONSHIPS: "Tag"
    CLICKUP_TASK_TEMPLATES: "Tag"
    CLICKUP_TEAMS___USER_GROUPS: "Tag"
    CLICKUP_TEAMS___WORKSPACES: "Tag"
    CLICKUP_TIME_TRACKING: "Tag"
    CLICKUP_TIME_TRACKING__LEGACY_: "Tag"
    CLICKUP_USERS: "Tag"
    CLICKUP_VIEWS: "Tag"
    CLICKUP_WEBHOOKS: "Tag"
    DEFAULT: "Tag"
    DISCORDBOT_IMPORTANT: "Tag"
    DISCORD_IMPORTANT: "Tag"
    ELEVENLABS_AUDIO_NATIVE: "Tag"
    ELEVENLABS_DUBBING: "Tag"
    ELEVENLABS_IMPORTANT: "Tag"
    ELEVENLABS_MODELS: "Tag"
    ELEVENLABS_PROJECTS: "Tag"
    ELEVENLABS_PRONUNCIATION_DICTIONARY: "Tag"
    ELEVENLABS_SAMPLES: "Tag"
    ELEVENLABS_SPEECH_HISTORY: "Tag"
    ELEVENLABS_SPEECH_TO_SPEECH: "Tag"
    ELEVENLABS_TEXT_TO_SPEECH: "Tag"
    ELEVENLABS_USER: "Tag"
    ELEVENLABS_VOICES: "Tag"
    ELEVENLABS_VOICE_GENERATION: "Tag"
    ELEVENLABS_WORKSPACE: "Tag"
    FIGMA_ACTIVITY_LOGS: "Tag"
    FIGMA_COMMENTS: "Tag"
    FIGMA_COMMENT_REACTIONS: "Tag"
    FIGMA_COMPONENTS: "Tag"
    FIGMA_COMPONENT_SETS: "Tag"
    FIGMA_DEV_RESOURCES: "Tag"
    FIGMA_FILES: "Tag"
    FIGMA_IMPORTANT: "Tag"
    FIGMA_PAYMENTS: "Tag"
    FIGMA_PROJECTS: "Tag"
    FIGMA_STYLES: "Tag"
    FIGMA_USERS: "Tag"
    FIGMA_VARIABLES: "Tag"
    FIGMA_WEBHOOKS: "Tag"
    GITHUB_ACTIONS: "Tag"
    GITHUB_ACTIVITY: "Tag"
    GITHUB_APPS: "Tag"
    GITHUB_BILLING: "Tag"
    GITHUB_CHECKS: "Tag"
    GITHUB_CLASSROOM: "Tag"
    GITHUB_CODESPACES: "Tag"
    GITHUB_CODES_OF_CONDUCT: "Tag"
    GITHUB_CODE_SCANNING: "Tag"
    GITHUB_COPILOT: "Tag"
    GITHUB_DEPENDABOT: "Tag"
    GITHUB_DEPENDENCY_GRAPH: "Tag"
    GITHUB_EMOJIS: "Tag"
    GITHUB_GISTS: "Tag"
    GITHUB_GIT: "Tag"
    GITHUB_GITIGNORE: "Tag"
    GITHUB_IMPORTANT: "Tag"
    GITHUB_INTERACTIONS: "Tag"
    GITHUB_ISSUES: "Tag"
    GITHUB_LICENSES: "Tag"
    GITHUB_MARKDOWN: "Tag"
    GITHUB_META: "Tag"
    GITHUB_MIGRATIONS: "Tag"
    GITHUB_OIDC: "Tag"
    GITHUB_ORGS: "Tag"
    GITHUB_PACKAGES: "Tag"
    GITHUB_PROJECTS: "Tag"
    GITHUB_PULLS: "Tag"
    GITHUB_RATE_LIMIT: "Tag"
    GITHUB_REACTIONS: "Tag"
    GITHUB_REPOS: "Tag"
    GITHUB_SEARCH: "Tag"
    GITHUB_SECRET_SCANNING: "Tag"
    GITHUB_SECURITY_ADVISORIES: "Tag"
    GITHUB_TEAMS: "Tag"
    GITHUB_USERS: "Tag"
    HUBSPOT_BASIC: "Tag"
    HUBSPOT_BATCH: "Tag"
    HUBSPOT_CORE: "Tag"
    HUBSPOT_EVENTS: "Tag"
    HUBSPOT_GDPR: "Tag"
    HUBSPOT_GROUPS: "Tag"
    HUBSPOT_IMPORTANT: "Tag"
    HUBSPOT_OWNERS: "Tag"
    HUBSPOT_PIPELINES: "Tag"
    HUBSPOT_PIPELINE_AUDITS: "Tag"
    HUBSPOT_PIPELINE_STAGES: "Tag"
    HUBSPOT_PIPELINE_STAGE_AUDITS: "Tag"
    HUBSPOT_PUBLIC_IMPORTS: "Tag"
    HUBSPOT_PUBLIC_OBJECT: "Tag"
    HUBSPOT_PUBLIC_OBJECT_SCHEMAS: "Tag"
    HUBSPOT_RECORDING_SETTINGS: "Tag"
    HUBSPOT_SEARCH: "Tag"
    HUBSPOT_SETTINGS: "Tag"
    HUBSPOT_TEMPLATES: "Tag"
    HUBSPOT_TOKENS: "Tag"
    JIRA_ANNOUNCEMENT_BANNER: "Tag"
    JIRA_APPLICATION_ROLES: "Tag"
    JIRA_APP_DATA_POLICIES__EAP_: "Tag"
    JIRA_APP_MIGRATION: "Tag"
    JIRA_APP_PROPERTIES: "Tag"
    JIRA_AUDIT_RECORDS: "Tag"
    JIRA_AVATARS: "Tag"
    JIRA_CLASSIFICATION_LEVELS: "Tag"
    JIRA_DASHBOARDS: "Tag"
    JIRA_DYNAMIC_MODULES: "Tag"
    JIRA_FILTERS: "Tag"
    JIRA_FILTER_SHARING: "Tag"
    JIRA_GROUPS: "Tag"
    JIRA_GROUP_AND_USER_PICKER: "Tag"
    JIRA_IMPORTANT: "Tag"
    JIRA_ISSUES: "Tag"
    JIRA_ISSUE_ATTACHMENTS: "Tag"
    JIRA_ISSUE_COMMENTS: "Tag"
    JIRA_ISSUE_COMMENT_PROPERTIES: "Tag"
    JIRA_ISSUE_CUSTOM_FIELD_CONFIGURATION__APPS_: "Tag"
    JIRA_ISSUE_CUSTOM_FIELD_CONTEXTS: "Tag"
    JIRA_ISSUE_CUSTOM_FIELD_OPTIONS: "Tag"
    JIRA_ISSUE_CUSTOM_FIELD_OPTIONS__APPS_: "Tag"
    JIRA_ISSUE_CUSTOM_FIELD_VALUES__APPS_: "Tag"
    JIRA_ISSUE_FIELDS: "Tag"
    JIRA_ISSUE_FIELD_CONFIGURATIONS: "Tag"
    JIRA_ISSUE_LINKS: "Tag"
    JIRA_ISSUE_LINK_TYPES: "Tag"
    JIRA_ISSUE_NAVIGATOR_SETTINGS: "Tag"
    JIRA_ISSUE_NOTIFICATION_SCHEMES: "Tag"
    JIRA_ISSUE_PRIORITIES: "Tag"
    JIRA_ISSUE_PROPERTIES: "Tag"
    JIRA_ISSUE_REMOTE_LINKS: "Tag"
    JIRA_ISSUE_RESOLUTIONS: "Tag"
    JIRA_ISSUE_SEARCH: "Tag"
    JIRA_ISSUE_SECURITY_LEVEL: "Tag"
    JIRA_ISSUE_SECURITY_SCHEMES: "Tag"
    JIRA_ISSUE_TYPES: "Tag"
    JIRA_ISSUE_TYPE_PROPERTIES: "Tag"
    JIRA_ISSUE_TYPE_SCHEMES: "Tag"
    JIRA_ISSUE_TYPE_SCREEN_SCHEMES: "Tag"
    JIRA_ISSUE_VOTES: "Tag"
    JIRA_ISSUE_WATCHERS: "Tag"
    JIRA_ISSUE_WORKLOGS: "Tag"
    JIRA_ISSUE_WORKLOG_PROPERTIES: "Tag"
    JIRA_JIRA_EXPRESSIONS: "Tag"
    JIRA_JIRA_SETTINGS: "Tag"
    JIRA_JQL: "Tag"
    JIRA_JQL_FUNCTIONS__APPS_: "Tag"
    JIRA_LABELS: "Tag"
    JIRA_LICENSE_METRICS: "Tag"
    JIRA_MYSELF: "Tag"
    JIRA_PERMISSIONS: "Tag"
    JIRA_PERMISSION_SCHEMES: "Tag"
    JIRA_PROJECTS: "Tag"
    JIRA_PROJECT_AVATARS: "Tag"
    JIRA_PROJECT_CATEGORIES: "Tag"
    JIRA_PROJECT_CLASSIFICATION_LEVELS: "Tag"
    JIRA_PROJECT_COMPONENTS: "Tag"
    JIRA_PROJECT_EMAIL: "Tag"
    JIRA_PROJECT_FEATURES: "Tag"
    JIRA_PROJECT_KEY_AND_NAME_VALIDATION: "Tag"
    JIRA_PROJECT_PERMISSION_SCHEMES: "Tag"
    JIRA_PROJECT_PROPERTIES: "Tag"
    JIRA_PROJECT_ROLES: "Tag"
    JIRA_PROJECT_ROLE_ACTORS: "Tag"
    JIRA_PROJECT_TYPES: "Tag"
    JIRA_PROJECT_VERSIONS: "Tag"
    JIRA_SCREENS: "Tag"
    JIRA_SCREEN_SCHEMES: "Tag"
    JIRA_SCREEN_TABS: "Tag"
    JIRA_SCREEN_TAB_FIELDS: "Tag"
    JIRA_SERVER_INFO: "Tag"
    JIRA_SERVICE_REGISTRY: "Tag"
    JIRA_STATUS: "Tag"
    JIRA_TASKS: "Tag"
    JIRA_TIME_TRACKING: "Tag"
    JIRA_UI_MODIFICATIONS__APPS_: "Tag"
    JIRA_USERS: "Tag"
    JIRA_USER_PROPERTIES: "Tag"
    JIRA_USER_SEARCH: "Tag"
    JIRA_WEBHOOKS: "Tag"
    JIRA_WORKFLOWS: "Tag"
    JIRA_WORKFLOW_SCHEMES: "Tag"
    JIRA_WORKFLOW_SCHEME_DRAFTS: "Tag"
    JIRA_WORKFLOW_SCHEME_PROJECT_ASSOCIATIONS: "Tag"
    JIRA_WORKFLOW_STATUSES: "Tag"
    JIRA_WORKFLOW_STATUS_CATEGORIES: "Tag"
    JIRA_WORKFLOW_TRANSITION_PROPERTIES: "Tag"
    JIRA_WORKFLOW_TRANSITION_RULES: "Tag"
    KLAVIYO_ACCOUNTS: "Tag"
    KLAVIYO_CAMPAIGNS: "Tag"
    KLAVIYO_CATALOGS: "Tag"
    KLAVIYO_CLIENT: "Tag"
    KLAVIYO_COUPONS: "Tag"
    KLAVIYO_DATA_PRIVACY: "Tag"
    KLAVIYO_EVENTS: "Tag"
    KLAVIYO_FLOWS: "Tag"
    KLAVIYO_FORMS: "Tag"
    KLAVIYO_IMAGES: "Tag"
    KLAVIYO_IMPORTANT: "Tag"
    KLAVIYO_LISTS: "Tag"
    KLAVIYO_METRICS: "Tag"
    KLAVIYO_PROFILES: "Tag"
    KLAVIYO_REPORTING: "Tag"
    KLAVIYO_SEGMENTS: "Tag"
    KLAVIYO_TAGS: "Tag"
    KLAVIYO_TEMPLATES: "Tag"
    KLAVIYO_WEBHOOKS: "Tag"
    LISTENNOTES_DIRECTORY_API: "Tag"
    LISTENNOTES_IMPORTANT: "Tag"
    LISTENNOTES_INSIGHTS_API: "Tag"
    LISTENNOTES_PLAYLIST_API: "Tag"
    LISTENNOTES_PODCASTER_API: "Tag"
    LISTENNOTES_SEARCH_API: "Tag"
    MAILCHIMP_ACCOUNTEXPORT: "Tag"
    MAILCHIMP_ACCOUNTEXPORTS: "Tag"
    MAILCHIMP_ACTIVITYFEED: "Tag"
    MAILCHIMP_AUTHORIZEDAPPS: "Tag"
    MAILCHIMP_AUTOMATIONS: "Tag"
    MAILCHIMP_BATCHES: "Tag"
    MAILCHIMP_BATCHWEBHOOKS: "Tag"
    MAILCHIMP_CAMPAIGNFOLDERS: "Tag"
    MAILCHIMP_CAMPAIGNS: "Tag"
    MAILCHIMP_CONNECTEDSITES: "Tag"
    MAILCHIMP_CONVERSATIONS: "Tag"
    MAILCHIMP_CUSTOMERJOURNEYS: "Tag"
    MAILCHIMP_ECOMMERCE: "Tag"
    MAILCHIMP_FACEBOOKADS: "Tag"
    MAILCHIMP_FILEMANAGER: "Tag"
    MAILCHIMP_IMPORTANT: "Tag"
    MAILCHIMP_LANDINGPAGES: "Tag"
    MAILCHIMP_LISTS: "Tag"
    MAILCHIMP_PING: "Tag"
    MAILCHIMP_REPORTING: "Tag"
    MAILCHIMP_REPORTS: "Tag"
    MAILCHIMP_ROOT: "Tag"
    MAILCHIMP_SEARCHCAMPAIGNS: "Tag"
    MAILCHIMP_SEARCHMEMBERS: "Tag"
    MAILCHIMP_SURVEYS: "Tag"
    MAILCHIMP_TEMPLATEFOLDERS: "Tag"
    MAILCHIMP_TEMPLATES: "Tag"
    MAILCHIMP_VERIFIEDDOMAINS: "Tag"
    NASA_ORGANIZATION: "Tag"
    NASA_PROJECT: "Tag"
    NASA_RESOURCE: "Tag"
    NOTION_IMPORTANT: "Tag"
    PIPEDRIVE_ACTIVITIES: "Tag"
    PIPEDRIVE_ACTIVITYFIELDS: "Tag"
    PIPEDRIVE_ACTIVITYTYPES: "Tag"
    PIPEDRIVE_BILLING: "Tag"
    PIPEDRIVE_CALLLOGS: "Tag"
    PIPEDRIVE_CHANNELS: "Tag"
    PIPEDRIVE_CURRENCIES: "Tag"
    PIPEDRIVE_DEALFIELDS: "Tag"
    PIPEDRIVE_DEALS: "Tag"
    PIPEDRIVE_FILES: "Tag"
    PIPEDRIVE_FILTERS: "Tag"
    PIPEDRIVE_GOALS: "Tag"
    PIPEDRIVE_IMPORTANT: "Tag"
    PIPEDRIVE_ITEMSEARCH: "Tag"
    PIPEDRIVE_LEADLABELS: "Tag"
    PIPEDRIVE_LEADS: "Tag"
    PIPEDRIVE_LEADSOURCES: "Tag"
    PIPEDRIVE_LEGACYTEAMS: "Tag"
    PIPEDRIVE_MAILBOX: "Tag"
    PIPEDRIVE_MEETINGS: "Tag"
    PIPEDRIVE_NOTEFIELDS: "Tag"
    PIPEDRIVE_NOTES: "Tag"
    PIPEDRIVE_OAUTH: "Tag"
    PIPEDRIVE_ORGANIZATIONFIELDS: "Tag"
    PIPEDRIVE_ORGANIZATIONRELATIONSHIPS: "Tag"
    PIPEDRIVE_ORGANIZATIONS: "Tag"
    PIPEDRIVE_PERMISSIONSETS: "Tag"
    PIPEDRIVE_PERSONFIELDS: "Tag"
    PIPEDRIVE_PERSONS: "Tag"
    PIPEDRIVE_PIPELINES: "Tag"
    PIPEDRIVE_PRODUCTFIELDS: "Tag"
    PIPEDRIVE_PRODUCTS: "Tag"
    PIPEDRIVE_PROJECTS: "Tag"
    PIPEDRIVE_PROJECTTEMPLATES: "Tag"
    PIPEDRIVE_RECENTS: "Tag"
    PIPEDRIVE_ROLES: "Tag"
    PIPEDRIVE_STAGES: "Tag"
    PIPEDRIVE_SUBSCRIPTIONS: "Tag"
    PIPEDRIVE_TASKS: "Tag"
    PIPEDRIVE_USERCONNECTIONS: "Tag"
    PIPEDRIVE_USERS: "Tag"
    PIPEDRIVE_USERSETTINGS: "Tag"
    PIPEDRIVE_WEBHOOKS: "Tag"
    POSTHOG_ACTIONS: "Tag"
    POSTHOG_ACTIVITY_LOG: "Tag"
    POSTHOG_ANNOTATIONS: "Tag"
    POSTHOG_APP_METRICS: "Tag"
    POSTHOG_BATCH_EXPORTS: "Tag"
    POSTHOG_COHORTS: "Tag"
    POSTHOG_DASHBOARDS: "Tag"
    POSTHOG_DASHBOARD_TEMPLATES: "Tag"
    POSTHOG_DOMAINS: "Tag"
    POSTHOG_EARLY_ACCESS_FEATURE: "Tag"
    POSTHOG_EVENTS: "Tag"
    POSTHOG_EVENT_DEFINITIONS: "Tag"
    POSTHOG_EXPERIMENTS: "Tag"
    POSTHOG_EXPLICIT_MEMBERS: "Tag"
    POSTHOG_EXPORTS: "Tag"
    POSTHOG_FEATURE_FLAGS: "Tag"
    POSTHOG_FUNNEL: "Tag"
    POSTHOG_GROUPS: "Tag"
    POSTHOG_GROUPS_TYPES: "Tag"
    POSTHOG_IMPORTANT: "Tag"
    POSTHOG_INSIGHTS: "Tag"
    POSTHOG_INVITES: "Tag"
    POSTHOG_MEMBERS: "Tag"
    POSTHOG_NOTEBOOKS: "Tag"
    POSTHOG_ORGANIZATIONS: "Tag"
    POSTHOG_PERSONS: "Tag"
    POSTHOG_PIPELINE_DESTINATIONS: "Tag"
    POSTHOG_PIPELINE_DESTINATION_CONFIGS: "Tag"
    POSTHOG_PIPELINE_FRONTEND_APPS: "Tag"
    POSTHOG_PIPELINE_FRONTEND_APPS_CONFIGS: "Tag"
    POSTHOG_PIPELINE_IMPORT_APPS: "Tag"
    POSTHOG_PIPELINE_IMPORT_APPS_CONFIGS: "Tag"
    POSTHOG_PIPELINE_TRANSFORMATIONS: "Tag"
    POSTHOG_PIPELINE_TRANSFORMATION_CONFIGS: "Tag"
    POSTHOG_PLUGINS: "Tag"
    POSTHOG_PLUGIN_CONFIGS: "Tag"
    POSTHOG_PROJECTS: "Tag"
    POSTHOG_PROPERTY_DEFINITIONS: "Tag"
    POSTHOG_PROXY_RECORDS: "Tag"
    POSTHOG_QUERY: "Tag"
    POSTHOG_ROLES: "Tag"
    POSTHOG_SESSIONS: "Tag"
    POSTHOG_SESSION_RECORDINGS: "Tag"
    POSTHOG_SESSION_RECORDING_PLAYLISTS: "Tag"
    POSTHOG_SUBSCRIPTIONS: "Tag"
    POSTHOG_SURVEYS: "Tag"
    POSTHOG_TREND: "Tag"
    POSTHOG_USERS: "Tag"
    SALESFORCE_ACCOUNT: "Tag"
    SALESFORCE_CAMPAIGN: "Tag"
    SALESFORCE_CONTACT: "Tag"
    SALESFORCE_IMPORTANT: "Tag"
    SALESFORCE_LEAD: "Tag"
    SALESFORCE_NOTE: "Tag"
    SALESFORCE_OPPORTUNITY: "Tag"
    SLACKBOT_ADMIN: "Tag"
    SLACKBOT_ADMIN_APPS: "Tag"
    SLACKBOT_ADMIN_APPS_APPROVED: "Tag"
    SLACKBOT_ADMIN_APPS_REQUESTS: "Tag"
    SLACKBOT_ADMIN_APPS_RESTRICTED: "Tag"
    SLACKBOT_ADMIN_CONVERSATIONS: "Tag"
    SLACKBOT_ADMIN_CONVERSATIONS_EKM: "Tag"
    SLACKBOT_ADMIN_CONVERSATIONS_RESTRICTACCESS: "Tag"
    SLACKBOT_ADMIN_EMOJI: "Tag"
    SLACKBOT_ADMIN_INVITEREQUESTS: "Tag"
    SLACKBOT_ADMIN_INVITEREQUESTS_APPROVED: "Tag"
    SLACKBOT_ADMIN_INVITEREQUESTS_DENIED: "Tag"
    SLACKBOT_ADMIN_TEAMS: "Tag"
    SLACKBOT_ADMIN_TEAMS_ADMINS: "Tag"
    SLACKBOT_ADMIN_TEAMS_OWNERS: "Tag"
    SLACKBOT_ADMIN_TEAMS_SETTINGS: "Tag"
    SLACKBOT_ADMIN_USERGROUPS: "Tag"
    SLACKBOT_ADMIN_USERS: "Tag"
    SLACKBOT_ADMIN_USERS_SESSION: "Tag"
    SLACKBOT_API: "Tag"
    SLACKBOT_APPS: "Tag"
    SLACKBOT_APPS_EVENT_AUTHORIZATIONS: "Tag"
    SLACKBOT_APPS_PERMISSIONS: "Tag"
    SLACKBOT_APPS_PERMISSIONS_RESOURCES: "Tag"
    SLACKBOT_APPS_PERMISSIONS_SCOPES: "Tag"
    SLACKBOT_APPS_PERMISSIONS_USERS: "Tag"
    SLACKBOT_AUTH: "Tag"
    SLACKBOT_BOTS: "Tag"
    SLACKBOT_CALLS: "Tag"
    SLACKBOT_CALLS_PARTICIPANTS: "Tag"
    SLACKBOT_CHAT: "Tag"
    SLACKBOT_CHAT_SCHEDULEDMESSAGES: "Tag"
    SLACKBOT_CONVERSATIONS: "Tag"
    SLACKBOT_DIALOG: "Tag"
    SLACKBOT_DND: "Tag"
    SLACKBOT_EMOJI: "Tag"
    SLACKBOT_FILES: "Tag"
    SLACKBOT_FILES_COMMENTS: "Tag"
    SLACKBOT_FILES_REMOTE: "Tag"
    SLACKBOT_IMPORTANT: "Tag"
    SLACKBOT_MIGRATION: "Tag"
    SLACKBOT_OAUTH: "Tag"
    SLACKBOT_OAUTH_V2: "Tag"
    SLACKBOT_PINS: "Tag"
    SLACKBOT_REACTIONS: "Tag"
    SLACKBOT_REMINDERS: "Tag"
    SLACKBOT_RTM: "Tag"
    SLACKBOT_SEARCH: "Tag"
    SLACKBOT_STARS: "Tag"
    SLACKBOT_TEAM: "Tag"
    SLACKBOT_TEAM_PROFILE: "Tag"
    SLACKBOT_USERGROUPS: "Tag"
    SLACKBOT_USERGROUPS_USERS: "Tag"
    SLACKBOT_USERS: "Tag"
    SLACKBOT_USERS_PROFILE: "Tag"
    SLACKBOT_VIEWS: "Tag"
    SLACKBOT_WORKFLOWS: "Tag"
    SLACK_ADMIN: "Tag"
    SLACK_ADMIN_APPS: "Tag"
    SLACK_ADMIN_APPS_APPROVED: "Tag"
    SLACK_ADMIN_APPS_REQUESTS: "Tag"
    SLACK_ADMIN_APPS_RESTRICTED: "Tag"
    SLACK_ADMIN_CONVERSATIONS: "Tag"
    SLACK_ADMIN_CONVERSATIONS_EKM: "Tag"
    SLACK_ADMIN_CONVERSATIONS_RESTRICTACCESS: "Tag"
    SLACK_ADMIN_EMOJI: "Tag"
    SLACK_ADMIN_INVITEREQUESTS: "Tag"
    SLACK_ADMIN_INVITEREQUESTS_APPROVED: "Tag"
    SLACK_ADMIN_INVITEREQUESTS_DENIED: "Tag"
    SLACK_ADMIN_TEAMS: "Tag"
    SLACK_ADMIN_TEAMS_ADMINS: "Tag"
    SLACK_ADMIN_TEAMS_OWNERS: "Tag"
    SLACK_ADMIN_TEAMS_SETTINGS: "Tag"
    SLACK_ADMIN_USERGROUPS: "Tag"
    SLACK_ADMIN_USERS: "Tag"
    SLACK_ADMIN_USERS_SESSION: "Tag"
    SLACK_API: "Tag"
    SLACK_APPS: "Tag"
    SLACK_APPS_EVENT_AUTHORIZATIONS: "Tag"
    SLACK_APPS_PERMISSIONS: "Tag"
    SLACK_APPS_PERMISSIONS_RESOURCES: "Tag"
    SLACK_APPS_PERMISSIONS_SCOPES: "Tag"
    SLACK_APPS_PERMISSIONS_USERS: "Tag"
    SLACK_AUTH: "Tag"
    SLACK_BOTS: "Tag"
    SLACK_CALLS: "Tag"
    SLACK_CALLS_PARTICIPANTS: "Tag"
    SLACK_CHAT: "Tag"
    SLACK_CHAT_SCHEDULEDMESSAGES: "Tag"
    SLACK_CONVERSATIONS: "Tag"
    SLACK_DIALOG: "Tag"
    SLACK_DND: "Tag"
    SLACK_EMOJI: "Tag"
    SLACK_FILES: "Tag"
    SLACK_FILES_COMMENTS: "Tag"
    SLACK_FILES_REMOTE: "Tag"
    SLACK_IMPORTANT: "Tag"
    SLACK_MIGRATION: "Tag"
    SLACK_OAUTH: "Tag"
    SLACK_OAUTH_V2: "Tag"
    SLACK_PINS: "Tag"
    SLACK_REACTIONS: "Tag"
    SLACK_REMINDERS: "Tag"
    SLACK_RTM: "Tag"
    SLACK_SEARCH: "Tag"
    SLACK_STARS: "Tag"
    SLACK_TEAM: "Tag"
    SLACK_TEAM_PROFILE: "Tag"
    SLACK_USERGROUPS: "Tag"
    SLACK_USERGROUPS_USERS: "Tag"
    SLACK_USERS: "Tag"
    SLACK_USERS_PROFILE: "Tag"
    SLACK_VIEWS: "Tag"
    SLACK_WORKFLOWS: "Tag"
    TRELLO_ACTION: "Tag"
    TRELLO_BATCH: "Tag"
    TRELLO_BOARD: "Tag"
    TRELLO_CARD: "Tag"
    TRELLO_CHECKLIST: "Tag"
    TRELLO_IMPORTANT: "Tag"
    TRELLO_LABEL: "Tag"
    TRELLO_LIST: "Tag"
    TRELLO_MEMBER: "Tag"
    TRELLO_NOTIFICATION: "Tag"
    TRELLO_ORGANIZATION: "Tag"
    TRELLO_SEARCH: "Tag"
    TRELLO_SESSION: "Tag"
    TRELLO_TOKEN: "Tag"
    TRELLO_TYPE: "Tag"
    TRELLO_WEBHOOK: "Tag"
    TWITTER_BOOKMARKS: "Tag"
    TWITTER_COMPLIANCE: "Tag"
    TWITTER_DIRECT_MESSAGES: "Tag"
    TWITTER_GENERAL: "Tag"
    TWITTER_IMPORTANT: "Tag"
    TWITTER_LISTS: "Tag"
    TWITTER_SPACES: "Tag"
    TWITTER_TWEETS: "Tag"
    TWITTER_USAGE: "Tag"
    TWITTER_USERS: "Tag"

    @property
    def app(self) -> str:
        """App name for this tag."""
        return self.load().app

    @property
    def value(self) -> str:
        """Tag string."""
        return self.load().value
