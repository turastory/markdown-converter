import os
import pathlib
from file_manipulation import *

def test_read_from_file(tmp_path):
    name = os.path.join(tmp_path, "test.txt")
    content = "Content"
    p = pathlib.Path(name)
    p.write_text(content)
    assert read_from_file(name) == content

def test_write_to_file(tmp_path):
    name = os.path.join(tmp_path, "test.txt")
    content = "Content"
    p = pathlib.Path(name)
    write_to_file(name, content)
    assert p.read_text() == content

def test_is_file_exists(tmp_path):
    a_name = os.path.join(tmp_path, "a.txt")
    ap = pathlib.Path(a_name)
    ap.write_text("helll world")

    b_name = os.path.join(tmp_path, "b.txt")
    bp = pathlib.Path(b_name)
    bp.write_text("helll world")
    
    else_name = os.path.join(tmp_path, "else.txt")
    
    assert is_file_exists(a_name) == True
    assert is_file_exists(b_name) == True
    assert is_file_exists(else_name) == False

def test_name_with_platform(tmp_path):
    name = os.path.join(tmp_path, "test.txt")
    dst = name_with_platform(name, "velog")
    assert dst == "test-velog.txt"
