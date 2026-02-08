# import os
# from pydantic_settings import BaseSettings, SettingsConfigDict

# _model_config = SettingsConfigDict(
#     env_file=".env",
#     env_ignore_empty=True,
#     extra="ignore",
# )


# class LLMSettings(BaseSettings):
#     OLLAMA_API_KEY: str = os.getenv("OLLAMA_API_KEY") or ""
#     MODEL_NAME: str = os.getenv("MODEL_NAME") or ""

#     model_config = _model_config


# llm_settings = LLMSettings()
