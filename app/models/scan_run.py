from datetime import datetime

from sqlalchemy import (
    Column,
    Integer,
    String,
    Float,
    DateTime
)

from app.database.connection import Base


class ScanRun(Base):

    __tablename__ = "scan_runs"

    id = Column(
        Integer,
        primary_key=True
    )

    scan_time = Column(
        DateTime,
        default=datetime.utcnow
    )

    market_bias = Column(
        String(50)
    )

    spy_direction = Column(
        String(50)
    )

    qqq_direction = Column(
        String(50)
    )

    vix_level = Column(
        Float
    )

    algorithm_version = Column(
        String(50),
        default="PTR-0.4.0"
    )

    notes = Column(
        String(255)
    )

