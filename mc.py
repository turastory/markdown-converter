"""
Markdown Converter - Easily publish markdown posts

Usage:
    mc -p <platform> <src> [<dst>]
    mc -h | --help
    mc --version

Arguments:
    src     Source file.
    dst     Destination file. If not specified, <src>-<platform> is default. File extension is preserved.

Options:
    -h --help        Show this screen.
    --version        Show version.
    -p, --platform   Target platform
"""
from docopt import docopt, DocoptExit
from time import time
from converter import replace
from file_manipulation import *

VERSION = "0.1.0"

def convert(src, dst, platform):
    text = read_from_file(src)
    converted = replace(platform, text)
    write_to_file(dst, converted)

if __name__ == "__main__":
    arguments = docopt(__doc__, version=VERSION)
    
    platform = arguments['<platform>']
    source_file = arguments['<src>']
    dest_file = arguments['<dst>'] or name_with_platform(source_file, platform)
    
    if is_file_exists(dest_file):
        print(f"Destination file already exists: {dest_file}")
        exit(1)
    
    print(f"Generating markdown for [{platform}]...")
    print(f"{source_file} -> {dest_file}")

    start = time()
    convert(source_file, dest_file, platform)
    elapsed = time() - start

    print(f"Conversion completed in {elapsed:.6f}ms")
