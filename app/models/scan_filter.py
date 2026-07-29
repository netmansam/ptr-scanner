from datetime import datetime

from sqlalchemy import (
    Column,
    Integer,
    Float,
    String,
    ForeignKey,
    DateTime
)

from app.database.connection import Base


class ScanFilter(Base):

    __tablename__ = "scan_filters"

    id = Column(
        Integer,
        primary_key=True
    )

    scan_run_id = Column(
        Integer,
        ForeignKey("scan_runs.id"),
        nullable=False
    )

    minimum_price = Column(
        Float
    )

    maximum_price = Column(
        Float
    )

    maximum_float = Column(
        Float
    )

    minimum_relative_volume = Column(
        Float
    )

    algorithm_version = Column(
        String(50)
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )

