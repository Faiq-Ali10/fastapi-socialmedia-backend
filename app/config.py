from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    ALGORITHM : str = "any"
    ACCESS_TOKEN_EXPIRE_MINUTES : int = 100
    DATABASE_USERNAME : str = "any" 
    DATABASE_PASSWORD : str = "any" 
    DATABASE_HOSTNAME : str = "any" 
    DATABASE_PORT : int = 0
    DATABASE_NAME : str = "any" 
    TOKEN_BYTE : int = 0
    SECRET_KEY : str = "any"
    DATABASE_NAME_Test : str = "any"

    model_config: SettingsConfigDict = {
        "env_file": ".env",
        "env_file_encoding": "utf-8",
    }
        
settings = Settings()    