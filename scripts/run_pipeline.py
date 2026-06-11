"""
Master script to execute Bluestock MF pipeline
"""

import subprocess

print("Starting Bluestock Mutual Fund Pipeline...")

scripts = [
    "scripts/data_ingestion.py",
    "scripts/etl_pipeline.py",
    "scripts/live_nav_fetch.py"
]

for script in scripts:
    print(f"Running {script}")
    subprocess.run(["python", script])

print("Pipeline executed successfully!")