from datetime import datetime

from sqlalchemy import (
    Column,
    Integer,
    String,
    Float,
    DateTime,
    Boolean,
    ForeignKey
)

from app.database.connection import Base


class ScanResult(Base):

    __tablename__ = "scan_results"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    scan_run_id = Column(
        Integer,
        ForeignKey("scan_runs.id"),
        nullable=False
    )

    ticker = Column(
        String(10),
        nullable=False,
        index=True
    )

    scan_rank = Column(
        Integer,
        index=True
    )

    price = Column(
        Float
    )

    float_shares = Column(
        Float
    )

    market_cap = Column(
        Float
    )

    premarket_volume = Column(
        Integer
    )

    relative_volume = Column(
        Float
    )

    catalyst_score = Column(
        Float
    )

    technical_score = Column(
        Float
    )

    momentum_score = Column(
        Float
    )

    no_trade_score = Column(
        Float
    )

    confidence_score = Column(
        Float
    )

    ptr_score = Column(
        Float
    )

    breakout_level = Column(
        Float
    )

    stop_level = Column(
        Float
    )

    passed_scan = Column(
        Boolean,
        default=False
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )
