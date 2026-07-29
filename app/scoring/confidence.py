def calculate_confidence_score(
    catalyst_score,
    technical_score,
    momentum_score,
    liquidity_score
):

    return min(
        catalyst_score +
        technical_score +
        momentum_score +
        liquidity_score,
        100
    )
