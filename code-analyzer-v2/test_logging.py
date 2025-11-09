#!/usr/bin/env python3
"""
Test script to verify UTF-8 logging works correctly
Run this to test before running main.py
"""

import sys
import logging

class Utf8StreamHandler(logging.StreamHandler):
    """Custom handler that properly handles UTF-8/emoji output on Windows."""

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


# Initialize logging
logger = setup_logging(logging.INFO)

print()
print("="*80)
print("TESTING UTF-8 LOGGING WITH EMOJIS")
print("="*80)
print()

# Test various emojis and unicode characters
logger.info("✓ Testing checkmark emoji")
logger.info("● Testing bullet point")
logger.info("○ Testing circle")
logger.info("🚀 Testing rocket emoji")
logger.info("🔍 Testing magnifying glass")
logger.info("📊 Testing chart emoji")
logger.info("🎨 Testing palette emoji")
logger.info("✅ Testing check mark button")
logger.info("❌ Testing cross mark")
logger.info("⚠️ Testing warning emoji")
logger.info("📁 Testing folder emoji")
logger.info("🐍 Testing snake emoji (Python)")

print()
logger.debug("DEBUG message test")
logger.warning("WARNING message test")
logger.error("ERROR message test")

print()
print("="*80)
print("✓ TEST COMPLETE!")
print("="*80)
print()
print("Check results:")
print("  1. All emojis should be visible above")
print("  2. Check 'test_logging.log' file for file output")
print("  3. If all looks good, run: python main.py -p ./examples/sample_project --all")
print()
