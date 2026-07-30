from datetime import datetime

from sqlalchemy import (
    Column,
    Integer,
    String,
    Date,
    DateTime,
    JSON
)

from app.database.connection import Base


class MarketDataCache(Base):

    __tablename__ = "market_data_cache"


    id = Column(
        Integer,
        primary_key=True
    )


    ticker = Column(
        String(10),
        nullable=False,
        index=True
    )


    data_type = Column(
        String(50),
        nullable=False
    )


    timeframe = Column(
        String(20)
    )


    data_date = Column(
        Date
    )


    json_data = Column(
        JSON,
        nullable=False
    )


    source = Column(
        String(50),
        default="MASSIVE"
    )


    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )


    updated_at = Column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow
    )
