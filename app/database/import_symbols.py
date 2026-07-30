import csv
from datetime import datetime

from app.database.connection import SessionLocal
from app.models.symbol import Symbol


CSV_FILE = "symbols.csv"


def import_symbols():

    db = SessionLocal()

    count = 0

    try:

        with open(CSV_FILE, newline="") as file:

            reader = csv.DictReader(file)

            for row in reader:

                symbol = Symbol(
                    ticker=row["ticker"],
                    company_name=row.get("company_name"),
                    exchange=row.get("exchange"),
                    sector=row.get("sector"),
                    industry=row.get("industry"),
                    shares_outstanding=float(row.get("shares_outstanding") or 0),
                    float_shares=float(row.get("float_shares") or 0),
                    market_cap=float(row.get("market_cap") or 0),
                    active=True,
                    updated_at=datetime.utcnow()
                )

                db.merge(symbol)

                count += 1

        db.commit()

        print(f"Imported {count} symbols")

    finally:

        db.close()


if __name__ == "__main__":
    import_symbols()
