from enum import Enum

class App(Enum):
    INTERCOM = "intercom"
    MIRO = "miro"
    BOX = "box"
    FIGMA = "figma"
    SHOPIFY = "shopify"
    JIRA = "jira"
    CALENDLY = "calendly"
    TIMELY = "timely"
    TWITCH = "twitch"
    SURVEY_MONKEY = "survey-monkey"
    KLAVIYO = "klaviyo"
    STRAVA = "strava"
    PIPEDRIVE = "pipedrive"
    ZENDESK = "zendesk"
    TRELLO = "trello"
    ZOHO_INVENTORY = "zoho_inventory"
    ZOHO_DESK = "zoho_desk"
    AMAZON = "amazon"
    SMARTRECRUITERS = "smartrecruiters"
    AMPLITUDE = "amplitude"
    DROPBOX = "dropbox"
    ACCELO = "accelo"
    EVENTBRITE = "eventbrite"
    WAKATIME = "wakatime"
    AUTH0 = "auth0"
    CLOSE = "close"
    WORKABLE = "workable"
    DEEL = "deel"
    SQUARE = "square"
    BATTLENET = "battlenet"
    WAVE_ACCOUNTING = "wave-accounting"
    BOLDSIGN = "boldsign"
    STACK_EXCHANGE = "stack-exchange"
    GURU = "guru"
    FACEBOOK = "facebook"
    ZOHO_BIGIN = "zoho_bigin"
    REDDIT = "reddit"
    HACKERRANK_WORK = "hackerrank-work"
    MONDAY = "monday"
    ADOBE = "adobe"
    RING_CENTRAL = "ring-central"
    GITHUB = "github"
    SLACK = "slack"
    GITLAB = "gitlab"
    SALESFORCE = "salesforce"
    APIFY = "apify"
    MAILCHIMP = "mailchimp"
    SERVICEM8 = "servicem8"
    ASHBY = "ashby"
    BITBUCKET = "bitbucket"
    SAGE = "sage"
    ZOHO_BOOKS = "zoho_books"
    ZOHO_MAIL = "zoho_mail"
    SMUGMUG = "smugmug"
    ZOOM = "zoom"
    ASANA = "asana"
    HUBSPOT = "hubspot"
    TEST_ASANA = "test_asana"
    ATTIO = "attio"
    GOOGLE_DRIVE = "google-drive"
    GMAIL = "gmail"
    FRESHDESK = "freshdesk"
    KEAP = "keap"
    SHORTCUT = "shortcut"
    TWITTER = "twitter"
    TYPEFORM = "typeform"
    BRAINTREE = "braintree"
    BLACKBAUD = "blackbaud"
    GUMROAD = "gumroad"
    YANDEX = "yandex"
    XERO = "xero"
    HARVEST = "harvest"
    ZOHO = "zoho"
    GORGIAS = "gorgias"
    DISCORD = "discord"
    LINEAR = "linear"
    MURAL = "mural"
    EPIC_GAMES = "epic-games"
    ONE_DRIVE = "one-drive"
    GOOGLE_DOCS = "google-docs"
    HEROKU = "heroku"
    LINEARSANDBOX = "linearsandbox"
    FRONT = "front"
    SLACKBOT = "slackbot"
    YOUTUBE = "youtube"
    PAGERDUTY = "pagerduty"
    TASKADE = "taskade"
    ZOHO_INVOICE = "zoho_invoice"
    TODOIST = "todoist"
    PANDADOC = "pandadoc"
    LINKHUT = "linkhut"
    HIGHLEVEL = "highlevel"
    CLICKUP = "clickup"
    NOTION = "notion"
    GOOGLE_SHEETS = "google-sheets"
    CODEINTERPRETER = "CodeInterpreter"
    SERPAPI = "serpapi"
    SPLITWISE = "splitwise"
    GOOGLECALENDAR = "googlecalendar"
    OKTA = "okta"
    BAMBOOHR = "bamboohr"
    FRESHBOOKS = "freshbooks"
    ATLASSIAN = "atlassian"
    MIXPANEL = "mixpanel"

class Action(Enum):
    def __init__(self, service, action):
        self.service = service
        self.action = action

    ZENDESK_CREATE_ZENDESK_ORGANIZATION = ("zendesk", "zendesk_create_zendesk_organization")
    ZENDESK_DELETE_ZENDESK_ORGANIZATION = ("zendesk", "zendesk_delete_zendesk_organization")
    ZENDESK_COUNT_ZENDESK_ORGANIZATIONS = ("zendesk", "zendesk_count_zendesk_organizations")
    ZENDESK_GET_ZENDESK_ORGANIZATION = ("zendesk", "zendesk_get_zendesk_organization")
    ZENDESK_GET_ALL_ZENDESK_ORGANIZATIONS = ("zendesk", "zendesk_get_all_zendesk_organizations")
    ZENDESK_UPDATE_ZENDESK_ORGANIZATION = ("zendesk", "zendesk_update_zendesk_organization")
    ZENDESK_CREATE_ZENDESK_TICKET = ("zendesk", "zendesk_create_zendesk_ticket")
    ZENDESK_DELETE_ZENDESK_TICKET = ("zendesk", "zendesk_delete_zendesk_ticket")
    ZENDESK_GET_ABOUT_ME = ("zendesk", "zendesk_get_about_me")
    TRELLO_CREATE_TRELLO_LIST = ("trello", "trello_create_trello_list")
    TRELLO_CREATE_TRELLO_CARD = ("trello", "trello_create_trello_card")
    TRELLO_GET_TRELLO_BOARD_CARDS = ("trello", "trello_get_trello_board_cards")
    TRELLO_DELETE_TRELLO_CARD = ("trello", "trello_delete_trello_card")
    TRELLO_ADD_TRELLO_CARD_COMMENT = ("trello", "trello_add_trello_card_comment")
    TRELLO_CREATE_TRELLO_LABEL = ("trello", "trello_create_trello_label")
    TRELLO_UPDATE_TRELLO_BOARD = ("trello", "trello_update_trello_board")
    TRELLO_GET_ABOUT_ME = ("trello", "trello_get_about_me")
    TRELLO_SEARCH_TRELLO = ("trello", "trello_search_trello")
    TRELLO_SEARCH_TRELLO_MEMBER = ("trello", "trello_search_trello_member")
    TRELLO_UPDATE_TRELLO_CARD = ("trello", "trello_update_trello_card")
    TRELLO_GET_TRELLO_MEMBER_BOARD = ("trello", "trello_get_trello_member_board")
    DROPBOX_GET_ABOUT_ME = ("dropbox", "dropbox_get_about_me")
    GITHUB_CREATE_ISSUE = ("github", "github_create_issue")
    GITHUB_LIST_GITHUB_REPOS = ("github", "github_list_github_repos")
    GITHUB_STAR_REPO = ("github", "github_star_repo")
    GITHUB_GET_ABOUT_ME = ("github", "github_get_about_me")
    GITHUB_FETCH_README = ("github", "github_fetch_readme")
    GITHUB_GET_COMMITS = ("github", "github_get_commits")
    GITHUB_GET_COMMITS_WITH_CODE = ("github", "github_get_commits_with_code")
    GITHUB_GET_PATCH_FOR_COMMIT = ("github", "github_get_patch_for_commit")
    SLACK_SEND_SLACK_MESSAGE = ("slack", "slack_send_slack_message")
    SLACK_LIST_SLACK_CHANNELS = ("slack", "slack_list_slack_channels")
    SLACK_LIST_SLACK_MEMBERS = ("slack", "slack_list_slack_members")
    SLACK_LIST_SLACK_MESSAGES = ("slack", "slack_list_slack_messages")
    APIFY_LIST_APIFY_ACTORS = ("apify", "apify_list_apify_actors")
    APIFY_CREATE_APIFY_ACTOR = ("apify", "apify_create_apify_actor")
    APIFY_GET_ACTOR_ID = ("apify", "apify_get_actor_id")
    APIFY_SEARCH_STORE = ("apify", "apify_search_store")
    APIFY_GET_LAST_RUN_DATA = ("apify", "apify_get_last_run_data")
    APIFY_LIST_APIFY_TASKS = ("apify", "apify_list_apify_tasks")
    ASANA_CREATE_SUBTASK = ("asana", "asana_create_subtask")
    ASANA_GET_SUBTASKS = ("asana", "asana_get_subtasks")
    TEST_ASANA_CREATE_SUBTASK = ("test_asana", "test_asana_create_subtask")
    TEST_ASANA_GET_SUBTASKS = ("test_asana", "test_asana_get_subtasks")
    GMAIL_SEND_EMAIL = ("gmail", "gmail_send_email")
    GMAIL_CREATE_EMAIL_DRAFT = ("gmail", "gmail_create_email_draft")
    GMAIL_FIND_EMAIL_ID = ("gmail", "gmail_find_email_id")
    GMAIL_FETCH_LAST_THREE_MESSAGES = ("gmail", "gmail_fetch_last_three_messages")
    GMAIL_ADD_LABEL_TO_EMAIL = ("gmail", "gmail_add_label_to_email")
    GMAIL_LIST_LABELS = ("gmail", "gmail_list_labels")
    GMAIL_FETCH_MESSAGE_BY_THREAD_ID = ("gmail", "gmail_fetch_message_by_thread_id")
    GMAIL_REPLY_TO_THREAD = ("gmail", "gmail_reply_to_thread")
    GMAIL_FETCH_EMAILS_WITH_LABEL = ("gmail", "gmail_fetch_emails_with_label")
    TYPEFORM_GET_ABOUT_ME = ("typeform", "typeform_get_about_me")
    LINEAR_CREATE_LINEAR_ISSUE = ("linear", "linear_create_linear_issue")
    LINEAR_LIST_LINEAR_PROJECTS = ("linear", "linear_list_linear_projects")
    LINEAR_LIST_LINEAR_TEAMS = ("linear", "linear_list_linear_teams")
    SLACKBOT_SEND_SLACK_MESSAGE = ("slackbot", "slackbot_send_slack_message")
    SLACKBOT_LIST_SLACK_CHANNELS = ("slackbot", "slackbot_list_slack_channels")
    SLACKBOT_LIST_SLACK_MEMBERS = ("slackbot", "slackbot_list_slack_members")
    SLACKBOT_LIST_SLACK_MESSAGES = ("slackbot", "slackbot_list_slack_messages")
    CLICKUP_CREATE_TASK = ("clickup", "clickup_create_task")
    CLICKUP_GET_TASKS = ("clickup", "clickup_get_tasks")
    CLICKUP_GET_TASK = ("clickup", "clickup_get_task")
    CLICKUP_CREATE_LIST = ("clickup", "clickup_create_list")
    CLICKUP_GET_LISTS = ("clickup", "clickup_get_lists")
    CLICKUP_GET_SPACES = ("clickup", "clickup_get_spaces")
    CLICKUP_CREATE_SPACE = ("clickup", "clickup_create_space")
    CLICKUP_CREATE_FOLDER = ("clickup", "clickup_create_folder")
    CLICKUP_GET_FOLDERS = ("clickup", "clickup_get_folders")
    NOTION_GET_ABOUT_ME = ("notion", "notion_get_about_me")
    NOTION_ADD_NOTION_PAGE_CHILDREN = ("notion", "notion_add_notion_page_children")
    NOTION_ARCHIVE_NOTION_PAGE = ("notion", "notion_archive_notion_page")
    NOTION_CREATE_NOTION_DATABASE = ("notion", "notion_create_notion_database")
    NOTION_CREATE_PAGE_COMMENT = ("notion", "notion_create_page_comment")
    NOTION_CREATE_NOTION_PAGE = ("notion", "notion_create_notion_page")
    NOTION_DELETE_NOTION_PAGE_CHILDREN = ("notion", "notion_delete_notion_page_children")
    NOTION_FETCH_NOTION_COMMENT = ("notion", "notion_fetch_notion_comment")
    NOTION_FETCH_NOTION_DATABASE = ("notion", "notion_fetch_notion_database")
    NOTION_FETCH_NOTION_PAGE = ("notion", "notion_fetch_notion_page")
    NOTION_SEARCH_NOTION_PAGE = ("notion", "notion_search_notion_page")
    NOTION_UPDATE_NOTION_DATABASE = ("notion", "notion_update_notion_database")
    NOTION_FETCH_NOTION_BLOCK = ("notion", "notion_fetch_notion_block")
    NOTION_FETCH_NOTION_CHILD_BLOCK = ("notion", "notion_fetch_notion_child_block")
    SERPAPI_SEARCH = ("serpapi", "serpapi_search")
    GOOGLECALENDAR_CREATE_GOOGLE_EVENT = ("googlecalendar", "googlecalendar_create_google_event")
    GOOGLECALENDAR_REMOVE_ATTENDEE = ("googlecalendar", "googlecalendar_remove_attendee")
    GOOGLECALENDAR_FIND_EVENT = ("googlecalendar", "googlecalendar_find_event")
    GOOGLECALENDAR_DELETE_GOOGLE_EVENT = ("googlecalendar", "googlecalendar_delete_google_event")
    GOOGLECALENDAR_UPDATE_GOOGLE_EVENT = ("googlecalendar", "googlecalendar_update_google_event")
    GOOGLECALENDAR_FIND_FREE_SLOTS = ("googlecalendar", "googlecalendar_find_free_slots")
    GOOGLECALENDAR_DUPLICATE_GOOGLE_CALENDAR = ("googlecalendar", "googlecalendar_duplicate_google_calendar")
    GOOGLECALENDAR_LIST_GOOGLE_CALENDARS = ("googlecalendar", "googlecalendar_list_google_calendars")
    GOOGLECALENDAR_PATCH_GOOGLE_CALENDAR = ("googlecalendar", "googlecalendar_patch_google_calendar")
    GOOGLECALENDAR_QUICK_ADD_GOOGLE_CALENDAR = ("googlecalendar", "googlecalendar_quick_add_google_calendar")

class Trigger(Enum):
    def __init__(self, service, trigger):
        self.service = service
        self.trigger = trigger

    GITHUB_PULL_REQUEST_EVENT = ("github", "github_pull_request_event")
    GITHUB_COMMIT_EVENT = ("github", "github_commit_event")
    SLACK_NEW_MESSAGE = ("slack", "slack_receive_message")
    SLACKBOT_NEW_MESSAGE = ("slackbot", "slackbot_receive_message")
