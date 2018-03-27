"""Database models for PUDL tables for ."""

from sqlalchemy import Column, ForeignKey, Integer, String, Float
from sqlalchemy import Boolean, Integer, String, Float, Numeric, Date
from sqlalchemy import ForeignKeyConstraint
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

PUDLBase = declarative_base()


class PlantEntityEIA(PUDLBase):
    """
    An EIA Plant, listed in 923 or 860.

    A compilation of all EIA plant ids and static info.
    """

    __tablename__ = 'plants_entity_eia'
    plant_id_eia = Column(Integer, primary_key=True, nullable=False)
    # TODO: Add static plant info


class GeneratorEntityEIA(PUDLBase):
    """
    An EIA Plant, listed in 923 or 860.

    A compilation of all EIA plant ids and static info.
    """

    __tablename__ = 'generators_entity_eia'
    plant_id_eia = Column(Integer,
                          ForeignKey('plants_entity_eia.plant_id_eia'),
                          primary_key=True, nullable=False)
    generator_id = Column(String, primary_key=True, nullable=False)
    # TODO: Add static plant info
