def calculate_liquidity_score(
    float_shares,
    spread_percent,
    dollar_volume
):

    score = 0


    if float_shares < 10_000_000:
        score += 10

    elif float_shares < 20_000_000:
        score += 5


    if spread_percent <= 1:
        score += 5


    if dollar_volume >= 5_000_000:
        score += 5


    if dollar_volume >= 25_000_000:
        score += 5


    return min(score,25)

