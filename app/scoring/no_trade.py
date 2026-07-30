def calculate_no_trade_score(
    catalyst,
    spread_percent,
    dollar_volume,
    halt_risk,
    volatility
):

    score = 0


    if catalyst == "NONE":
        score += 20


    if spread_percent > 3:
        score += 20


    if dollar_volume < 1_000_000:
        score += 15


    if halt_risk:
        score += 15


    if volatility == "EXTREME":
        score += 20


    return min(score,100)

