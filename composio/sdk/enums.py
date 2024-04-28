from enum import Enum


class Tag(Enum):
    IMPORTANT = "important"


class App(Enum):
    ASANA = "asana"
    LINEAR = "linear"
    SLACK = "slack"
    BITBUCKET = "bitbucket"
    STRAVA = "strava"
    DROPBOX = "dropbox"
    PAGERDUTY = "pagerduty"
    FIGMA = "figma"
    CLICKUP = "clickup"
    MIRO = "miro"
    GUMROAD = "gumroad"
    KLAVIYO = "klaviyo"
    FRESHDESK = "freshdesk"
    MIXPANEL = "mixpanel"
    INTERCOM = "intercom"
    STACK_EXCHANGE = "stack-exchange"
    ZOHO = "zoho"
    SPLITWISE = "splitwise"
    NOTION = "notion"
    TASKADE = "taskade"
    TYPEFORM = "typeform"
    PIPEDRIVE = "pipedrive"
    MONDAY = "monday"
    SHOPIFY = "shopify"
    TWITTER = "twitter"
    BOLDSIGN = "boldsign"
    KEAP = "keap"
    GCALENDAR = "gcalendar"
    ONE_DRIVE = "one-drive"
    SMUGMUG = "smugmug"
    TRELLO = "trello"
    ZOHO_BIGIN = "zoho-bigin"
    ZOHO_BOOKS = "zoho-books"
    ZOHO_DESK = "zoho-desk"
    ZOHO_INVENTORY = "zoho-inventory"
    ZOHO_INVOICE = "zoho-invoice"
    ZOHO_MAIL = "zoho-mail"
    TEST_ASANA = "test_asana"
    BOX = "box"
    JIRA = "jira"
    AMAZON = "amazon"
    GMAIL = "gmail"
    TINYURL = "tinyurl"
    REDDIT = "reddit"
    SERVICEM8 = "servicem8"
    SHORTCUT = "shortcut"
    FRONT = "front"
    SURVEY_MONKEY = "survey-monkey"
    WAKATIME = "wakatime"
    DISCORD = "discord"
    TWITCH = "twitch"
    ATLASSIAN = "atlassian"
    HARVEST = "harvest"
    CALENDLY = "calendly"
    BAMBOOHR = "bamboohr"
    GITHUB = "github"
    DEEL = "deel"
    GITLAB = "gitlab"
    HUBSPOT = "hubspot"
    SLACKBOT = "slackbot"
    YANDEX = "yandex"
    BRAINTREE = "braintree"
    FRESHBOOKS = "freshbooks"
    AUTH0 = "auth0"
    OKTA = "okta"
    SMARTRECRUITERS = "smartrecruiters"
    FACEBOOK = "facebook"
    YOUTUBE = "youtube"
    ASHBY = "ashby"
    AMPLITUDE = "amplitude"
    HEROKU = "heroku"
    SAGE = "sage"
    WAVE_ACCOUNTING = "wave-accounting"
    CLOSE = "close"
    PANDADOC = "pandadoc"
    BLACKBAUD = "blackbaud"
    GURU = "guru"
    SERPAPI = "serpapi"
    BATTLENET = "battlenet"
    LINKHUT = "linkhut"
    XERO = "xero"
    APIFY = "apify"
    LINEARSANDBOX = "linearsandbox"
    ZENDESK = "zendesk"
    RING_CENTRAL = "ring-central"
    CODEINTERPRETER = "codeinterpreter"
    ACCELO = "accelo"
    ABLY = "ably"
    ADOBE = "adobe"
    AERO_WORKFLOW = "aero-workflow"
    ALCHEMY = "alchemy"
    AMCARDS = "amcards"
    APPDRAG = "appdrag"
    BREX_STAGING = "brex-staging"
    BROWSEAI = "browseai"
    BROWSERHUB = "browserhub"
    BUBBLE = "bubble"
    CAL = "cal"
    CHATWORK = "chatwork"
    CHMEETINGS = "chmeetings"
    CONTENTFUL = "contentful"
    CUSTOMER_IO = "customer_io"
    FACTORIAL = "factorial"
    FILEMANAGER = "filemanager"
    FITBIT = "fitbit"
    NETSUITE = "netsuite"
    NGROK = "ngrok"
    PRINTNODE = "printnode"
    PROCESS_STREET = "process-street"
    RAVENSEOTOOLS = "ravenseotools"
    SALESFORCE = "salesforce"
    SNOWFLAKE = "snowflake"
    TEXTRAZOR = "textrazor"
    TIMEKIT = "timekit"
    TINYPNG = "tinypng"
    AXONAUT = "axonaut"
    BANNERBEAR = "bannerbear"
    BASEROW = "baserow"
    BEEMINDER = "beeminder"
    BITWARDEN = "bitwarden"
    BRANDFETCH = "brandfetch"
    BREVO = "brevo"
    DATAGMA = "datagma"
    LAUNCH_DARKLY = "launch-darkly"
    TODOIST = "todoist"
    TONEDEN = "toneden"
    VENLY = "venly"
    WABOXAPP = "waboxapp"
    WORKABLE = "workable"
    WORKSPACE = "workspace"
    BREX = "brex"
    DATADOG = "datadog"
    DEMIO = "demio"
    DIGICERT = "digicert"
    DROPBOX_SIGN = "dropbox-sign"
    ECHTPOST = "echtpost"
    EPIC_GAMES = "epic-games"
    EXA = "exa"
    EXIST = "exist"
    GOOGLE_DRIVE = "google-drive"
    GORGIAS = "gorgias"
    HIGHLEVEL = "highlevel"
    GOOGLE_DOCS = "google-docs"
    GOOGLE_SHEETS = "google-sheets"
    MAILCHIMP = "mailchimp"
    TIMELY = "timely"
    ZOOM = "zoom"
    ATTIO = "attio"
    EVENTBRITE = "eventbrite"
    HACKERRANK_WORK = "hackerrank-work"
    KLIPFOLIO = "klipfolio"
    LASTPASS = "lastpass"
    LEXOFFICE = "lexoffice"
    MAINTAINX = "maintainx"
    MICROSOFT_TEAMS = "microsoft-teams"
    MICROSOFT_TENANT = "microsoft-tenant"
    MOXIE = "moxie"
    MURAL = "mural"
    SQUARE = "square"
    TAPFORM = "tapform"


class Action(Enum):
    def __init__(self, service, action, no_auth):
        self.service = service
        self.action = action
        self.no_auth = no_auth

    ASANA_CREATE_SUBTASK = ("asana", "asana_create_subtask", False)
    ASANA_GET_SUBTASKS = ("asana", "asana_get_subtasks", False)
    LINEAR_CREATE_LINEAR_ISSUE = ("linear", "linear_create_linear_issue", False)
    LINEAR_LIST_LINEAR_PROJECTS = ("linear", "linear_list_linear_projects", False)
    LINEAR_LIST_LINEAR_TEAMS = ("linear", "linear_list_linear_teams", False)
    SLACK_SEND_SLACK_MESSAGE = ("slack", "slack_send_slack_message", False)
    SLACK_LIST_SLACK_CHANNELS = ("slack", "slack_list_slack_channels", False)
    SLACK_LIST_SLACK_MEMBERS = ("slack", "slack_list_slack_members", False)
    SLACK_LIST_SLACK_MESSAGES = ("slack", "slack_list_slack_messages", False)
    DROPBOX_GET_ABOUT_ME = ("dropbox", "dropbox_get_about_me", False)
    CLICKUP_CREATE_TASK = ("clickup", "clickup_create_task", False)
    CLICKUP_GET_TASKS = ("clickup", "clickup_get_tasks", False)
    CLICKUP_GET_TASK = ("clickup", "clickup_get_task", False)
    CLICKUP_CREATE_LIST = ("clickup", "clickup_create_list", False)
    CLICKUP_GET_LISTS = ("clickup", "clickup_get_lists", False)
    CLICKUP_GET_SPACES = ("clickup", "clickup_get_spaces", False)
    CLICKUP_CREATE_SPACE = ("clickup", "clickup_create_space", False)
    CLICKUP_CREATE_FOLDER = ("clickup", "clickup_create_folder", False)
    CLICKUP_GET_FOLDERS = ("clickup", "clickup_get_folders", False)
    NOTION_GET_ABOUT_ME = ("notion", "notion_get_about_me", False)
    NOTION_ADD_NOTION_PAGE_CHILDREN = (
        "notion",
        "notion_add_notion_page_children",
        False,
    )
    NOTION_ARCHIVE_NOTION_PAGE = ("notion", "notion_archive_notion_page", False)
    NOTION_CREATE_NOTION_DATABASE = ("notion", "notion_create_notion_database", False)
    NOTION_CREATE_PAGE_COMMENT = ("notion", "notion_create_page_comment", False)
    NOTION_CREATE_NOTION_PAGE = ("notion", "notion_create_notion_page", False)
    NOTION_DELETE_NOTION_PAGE_CHILDREN = (
        "notion",
        "notion_delete_notion_page_children",
        False,
    )
    NOTION_FETCH_NOTION_COMMENT = ("notion", "notion_fetch_notion_comment", False)
    NOTION_FETCH_NOTION_DATABASE = ("notion", "notion_fetch_notion_database", False)
    NOTION_FETCH_NOTION_PAGE = ("notion", "notion_fetch_notion_page", False)
    NOTION_SEARCH_NOTION_PAGE = ("notion", "notion_search_notion_page", False)
    NOTION_UPDATE_NOTION_DATABASE = ("notion", "notion_update_notion_database", False)
    NOTION_FETCH_NOTION_BLOCK = ("notion", "notion_fetch_notion_block", False)
    NOTION_FETCH_NOTION_CHILD_BLOCK = (
        "notion",
        "notion_fetch_notion_child_block",
        False,
    )
    TYPEFORM_GET_ABOUT_ME = ("typeform", "typeform_get_about_me", False)
    GOOGLECALENDAR_CREATE_GOOGLE_EVENT = (
        "gcalendar",
        "googlecalendar_create_google_event",
        False,
    )
    GOOGLECALENDAR_REMOVE_ATTENDEE = (
        "gcalendar",
        "googlecalendar_remove_attendee",
        False,
    )
    GOOGLECALENDAR_FIND_EVENT = ("gcalendar", "googlecalendar_find_event", False)
    GOOGLECALENDAR_DELETE_GOOGLE_EVENT = (
        "gcalendar",
        "googlecalendar_delete_google_event",
        False,
    )
    GOOGLECALENDAR_UPDATE_GOOGLE_EVENT = (
        "gcalendar",
        "googlecalendar_update_google_event",
        False,
    )
    GOOGLECALENDAR_FIND_FREE_SLOTS = (
        "gcalendar",
        "googlecalendar_find_free_slots",
        False,
    )
    GOOGLECALENDAR_DUPLICATE_GOOGLE_CALENDAR = (
        "gcalendar",
        "googlecalendar_duplicate_google_calendar",
        False,
    )
    GOOGLECALENDAR_LIST_GOOGLE_CALENDARS = (
        "gcalendar",
        "googlecalendar_list_google_calendars",
        False,
    )
    GOOGLECALENDAR_PATCH_GOOGLE_CALENDAR = (
        "gcalendar",
        "googlecalendar_patch_google_calendar",
        False,
    )
    GOOGLECALENDAR_QUICK_ADD_GOOGLE_CALENDAR = (
        "gcalendar",
        "googlecalendar_quick_add_google_calendar",
        False,
    )
    GOOGLECALENDAR_GET_CURRENT_DATE_TIME = (
        "gcalendar",
        "googlecalendar_get_current_date_time",
        False,
    )
    TRELLO_CREATE_TRELLO_LIST = ("trello", "trello_create_trello_list", False)
    TRELLO_CREATE_TRELLO_CARD = ("trello", "trello_create_trello_card", False)
    TRELLO_GET_TRELLO_BOARD_CARDS = ("trello", "trello_get_trello_board_cards", False)
    TRELLO_DELETE_TRELLO_CARD = ("trello", "trello_delete_trello_card", False)
    TRELLO_ADD_TRELLO_CARD_COMMENT = ("trello", "trello_add_trello_card_comment", False)
    TRELLO_CREATE_TRELLO_LABEL = ("trello", "trello_create_trello_label", False)
    TRELLO_UPDATE_TRELLO_BOARD = ("trello", "trello_update_trello_board", False)
    TRELLO_GET_ABOUT_ME = ("trello", "trello_get_about_me", False)
    TRELLO_SEARCH_TRELLO = ("trello", "trello_search_trello", False)
    TRELLO_SEARCH_TRELLO_MEMBER = ("trello", "trello_search_trello_member", False)
    TRELLO_UPDATE_TRELLO_CARD = ("trello", "trello_update_trello_card", False)
    TRELLO_GET_TRELLO_MEMBER_BOARD = ("trello", "trello_get_trello_member_board", False)
    GMAIL_SEND_EMAIL = ("gmail", "gmail_send_email", False)
    GMAIL_CREATE_EMAIL_DRAFT = ("gmail", "gmail_create_email_draft", False)
    GMAIL_FIND_EMAIL_ID = ("gmail", "gmail_find_email_id", False)
    GMAIL_FETCH_LAST_THREE_MESSAGES = (
        "gmail",
        "gmail_fetch_last_three_messages",
        False,
    )
    GMAIL_ADD_LABEL_TO_EMAIL = ("gmail", "gmail_add_label_to_email", False)
    GMAIL_LIST_LABELS = ("gmail", "gmail_list_labels", False)
    GMAIL_FETCH_MESSAGE_BY_THREAD_ID = (
        "gmail",
        "gmail_fetch_message_by_thread_id",
        False,
    )
    GMAIL_REPLY_TO_THREAD = ("gmail", "gmail_reply_to_thread", False)
    GMAIL_FETCH_EMAILS_WITH_LABEL = ("gmail", "gmail_fetch_emails_with_label", False)
    GITHUB_CREATE_ISSUE = ("github", "github_create_issue", False)
    GITHUB_LIST_GITHUB_REPOS = ("github", "github_list_github_repos", False)
    GITHUB_STAR_REPO = ("github", "github_star_repo", False)
    GITHUB_GET_ABOUT_ME = ("github", "github_get_about_me", False)
    GITHUB_FETCH_README = ("github", "github_fetch_readme", False)
    GITHUB_GET_COMMITS = ("github", "github_get_commits", False)
    GITHUB_GET_COMMITS_WITH_CODE = ("github", "github_get_commits_with_code", False)
    GITHUB_GET_PATCH_FOR_COMMIT = ("github", "github_get_patch_for_commit", False)
    SLACKBOT_SEND_SLACK_MESSAGE = ("slackbot", "slackbot_send_slack_message", False)
    SLACKBOT_LIST_SLACK_CHANNELS = ("slackbot", "slackbot_list_slack_channels", False)
    SLACKBOT_LIST_SLACK_MEMBERS = ("slackbot", "slackbot_list_slack_members", False)
    SLACKBOT_LIST_SLACK_MESSAGES = ("slackbot", "slackbot_list_slack_messages", False)
    SERPAPI_SEARCH = ("serpapi", "serpapi_search", True)
    APIFY_LIST_APIFY_ACTORS = ("apify", "apify_list_apify_actors", False)
    APIFY_CREATE_APIFY_ACTOR = ("apify", "apify_create_apify_actor", False)
    APIFY_GET_ACTOR_ID = ("apify", "apify_get_actor_id", False)
    APIFY_SEARCH_STORE = ("apify", "apify_search_store", False)
    APIFY_GET_LAST_RUN_DATA = ("apify", "apify_get_last_run_data", False)
    APIFY_LIST_APIFY_TASKS = ("apify", "apify_list_apify_tasks", False)
    ZENDESK_CREATE_ZENDESK_ORGANIZATION = (
        "zendesk",
        "zendesk_create_zendesk_organization",
        False,
    )
    ZENDESK_DELETE_ZENDESK_ORGANIZATION = (
        "zendesk",
        "zendesk_delete_zendesk_organization",
        False,
    )
    ZENDESK_COUNT_ZENDESK_ORGANIZATIONS = (
        "zendesk",
        "zendesk_count_zendesk_organizations",
        False,
    )
    ZENDESK_GET_ZENDESK_ORGANIZATION = (
        "zendesk",
        "zendesk_get_zendesk_organization",
        False,
    )
    ZENDESK_GET_ALL_ZENDESK_ORGANIZATIONS = (
        "zendesk",
        "zendesk_get_all_zendesk_organizations",
        False,
    )
    ZENDESK_UPDATE_ZENDESK_ORGANIZATION = (
        "zendesk",
        "zendesk_update_zendesk_organization",
        False,
    )
    ZENDESK_CREATE_ZENDESK_TICKET = ("zendesk", "zendesk_create_zendesk_ticket", False)
    ZENDESK_DELETE_ZENDESK_TICKET = ("zendesk", "zendesk_delete_zendesk_ticket", False)
    ZENDESK_GET_ABOUT_ME = ("zendesk", "zendesk_get_about_me", False)
    CODEINTERPRETER_EXECUTE_CODE = (
        "codeinterpreter",
        "codeinterpreter_execute_code",
        True,
    )
    FILEMANAGER_CREATE_SHELL_ACTION = (
        "filemanager",
        "filemanager_create_shell_action",
        True,
    )
    FILEMANAGER_CLOSE_SHELL_ACTION = (
        "filemanager",
        "filemanager_close_shell_action",
        True,
    )
    FILEMANAGER_RUN_COMMAND_ACTION = (
        "filemanager",
        "filemanager_run_command_action",
        True,
    )
    FILEMANAGER_SET_ENV_VAR_ACTION = (
        "filemanager",
        "filemanager_set_env_var_action",
        True,
    )
    FILEMANAGER_OPEN_FILE_ACTION = ("filemanager", "filemanager_open_file_action", True)
    FILEMANAGER_GOTO_LINE_ACTION = ("filemanager", "filemanager_goto_line_action", True)
    FILEMANAGER_SCROLL_ACTION = ("filemanager", "filemanager_scroll_action", True)
    FILEMANAGER_CREATE_FILE_ACTION = (
        "filemanager",
        "filemanager_create_file_action",
        True,
    )
    FILEMANAGER_EDIT_FILE_ACTION = ("filemanager", "filemanager_edit_file_action", True)
    SNOWFLAKE_RUN_QUERY = ("snowflake", "snowflake_run_query", False)
    SNOWFLAKE_SHOW_TABLES = ("snowflake", "snowflake_show_tables", False)
    SNOWFLAKE_DESCRIBE_TABLE = ("snowflake", "snowflake_describe_table", False)
    SNOWFLAKE_EXPLORE_COLUMNS = ("snowflake", "snowflake_explore_columns", False)
    EXA_SEARCH = ("exa", "exa_search", True)
    EXA_SIMILARLINK = ("exa", "exa_similarlink", True)


class Trigger(Enum):
    def __init__(self, service, trigger):
        self.service = service
        self.trigger = trigger

    SLACK_NEW_MESSAGE = ("slack", "slack_receive_message")
    GITHUB_PULL_REQUEST_EVENT = ("github", "github_pull_request_event")
    GITHUB_COMMIT_EVENT = ("github", "github_commit_event")
    SLACKBOT_NEW_MESSAGE = ("slackbot", "slackbot_receive_message")
