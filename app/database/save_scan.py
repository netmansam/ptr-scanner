from sqlalchemy.orm import Session

from app.models.scan_run import ScanRun
from app.models.scan_result import ScanResult


def save_scan(
    db: Session,
    results,
    market_context=None
):

    if market_context is None:
        market_context = {}


    scan_run = ScanRun(

        market_bias=market_context.get(
            "market_bias",
            "UNKNOWN"
        ),

        spy_direction=market_context.get(
            "spy_direction",
            "UNKNOWN"
        ),

        qqq_direction=market_context.get(
            "qqq_direction",
            "UNKNOWN"
        ),

        vix_level=market_context.get(
            "vix_level",
            None
        ),

        notes=market_context.get(
            "notes",
            None
        )

    )


    db.add(scan_run)

    db.flush()


    for index, result in enumerate(results, start=1):

        scan_result = ScanResult(

            scan_run_id=scan_run.id,

            ticker=result["ticker"],

            scan_rank=index,

            catalyst_score=result["catalyst_score"],

            technical_score=result["technical_score"],

            momentum_score=result["momentum_score"],

            no_trade_score=result["no_trade_score"],

            confidence_score=result["confidence_score"],

            ptr_score=result["ptr_score"],

            passed_scan=result["ptr_score"] >= 70

        )


        db.add(scan_result)


    db.commit()


    return scan_run.id

