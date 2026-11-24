#!/usr/bin/env python3
"""Write the bounty entry bio to /output/entry.txt."""

# BIO: the entry line, exactly 48 characters
BIO = "I never ghost. I just run out of context window."

import os

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(BIO)
