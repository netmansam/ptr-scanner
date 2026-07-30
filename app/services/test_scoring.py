from app.services.scoring_engine import evaluate_stock


test_stock = {

    "ticker": "ABCD",

    "catalyst": "FDA",

    "relative_volume": 18,

    "trend_strength": "STRONG",

    "float_shares": 8500000,

    "spread_percent": 0.5,

    "dollar_volume": 50000000,

    "above_vwap": True,

    "breakout_setup": True,

    "consolidation": True,

    "previous_high_break": True,

    "halt_risk": False,

    "volatility": "NORMAL"

}


print(evaluate_stock(test_stock))

