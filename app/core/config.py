import os
from dotenv import load_dotenv

load_dotenv()


class Settings:
    APP_NAME = os.getenv(
        "APP_NAME",
        "PTR Scanner"
    )

    APP_VERSION = os.getenv(
        "APP_VERSION",
        "0.3.0"
    )

    ENVIRONMENT = os.getenv(
        "ENVIRONMENT",
        "development"
    )

    DATABASE_HOST = os.getenv(
        "DATABASE_HOST",
        "localhost"
    )

    DATABASE_PORT = os.getenv(
        "DATABASE_PORT",
        "3306"
    )

    DATABASE_NAME = os.getenv(
        "DATABASE_NAME"
    )

    DATABASE_USER = os.getenv(
        "DATABASE_USER"
    )

    DATABASE_PASSWORD = os.getenv(
        "DATABASE_PASSWORD"
    )

    TIMEZONE = os.getenv(
        "TIMEZONE",
        "America/Denver"
    )

    @property
    def database_url(self):
        return (
            "mysql+pymysql://"
            f"{self.DATABASE_USER}:"
            f"{self.DATABASE_PASSWORD}@"
            f"{self.DATABASE_HOST}:"
            f"{self.DATABASE_PORT}/"
            f"{self.DATABASE_NAME}"
        )


settings = Settings()

