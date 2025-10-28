from utils.logger import setup_logger
import re

class AnalyzerAgent:
    def __init__(self):
        self.logger = setup_logger()

    def analyze(self, files):
        self.logger.info("🤖 Analyzing files for possible bugs...")
        bugs = []

        for file in files:
            with open(file, "r", encoding="utf-8") as f:
                lines = f.readlines()

            for i, line in enumerate(lines, start=1):
                # Debug print statements
                if "print(" in line:
                    bugs.append({
                        "summary": f"Debug print in {file}",
                        "description": f"Line {i}: `{line.strip()}` → Remove debug prints before production."
                    })

                # TODO comments
                if "TODO" in line:
                    bugs.append({
                        "summary": f"TODO found in {file}",
                        "description": f"Line {i}: `{line.strip()}` → Complete or remove this TODO."
                    })

                # Use of eval()
                if "eval(" in line:
                    bugs.append({
                        "summary": f"Unsafe eval() in {file}",
                        "description": f"Line {i}: `{line.strip()}` → Using eval() can be unsafe. Avoid it."
                    })

                # Hardcoded passwords
                if re.search(r'password\s*=\s*["\'].*["\']', line, re.IGNORECASE):
                    bugs.append({
                        "summary": f"Hardcoded password in {file}",
                        "description": f"Line {i}: `{line.strip()}` → Avoid storing passwords in code."
                    })

                # Empty exception handlers
                if re.search(r'except\s*:\s*pass', line):
                    bugs.append({
                        "summary": f"Empty exception handler in {file}",
                        "description": f"Line {i}: `{line.strip()}` → Handle errors explicitly, not with 'pass'."
                    })

            if bugs:
                self.logger.info(f"🪲 Found {len(bugs)} issues in {file}")

        if not bugs:
            self.logger.success("✨ No issues found! Code looks clean.")
        return bugs

