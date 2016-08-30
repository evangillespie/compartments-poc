# !/usr/bin/env python


from os.path import dirname, join


# ========================================

# Configuration variables to be used elsewhere in the program

# ========================================


# NAMES OF THE BASE AND OUTER EDGE DIVIDERS
OUTER_DIVIDER_NAME_BASE = "BASE"
OUTER_DIVIDER_NAME_LEFT = "LFT"
OUTER_DIVIDER_NAME_TOP = "TOP"
OUTER_DIVIDER_NAME_RIGHT = "RHT"
OUTER_DIVIDER_NAME_BOTTOM = "BTM"


# LENGTH (IN CHARACTERS) OF GENERATED DIVIDER AND COLLECTION NAMES
GENERATED_NAME_LENGTH = 5


# Where are output dxf files stored?
DXF_DEST_DIR = join(dirname(dirname(__file__)), "dxf_files")


# PROPORTIONAL HEIGHT OF JOINERY TABS
JOINERY_TAB_HEIGHT_PROPORTION = 0.2

# TAB OFFSET FROM THE EDGE OF THE DIVIDER IN MM
JOINERY_TAB_OFFSET_FROM_EDGE = 2


# DEPTH OF THE JOINERY CONNECTING THE VERTICAL DIVIDERS TO THE BASE IN MM
JOINERY_BASE_DEPTH = 2