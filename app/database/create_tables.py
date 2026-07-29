from app.database.connection import (
    engine,
    Base
)

from app.models import ScanRun


print("Creating PTR database tables...")

Base.metadata.create_all(
    bind=engine
)

print("PTR database tables created.")

