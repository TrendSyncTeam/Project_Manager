import os
from dotenv import load_dotenv , find_dotenv

def load_env():
    _ = load_dotenv(find_dotenv())

def get_openai_api_key():
    load_env()
    openai_api_key = "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"
    # os.getenv("OPENAI_API_KEY")
    return openai_key_key