import os
import requests
from requests.auth import HTTPBasicAuth

JIRA_URL = os.getenv("JIRA_URL")
EMAIL = os.getenv("JIRA_EMAIL")
API_TOKEN = os.getenv("JIRA_TOKEN")
PROJECT_KEY = os.getenv("JIRA_PROJECT", "BUGHUNT")

def create_jira_issue(summary, description):
    if not all([JIRA_URL, EMAIL, API_TOKEN]):
        print(f"[JIRA MOCK] Would create issue: {summary} - {description}")
        return "MOCK_MODE"

    url = f"{JIRA_URL}/rest/api/3/issue"
    headers = {"Content-Type": "application/json"}
    data = {
        "fields": {
            "project": {"key": PROJECT_KEY},
            "summary": summary,
            "description": description,
            "issuetype": {"name": "Bug"}
        }
    }
    auth = HTTPBasicAuth(EMAIL, API_TOKEN)
    response = requests.post(url, json=data, headers=headers, auth=auth)

    if response.status_code == 201:
        print(f"✅ Created Jira issue: {summary}")
    else:
        print(f"❌ Failed to create issue: {response.status_code} - {response.text}")

    return response.status_code

