"""Tests for ProjectScanner"""
import pytest
from pathlib import Path
from src.scanner import ProjectScanner

def test_scanner_initialization():
    scanner = ProjectScanner(Path('.'))
    assert scanner.root_path == Path('.')
