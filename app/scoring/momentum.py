def calculate_momentum_score(
    relative_volume,
    trend_strength
):

    score = 0

    if relative_volume >= 10:
        score += 10

    elif relative_volume >= 5:
        score += 5


    if trend_strength == "STRONG":
        score += 10

    elif trend_strength == "MODERATE":
        score += 5


    return min(score,25)
