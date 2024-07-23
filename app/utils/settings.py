from pydantic_settings import BaseSettings


class AppSettings(BaseSettings):
    TELEGRAM_BOT_TOKEN: str
    WEB_APP_URL: str
    CHANNEL_URL: str

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
