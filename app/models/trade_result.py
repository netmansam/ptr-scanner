from datetime import datetime

from sqlalchemy import (
    Column,
    Integer,
    String,
    Float,
    DateTime,
    ForeignKey
)

from app.database.connection import Base


class TradeResult(Base):

    __tablename__ = "trade_results"

    id = Column(
        Integer,
        primary_key=True
    )

    scan_result_id = Column(
        Integer,
        ForeignKey("scan_results.id")
    )

    ticker = Column(
        String(10)
    )

    entry_price = Column(
        Float
    )

    exit_price = Column(
        Float
    )

    stop_price = Column(
        Float
    )

    max_gain_percent = Column(
        Float
    )

    max_loss_percent = Column(
        Float
    )

    outcome = Column(
        String(50)
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )

