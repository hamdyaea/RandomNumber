#!/usr/bin/env python3
# Developer: Hamdy Abou El Anein
# Contact: hamdy.aea@protonmail.com
# SPDX-License-Identifier: GPL-3.0-or-later
"""Tests never write to the repository or contact GitHub."""
from pathlib import Path
import subprocess
import tempfile
import unittest

SCRIPT = Path(__file__).resolve().parents[1] / "random.bsh"


def run(*args):
    return subprocess.run(["bash", str(SCRIPT), *args], text=True,
                          capture_output=True, timeout=10)


class RandomTests(unittest.TestCase):
    def test_preview_does_not_write(self):
        with tempfile.TemporaryDirectory() as tmp:
            output = Path(tmp) / "number"
            result = run("--number", "7", "--output", str(output))
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertFalse(output.exists())
            self.assertIn("Preview only", result.stdout)

    def test_write_is_explicit(self):
        with tempfile.TemporaryDirectory() as tmp:
            output = Path(tmp) / "number"
            result = run("--number", "7", "--write", "--output", str(output))
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertEqual(output.read_text(), "7\n")

    def test_below_threshold_does_not_write(self):
        with tempfile.TemporaryDirectory() as tmp:
            output = Path(tmp) / "number"
            result = run("--number", "2", "--write", "--output", str(output))
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertFalse(output.exists())

    def test_existing_custom_file_is_protected(self):
        with tempfile.TemporaryDirectory() as tmp:
            output = Path(tmp) / "number"
            output.write_text("KEEP")
            result = run("--number", "8", "--write", "--output", str(output))
            self.assertEqual(result.returncode, 2)
            self.assertEqual(output.read_text(), "KEEP")

    def test_publish_cannot_use_test_number(self):
        result = run("--number", "8", "--publish")
        self.assertEqual(result.returncode, 2)

    def test_invalid_number(self):
        result = run("--number", "999")
        self.assertEqual(result.returncode, 2)


if __name__ == "__main__":
    unittest.main()
