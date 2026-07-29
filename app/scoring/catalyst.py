def calculate_catalyst_score(catalyst_type):

    scores = {
        "FDA": 25,
        "CONTRACT": 20,
        "EARNINGS": 20,
        "UPGRADE": 15,
        "PARTNERSHIP": 10,
        "NONE": 0
    }

    return scores.get(
        catalyst_type.upper(),
        0
    )
