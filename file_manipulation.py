import os
from pathlib import Path

def read_from_file(filename):
    p = Path(filename)
    return p.read_text()

def write_to_file(filename, content):
    p = Path(filename)
    p.write_text(content)

def is_file_exists(filename):
    return Path(filename).exists()

def name_with_platform(filename, platform):
    p = Path(filename)
    return p.with_name(f"{p.stem}-{platform}{p.suffix}").name
