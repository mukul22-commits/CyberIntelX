import os

os.system(
    "python collectors/rss_collector.py"
)

os.system(
    "python collectors/cisa_collector.py"
)

os.system(
    "python collectors/cve_collector.py"
)

print("All Intelligence Sources Updated")