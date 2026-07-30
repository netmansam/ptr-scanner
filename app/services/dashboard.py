from sqlalchemy.orm import Session

from app.models.scan_result import ScanResult
from app.models.scan_run import ScanRun


def get_latest_scan(db: Session):

    latest_run = (
        db.query(ScanRun)
        .order_by(ScanRun.id.desc())
        .first()
    )

    if not latest_run:
        return None


    results = (
        db.query(ScanResult)
        .filter(
            ScanResult.scan_run_id == latest_run.id
        )
        .order_by(
            ScanResult.scan_rank
        )
        .limit(10)
        .all()
    )


    return {
        "run": latest_run,
        "results": results
    }

