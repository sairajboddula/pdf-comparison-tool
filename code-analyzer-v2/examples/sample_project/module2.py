"""Analysis Module"""
from module1 import DataProcessor

class Analyzer:
    """Analyze data."""

    def __init__(self):
        self.results = {}

    def analyze(self, data):
        """Run analysis."""
        return {'count': len(data)}
