# !/usr/bin/env python

"""
	For turning dividers into dxf files
"""

__author__ = "Evan Gillespie"


import logging
import ezdxf
from os.path import dirname, join
from Controller import Controller
from DividerController import DividerController

logger = logging.getLogger( __name__ )

dxf_folder = join(dirname(dirname(dirname(__file__))), "dxf_files")


class DxfWriteController(Controller):


	def __init__(self, *args, **kwargs):
		pass


	"""
	Write a single Divider to a dxf file

	:param divider: the Divider to draw
	:param filename: file to write to

	:return: None
	"""
	@classmethod
	def draw_divider_to_dxf(cls, divider, filename):
		filepath = join(dxf_folder, filename)

		dwg = ezdxf.new('R2010')  # create a new DXF R2010 drawing, official DXF version name: 'AC1024'
		msp = dwg.modelspace()  # add new entities to the model space
		
		points = DividerController.get_points_for_layer_in_divider(divider, "outline") 
		points.append(points[0]) # make the points into a closed polygon
		for i in range(len(points) - 1):
			msp.add_line(points[i], points[i+1])

		dwg.saveas(filepath)

		logger.info("Drawing Divider(%s) to file(%s)" % (divider.name, filepath))

