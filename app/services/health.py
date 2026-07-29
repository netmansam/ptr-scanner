from sqlalchemy import text

from app.database.connection import engine


def database_health():

    try:
        with engine.connect() as connection:

            result = connection.execute(
                text("SELECT VERSION();")
            )

            version = result.scalar()

        return {
            "database": "online",
            "mysql_version": version
        }

    except Exception as e:

        return {
            "database": "offline",
            "error": str(e)
        }

