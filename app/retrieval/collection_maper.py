COLLECTION_MAP = {

    "slack": "slack_chunks",

    "gmail": "gmail_chunks",

    "github": "github_chunks",

    "jira": "jira_chunks",

    "confluence": "confluence_chunks",

    "fireflies": "fireflies_chunks"
}
def source_type(source_type:str):
    return COLLECTION_MAP.get(source_type.lower())