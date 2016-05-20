#!/usr/bin/env python

"""
	Model for the Divider  object

	A Divider is just a representation of the piece of wood
"""

__author__ = "Evan Gillespie"


import logging
from Model import Model

logger = logging.getLogger(__name__)


class DividerModel(Model):


	def __init__(self, *args, **kwargs):
		self.last_divider_id = 0


	"""
	Create a simple rectangular Divider

	:param width: width of the rectangle
	:param height: height of the rectangle
	:param thickness: thickness of the wood the divider will be made from

	:return: a Divider object representing a simple rectangle
	"""
	@classmethod
	def create_rectangular_divider(cls, width, height, thickness, *args, **kwargs):
		if 'name' in kwargs:
			name = kwargs['name']
		else:
			name = None

		div = Divider(name=name, thickness=thickness)
		div.add_point('outline', 0, 0)
		div.add_point('outline', 0, height)
		div.add_point('outline', width, height)
		div.add_point('outline', width, 0)

		logger.info("Creating Divider(%s)" % name)

		return div


	"""
	get the name of all layers in a particular divider

	:param divider: the divider to get layer names in

	:return: list of layer names (strings)
	"""
	@classmethod
	def get_layers_in_divider(cls, divider):
		return divider.points.keys()


	"""
	return a list of points for a particular layer in a Divider

	:param divider: the Divider to return points for
	:param layer: the name of the layer to return points for

	:return: list of points ((x,y) tuples) that belong to the layer for the Divider
	"""
	@classmethod
	def get_points_for_layer_in_divider(cls, divider, layer):
		
		if layer in divider.points:		
			return divider.points[layer]['points']
		return None


	"""
	return the color assigned to a layer

	:param divider: the Divider to return color for
	:param layer: the name of the layer to return points for

	:return: (int)color integer assigned to the layer
	"""
	@classmethod
	def get_color_for_layer_in_divider(cls, divider, layer):
		
		if layer in divider.points:		
			return divider.points[layer]['color']
		return None


# -----------------------------------------------
# ------------- Data Model Below ----------------
# -----------------------------------------------


class Divider():


	def __init__(self, name=None, thickness=None, *args, **kwargs):
		self.name = name
		self.thickness = thickness
		self.last_color = 0

		# each layer is a dict element containing:
			# layer parameters like name and color
			# a list of (x,y) tuples that represent points at the ends of lines
		self.points = dict();


	"""
	add a single point to the end of the divider list of points

	:param x: x coordinate of the new point
	:param y: y coordinate of the new point

	:return: None
	"""
	def add_point(self, layer, x, y):

		if layer not in self.points:
			self.points[layer] = {
				'name': layer,
				'color': self.get_next_color(),
				'points': [],
			}

		self.points[layer]['points'].append((x, y))


	"""
	get the next available color for a new layer
	"""
	def get_next_color(self):
		self.last_color += 1
		return self.last_color


	"""
	unabiguous string description of the divider
	"""
	def __repr__(self):
		ret = "Divider (%s)[%s]" % (self.name, len(self.points))
		if 'outline' in self.points and len(self.points['outline']['points']) > 0:
			pts = self.points['outline']['points']
			ret = ret + " << "
			ret = ret + "[%s, %s]" % (pts[0][0], pts[0]	[1])
			for p in pts[1:]:
				ret = ret + "->[%s, %s]" % (p[0], p[1])
			ret = ret + " >>"

		return ret


	"""
	basic string description of the divider
	"""
	def __str__(self):
		return "Divider (%s)[%s]" % (self.name, len(self.points))

