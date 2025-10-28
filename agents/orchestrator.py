from agents.scanner_agent import ScannerAgent
from agents.analyzer_agent import AnalyzerAgent
from agents.reporter_agent import ReporterAgent
from utils.logger import setup_logger
import os

class Orchestrator:
    def __init__(self):
        self.logger = setup_logger()
        self.scanner = ScannerAgent()
        self.analyzer = AnalyzerAgent()
        self.reporter = ReporterAgent()

    def run_all(self, repo_path="."):
        if not os.path.exists(repo_path):
            self.logger.error(f"❌ The path '{repo_path}' does not exist!")
            return

        self.logger.info(f"📁 Running AI Bug Hunter on: {repo_path}")

        # if it's a single file, analyze just that one
        if os.path.isfile(repo_path):
            files = [repo_path]
        else:
            files = self.scanner.scan_repo(repo_path)

        results = self.analyzer.analyze(files)

        for bug in results:
            self.reporter.report_bug(bug["summary"], bug["description"])
