"""Structured output schemas. Mirrors sector-reader.yaml's output_schema:
constrains the fields and guards against prompt injection."""
from pydantic import BaseModel, Field


class Fact(BaseModel):
    claim: str = Field(max_length=600)
    source: str = Field(max_length=300)


class SectorReaderOutput(BaseModel):
    sector: str = Field(max_length=64)
    facts: list[Fact] = Field(default_factory=list, max_length=100)


class CompsRow(BaseModel):
    ticker: str = Field(max_length=12)
    ev: float          # enterprise value, $mm
    ebitda: float      # $mm
    price: float       # per share
    eps: float         # per share
    source: str = Field(max_length=300)


class CompsTable(BaseModel):
    rows: list[CompsRow] = Field(default_factory=list, max_length=50)