from configparser import ConfigParser
import os

class Config:
    def __init__(self, config_file="./src/langgraph/ui/uiconfigfile.ini"):
        self.config = ConfigParser()
        loaded = self.config.read(config_file)

        if not loaded:
            print(f"⚠️ Config file NOT found: {os.path.abspath(config_file)}")
        else:
            print(f"✅ Config file loaded: {os.path.abspath(config_file)}")

    def get_llm_options(self):
        return self.config["DEFAULT"].get("LLM_OPTIONS", "OpenAI, Groq").split(", ")

    def get_usecase_options(self):
        return self.config["DEFAULT"].get("USECASE_OPTIONS", "Chatbot, Summarizer").split(", ")

    def get_groq_model_options(self):
        return self.config["DEFAULT"].get("GROQ_MODEL_OPTIONS", "mixtral-8x7b, llama2-70b").split(", ")

    def get_page_title(self):
        return self.config["DEFAULT"].get("PAGE_TITLE", "LangGraph Agentic AI")
