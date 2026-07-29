from sqlalchemy import text

from app.database.connection import engine


indexes = [

    {
        "name": "idx_scan_results_ticker",
        "table": "scan_results",
        "sql": """
            CREATE INDEX idx_scan_results_ticker
            ON scan_results (ticker)
        """
    },

    {
        "name": "idx_scan_results_scan_rank",
        "table": "scan_results",
        "sql": """
            CREATE INDEX idx_scan_results_scan_rank
            ON scan_results (scan_rank)
        """
    },

    {
        "name": "idx_scan_results_confidence",
        "table": "scan_results",
        "sql": """
            CREATE INDEX idx_scan_results_confidence
            ON scan_results (confidence_score)
        """
    },

    {
        "name": "idx_scan_results_no_trade",
        "table": "scan_results",
        "sql": """
            CREATE INDEX idx_scan_results_no_trade
            ON scan_results (no_trade_score)
        """
    },

    {
        "name": "idx_scan_results_scan_run",
        "table": "scan_results",
        "sql": """
            CREATE INDEX idx_scan_results_scan_run
            ON scan_results (scan_run_id)
        """
    },

    {
        "name": "idx_symbols_ticker",
        "table": "symbols",
        "sql": """
            CREATE INDEX idx_symbols_ticker
            ON symbols (ticker)
        """
    },

]


def index_exists(connection, index_name, table_name):

    query = text(
        """
        SELECT COUNT(*)
        FROM information_schema.statistics
        WHERE table_schema = DATABASE()
        AND table_name = :table_name
        AND index_name = :index_name
        """
    )

    result = connection.execute(
        query,
        {
            "table_name": table_name,
            "index_name": index_name
        }
    )

    return result.scalar() > 0


def add_indexes():

    print("Adding PTR database indexes...")

    with engine.connect() as connection:

        for index in indexes:

            if index_exists(
                connection,
                index["name"],
                index["table"]
            ):

                print(
                    f"Skipping existing index: {index['name']}"
                )

            else:

                print(
                    f"Creating index: {index['name']}"
                )

                connection.execute(
                    text(index["sql"])
                )

                connection.commit()

    print("PTR database indexes completed.")


if __name__ == "__main__":
    add_indexes()

