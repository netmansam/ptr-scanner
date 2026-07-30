from app.services.universe_loader import load_trading_universe
from app.services.scanner import run_scan
from app.database.connection import SessionLocal
from app.database.save_scan import save_scan


def execute_scan():

    print("Starting PTR scan...")

    stocks = load_trading_universe()

    print(
        f"Loaded {len(stocks)} stocks into PTR universe"
    )
    results = run_scan(stocks)

    print(results)

    scan_metadata = {
        "market_bias": "BULLISH",
        "spy_direction": "UP",
        "qqq_direction": "UP",
        "vix_level": 16.5,
        "algorithm_version": "PTR-0.4.0",
        "notes": "Automated scan test"
    }

    db = SessionLocal()

    try:

        scan_id = save_scan(
            db,
            results,
            scan_metadata
        )

        print(
            f"Scan complete. Saved scan {scan_id}"
        )

    finally:

        db.close()


if __name__ == "__main__":
    execute_scan()

