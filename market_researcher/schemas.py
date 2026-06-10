"""Structured output schemas. Mirrors sector-reader.yaml's output_schema:
it constrains the fields and guards against prompt injection."""
from pydantic import BaseModel, Field


class Fact(BaseModel):
    claim: str = Field(max_length=256)
    source: str = Field(max_length=128)


class SectorReaderOutput(BaseModel):
    sector: str = Field(max_length=64)
    facts: list[Fact] = Field(default_factory=list, max_length=100)