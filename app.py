from agents.orchestrator import Orchestrator
from utils.logger import setup_logger

def main():
    logger = setup_logger()
    logger.info("🚀 Starting AI Bug Hunter...")

    # ask for folder path
    repo_path = input("Enter the folder path you want to scan for bugs: ").strip()

    try:
        orchestrator = Orchestrator()
        orchestrator.run_all(repo_path)
        logger.success("✅ Bug hunting process completed successfully!")
    except Exception as e:
        logger.error(f"❌ Error during bug hunting: {e}")

if __name__ == "__main__":
    main()
