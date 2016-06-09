# !/usr/bin/env python


from os.path import dirname, join


# ========================================

# Configuration variables to be used elsewhere in the program

# ========================================


# Where are output dxf files stored?
DXF_DEST_DIR = join(dirname(dirname(__file__)), "dxf_files")


# LENGTH (IN CHARACTERS) OF GENERATED DIVIDER NAMES
GENERATED_DIVIDER_NAME_LENGTH = 5