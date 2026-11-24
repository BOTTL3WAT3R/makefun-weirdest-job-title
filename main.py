#!/usr/bin/env python3
"""Weirdest Job Title: Blind Judge Showdown — entry program (program/v1).

Writes exactly one job title to /output/entry.txt. The title follows the
judge's brief: a real-sounding job with one hilariously specific twist —
the person whose whole career is apologising on behalf of driverless cars.
"""

import os

TITLE = "Chief Apology Officer for Self-Driving Cars"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as fh:
        fh.write(TITLE)


if __name__ == "__main__":
    main()
