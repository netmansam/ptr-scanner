from datetime import datetime

from sqlalchemy import (
    Column,
    Integer,
    String,
    Float,
    Boolean,
    DateTime
)

from app.database.connection import Base


class Symbol(Base):

    __tablename__ = "symbols"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    ticker = Column(
        String(10),
        unique=True,
        nullable=False,
        index=True
    )

    company_name = Column(
        String(255)
    )

    exchange = Column(
        String(50)
    )

    sector = Column(
        String(100)
    )

    industry = Column(
        String(100)
    )

    shares_outstanding = Column(
        Float
    )

    float_shares = Column(
        Float
    )

    market_cap = Column(
        Float
    )

    active = Column(
        Boolean,
        default=True
    )

    updated_at = Column(
        DateTime,
        default=datetime.utcnow
    )

