from datetime import datetime

from app.services.scoring_engine import evaluate_stock


def run_scan(stock_list):

    results = []

    for stock in stock_list:

        result = evaluate_stock(stock)

        result["scan_time"] = datetime.utcnow()

        results.append(result)


    results.sort(
        key=lambda x: x["ptr_score"],
        reverse=True
    )

    return results

