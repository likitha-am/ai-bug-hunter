from utils.jira_api import create_jira_issue
from utils.logger import setup_logger

class ReporterAgent:
    def __init__(self):
        self.logger = setup_logger()

    def report_bug(self, summary, description):
        self.logger.info(f"📢 Reporting bug: {summary}")
        status = create_jira_issue(summary, description)
        if status == 201:
            self.logger.success("✅ Bug successfully logged in Jira!")
        elif status == "MOCK_MODE":
            self.logger.warning("🧪 Running in mock mode (no Jira API keys found).")
        else:
            self.logger.error("❌ Failed to report bug.")
