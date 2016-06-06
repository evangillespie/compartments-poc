# !/usr/bin/env python

"""
	For turning dividers into dxf files
"""

__author__ = "Evan Gillespie"


import logging
import ezdxf
from os.path import join
from DividerController import DividerController
from ..config import DXF_DEST_DIR

logger = logging.getLogger( __name__ )


class DxfWriteController(object):


	def __init__(self, *args, **kwargs):
		pass


	"""
	Write a single Divider to a dxf file

	:param layers: dict of layers to draw out
		layers = {<layer name>:[(x1, y1), (x2, y2), ...]}
	:param filename: file to write to

	:return: None
	"""
	@classmethod
	def draw_layers_and_points_to_dxf(cls, layers, filename):
		filepath = join(DXF_DEST_DIR, filename)

		dwg = ezdxf.new('R2010')
		msp = dwg.modelspace()

		# @TODO: update the dxf drawing stuff to use the new divider formatting

		# for layer_name in DividerController.get_layers_in_divider(divider):
		# 	dwg.layers.new(
		# 		name=layer_name,
		# 		dxfattribs={
		# 			'color': DividerController.get_color_for_layer_in_divider(divider, layer_name)
		# 		}
		# 	)
		# 	points = DividerController.get_points_for_layer_in_divider(divider, layer_name) 
		# 	points.append(points[0]) # make the points into a closed loop
		# 	msp.add_lwpolyline(points, dxfattribs={'layer': layer_name})

		dwg.saveas(filepath)

		logger.info("Drawing Divider to file(%s)" % (filepath))

