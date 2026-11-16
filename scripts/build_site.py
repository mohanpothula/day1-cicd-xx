"""Create a deployable static-site artifact using only the Python standard library."""
import json
import os
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
source = ROOT / "site"
target = ROOT / "dist"

if target.exists():
    shutil.rmtree(target)
shutil.copytree(source, target)
(target / "build-info.json").write_text(
    json.dumps({
        "commit": os.getenv("GITHUB_SHA", "local-build"),
        "run": os.getenv("GITHUB_RUN_NUMBER", "local"),
    }, indent=2) + "\n",
    encoding="utf-8",
)
print(f"Build ready: {target}")
print("Files:", ", ".join(sorted(p.name for p in target.iterdir())))
