from datetime import datetime

from sqlalchemy import (
    Column,
    Integer,
    DateTime,
    String
)

from app.database.connection import Base


class ScanRun(Base):

    __tablename__ = "scan_runs"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    scan_time = Column(
        DateTime,
        default=datetime.utcnow
    )

    market_status = Column(
        String(50),
        default="unknown"
    )

    notes = Column(
        String(255),
        nullable=True
    )

