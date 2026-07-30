from app.scoring.catalyst import calculate_catalyst_score
from app.scoring.momentum import calculate_momentum_score
from app.scoring.technical import calculate_technical_score
from app.scoring.liquidity import calculate_liquidity_score
from app.scoring.no_trade import calculate_no_trade_score
from app.scoring.confidence import calculate_confidence_score



def evaluate_stock(stock):


    catalyst_score = calculate_catalyst_score(
        stock.get("catalyst","NONE")
    )


    momentum_score = calculate_momentum_score(
        stock.get("relative_volume",0),
        stock.get("trend_strength","WEAK")
    )


    technical_score = calculate_technical_score(
        stock.get("above_vwap",False),
        stock.get("breakout_setup",False),
        stock.get("consolidation",False),
        stock.get("previous_high_break",False)
    )


    liquidity_score = calculate_liquidity_score(
        stock.get("float_shares",999999999),
        stock.get("spread_percent",99),
        stock.get("dollar_volume",0)
    )


    confidence_score = calculate_confidence_score(
        catalyst_score,
        technical_score,
        momentum_score,
        liquidity_score
    )


    no_trade_score = calculate_no_trade_score(
        stock.get("catalyst","NONE"),
        stock.get("spread_percent",99),
        stock.get("dollar_volume",0),
        stock.get("halt_risk",False),
        stock.get("volatility","NORMAL")
    )


    ptr_score = confidence_score - no_trade_score


    return {

        "ticker": stock.get("ticker"),

        "catalyst_score": catalyst_score,

        "technical_score": technical_score,

        "momentum_score": momentum_score,

        "liquidity_score": liquidity_score,

        "confidence_score": confidence_score,

        "no_trade_score": no_trade_score,

        "ptr_score": ptr_score

    }

