"""The Long Roast: Lawmakers and the File They Cannot Convert — make.fun entry.

Writes one satirical sentence — roasting lawmakers who would write the
rules for AI, crypto, and the entire internet but cannot convert a file
to PDF — to /output/entry.txt.
"""

import os

ROAST = (
    "The senator who wants to write the rules for AI, crypto, and the "
    "entire internet asked his staff to convert the bill to PDF, so they "
    "printed the PDF, scanned the printout, and emailed him a photo of "
    "the scan."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ROAST)


if __name__ == "__main__":
    main()
