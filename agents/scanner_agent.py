from utils.git_utils import get_python_files
from utils.logger import setup_logger

class ScannerAgent:
    def __init__(self):
        self.logger = setup_logger()

    def scan_repo(self, repo_path="."):
        self.logger.info("🔍 Scanning repository for Python files...")
        files = get_python_files(repo_path)
        # Skip venv and other irrelevant folders
        files = [f for f in files if ".venv" not in f and "__pycache__" not in f]
        self.logger.info(f"📁 Found {len(files)} Python files in your project.")
        return files


