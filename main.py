#!/usr/bin/env python3
"""The Dog Ate My Homework: Funniest Excuse.

Writes one line, in the dog's own voice, explaining why the homework
got eaten, to /output/entry.txt. Pure standard library, Python 3.13.
"""

import os

LINE = (
    "Your homework said 'show your work,' so I showed it to my stomach. "
    "It graded the answers delicious and ate the evidence."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
