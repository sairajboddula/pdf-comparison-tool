"""
Utility Functions - Enhanced Implementation
"""

import logging
import sys
from pathlib import Path
from typing import Optional
from datetime import datetime


# def setup_logging(level: int = logging.INFO):
#     """Configure comprehensive logging."""
#     log_format = '%(asctime)s | %(levelname)-8s | %(name)s | %(message)s'
#     date_format = '%Y-%m-%d %H:%M:%S'

#     formatter = logging.Formatter(fmt=log_format, datefmt=date_format)

#     # Console handler
#     console_handler = logging.StreamHandler(sys.stdout)
#     console_handler.setLevel(level)
#     console_handler.setFormatter(formatter)

#     # File handler
#     file_handler = logging.FileHandler('code_analyzer.log', mode='a')
#     file_handler.setLevel(logging.DEBUG)
#     file_handler.setFormatter(formatter)

#     # Configure root logger
#     root_logger = logging.getLogger()
#     root_logger.setLevel(logging.DEBUG)
#     # Clear existing handlers
#     root_logger.handlers = []
#     root_logger.addHandler(console_handler)
#     root_logger.addHandler(file_handler)

class Utf8StreamHandler(logging.StreamHandler):
    def emit(self, record):
        try:
            msg = self.format(record)
            stream = self.stream

            # For Windows console (cp1252), use buffer and encode to UTF-8
            if hasattr(stream, 'buffer'):
                # Write directly to buffer with UTF-8 encoding
                stream.buffer.write((msg + self.terminator).encode('utf-8', errors='replace'))
                stream.buffer.flush()
            else:
                # Fallback for non-buffered streams
                stream.write(msg + self.terminator)
                stream.flush()

        except Exception as e:
            self.handleError(record)

def setup_logging(level: int = logging.INFO):
    """Configure comprehensive logging with UTF-8 emoji support."""

    # Create formatter
    formatter = logging.Formatter(
        fmt='%(asctime)s | %(levelname)-8s | %(name)s | %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )

    # Create console handler with UTF-8 support
    console_handler = Utf8StreamHandler(sys.stdout)
    console_handler.setLevel(level)
    console_handler.setFormatter(formatter)

    # Create file handler with UTF-8 encoding
    file_handler = logging.FileHandler(
        'test_logging.log',
        mode='w',
        encoding='utf-8'
    )
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)

    # Configure root logger
    root_logger = logging.getLogger()
    root_logger.setLevel(logging.DEBUG)

    # Clear any existing handlers
    root_logger.handlers = []

    # Add handlers
    root_logger.addHandler(console_handler)
    root_logger.addHandler(file_handler)

    return root_logger

logger = setup_logging(logging.INFO)


def print_banner():
    """Print application banner."""
    banner = """
╔═══════════════════════════════════════════════════════════════════════════════╗
║                                                                               ║
║                   🚀 AI-POWERED CODE ANALYZER v2.0 🚀                        ║
║                                                                               ║
║                 Comprehensive Project Structure Analysis                      ║
║                                                                               ║
╚═══════════════════════════════════════════════════════════════════════════════╝
    """
    print(banner)


def validate_path(path: Path) -> bool:
    """Validate that a path exists and is accessible."""
    if not path.exists():
        logging.error(f"Path does not exist: {path}")
        return False

    if not path.is_dir():
        logging.error(f"Path is not a directory: {path}")
        return False

    return True


def get_color_for_node_type(node_type: str, theme: str = 'default') -> str:
    """Get color for different node types based on theme."""
    themes = {
        'default': {
            'directory': '#4A90E2',
            'file': '#7ED321',
            'class': '#F5A623',
            'function': '#BD10E0',
            'module': '#50E3C2'
        },
        'dark': {
            'directory': '#2C3E50',
            'file': '#34495E',
            'class': '#E74C3C',
            'function': '#9B59B6',
            'module': '#1ABC9C'
        },
        'colorful': {
            'directory': '#FF6B6B',
            'file': '#4ECDC4',
            'class': '#FFE66D',
            'function': '#A8E6CF',
            'module': '#FF8B94'
        },
        'minimal': {
            'directory': '#333333',
            'file': '#666666',
            'class': '#999999',
            'function': '#BBBBBB',
            'module': '#555555'
        }
    }
    return themes.get(theme, themes['default']).get(node_type, '#CCCCCC')


def format_size(bytes_size: int) -> str:
    """Format file size in human-readable format."""
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if bytes_size < 1024:
            return f"{bytes_size} {unit}"
        bytes_size //= 1024
    return f"{bytes_size} PB"


def get_file_type_icon(extension: str) -> str:
    """Get icon representation for file type."""
    icon_map = {
        '.py': '🐍',
        '.js': '📜',
        '.java': '☕',
        '.cpp': '⚙️',
        '.c': '⚙️',
        '.h': '📋',
        '.html': '🌐',
        '.css': '🎨',
        '.json': '📋',
        '.xml': '📋',
        '.md': '📝',
        '.txt': '📄',
        '.yml': '⚙️',
        '.yaml': '⚙️',
        '.sh': '🔧',
        '.sql': '🗄️',
        '.db': '🗄️',
        '.png': '🖼️',
        '.jpg': '🖼️',
        '.gif': '🖼️',
        '.svg': '🖼️'
    }
    return icon_map.get(extension.lower(), '📄')
