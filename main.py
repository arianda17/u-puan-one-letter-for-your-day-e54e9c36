ENTRY = "Q"

assert len(ENTRY) == 1 and ENTRY in "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "ENTRY must be a single uppercase letter A-Z"

import os

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as _f:
    _f.write(ENTRY)

print(ENTRY)