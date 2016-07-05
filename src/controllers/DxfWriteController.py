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
		one of the layers must be 'outline'
	:param filename: file to write to
	:param folder_name: name of the folder to put these dxf files in

	:return: None
	"""
	@classmethod
	def draw_layers_and_points_to_dxf(cls, layers, filename, folder_name):

		# @TODO: Create the folder or empty the folder if it exits.

		filepath = join(DXF_DEST_DIR, folder_name, filename)

		dwg = ezdxf.new('R2010')
		msp = dwg.modelspace()

		cls.add_layer_to_drawing(dwg, msp, 'outline', layers['outline'])

		for layer_name, points in layers.iteritems():
			if layer_name != 'outline':
				cls.add_layer_to_drawing(dwg, msp, layer_name, layer_points)

		dwg.saveas(filepath)

		logger.info("Drawing Divider to file(%s)" % (filepath))


	"""
	Add a single layer to the drawing that we're building

	:param drawing: ezdxf drawing object
	:param modelspace: ezdxf modelspace
	:param name: name of the new layer
	:param points: list of point tuples that make up the layer

	:return:
	"""
	@classmethod
	def add_layer_to_drawing(cls, drawing, modelspace, name, points):
		drawing.layers.new(name=name)
		modelspace.add_lwpolyline(points + [points[0]], dxfattribs={'layer': name})
