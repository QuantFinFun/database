"""Class defining the distribution table"""

__author__ = "Mohd Sadiq"
__version__ = "v0.1"
__module__ = "distribution_table"

import uuid
from datetime import datetime
from typing import List

from sqlalchemy import ARRAY, DateTime, Float, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column

from tables import Base
from utils import get_attributes


class DistributionDataset(Base):
    """Definition of the distribution table"""

    __tablename__ = "distribution_table"

    unique_id: Mapped[uuid.UUID] = mapped_column(UUID, primary_key=True)
    date: Mapped[datetime] = mapped_column(DateTime)
    assets: Mapped[List[str]] = mapped_column(ARRAY(String))
    distribution: Mapped[List[float]] = mapped_column(ARRAY(Float))

    def __repr__(self) -> str:
        return get_attributes(self)

    def __str__(self) -> str:
        return get_attributes(self)
