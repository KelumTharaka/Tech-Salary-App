from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    APP_NAME: str = "stats-service"
    APP_HOST: str = "0.0.0.0"
    APP_8PORT: int = 8000
    DATABASE_URL: str = ""
    CORS_ORIGINS: str = "*"

    model_config = SettingsConfigDict(
        env_file="stats_service.env",
        case_sensitive=True,
        extra="ignore",
    )


settings = Settings()