"""Data Processing Module"""
from pathlib import Path

class DataProcessor:
    """Process data files."""

    def __init__(self, path: str):
        self.path = Path(path)

    def load(self):
        """Load data."""
        return []

    def process(self, data):
        """Process data."""
        return [x.upper() for x in data]
