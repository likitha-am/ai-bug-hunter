from loguru import logger

def setup_logger():
    logger.remove()
    logger.add(
        "bughunter.log",
        format="{time} | {level} | {message}",
        level="INFO"
    )
    return logger
