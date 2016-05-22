# !/usr/bin/env python


from os.path import dirname, join


# ========================================

# Configuration variables to be used elsewhere in the program

# ========================================


# how high, as a fraction of overall divider height, should the tabs be?
TAB_HEIGHT_PROPORTION = 0.25

# Where are output dxf files stored?
DXF_DEST_DIR = join(dirname(dirname(__file__)), "dxf_files")
