def calculate_technical_score(
    above_vwap,
    breakout_setup,
    consolidation,
    previous_high_break
):

    score = 0

    if above_vwap:
        score += 5

    if breakout_setup:
        score += 5

    if consolidation:
        score += 5

    if previous_high_break:
        score += 5

    return min(score, 25)

