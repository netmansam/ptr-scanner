from sqlalchemy import text

from app.database.connection import SessionLocal


def load_trading_universe(limit=600):

    db = SessionLocal()

    try:

        query = text("""
            SELECT
                ticker,
                company_name,
                exchange,
                sector,
                industry,
                shares_outstanding,
                float_shares,
                market_cap,
                avg_dollar_volume
            FROM symbols
            WHERE active = 1
              AND is_etf = 0
              AND market_cap BETWEEN 50000000 AND 5000000000
              AND avg_dollar_volume >= 2000000
            ORDER BY
                avg_dollar_volume DESC
            LIMIT :limit
        """)

        rows = db.execute(
            query,
            {
                "limit": limit
            }
        ).mappings().all()


        stocks = []


        for row in rows:

            stocks.append({

                "ticker": row["ticker"],

                "company_name": row["company_name"],

                "sector": row["sector"],

                "industry": row["industry"],

                "float_shares": row["float_shares"] or 0,

                "market_cap": row["market_cap"] or 0,

                "dollar_volume": row["avg_dollar_volume"] or 0,

                # Technical inputs populated later
                "catalyst": "NONE",

                "relative_volume": 0,

                "trend_strength": "WEAK",

                "above_vwap": False,

                "breakout_setup": False,

                "consolidation": False,

                "previous_high_break": False,

                "spread_percent": 99,

                "halt_risk": False,

                "volatility": "NORMAL"
            })


        return stocks


    finally:

        db.close()
