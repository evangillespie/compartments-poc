#!/usr/bin/env python

"""
	for controlling Divider objects
"""

__author__ = "Evan Gillespie"


from Controller import Controller
from ..models.DividerModel import DividerModel


class DividerController(Controller):


	def __init__(self, *args, **kwargs):
		pass


	"""
	Create a simple rectangular Divider

	:param width: width of the rectangle
	:param height: height of the rectangle
	:param thickness: thickness of the wood the divider will be made from

	:return: a Divider object representing a simple rectangle
	"""
	@classmethod
	def create_rectangular_divider(cls, width, height, thickness, *args, **kwargs):
		return DividerModel.create_rectangular_divider(width, height, thickness, *args, **kwargs)


	"""
	get the name of all layers in a particular divider

	:param divider: the divider to get layer names in

	:return: list of layer names (strings)
	"""
	@classmethod
	def get_layers_in_divider(cls, divider):
		return DividerModel.get_layers_in_divider(divider)


	"""
	return a list of points for a particular layer in a Divider

	:param divider: the Divider to return points for
	:param layer: the name of the layer to return points for

	:return: list of points ((x,y) tuples) that belong to the layer for the Divider
	"""
	@classmethod
	def get_points_for_layer_in_divider(cls, divider, layer):
		return DividerModel.get_points_for_layer_in_divider(divider, layer)


		"""
	return the color assigned to a layer

	:param divider: the Divider to return color for
	:param layer: the name of the layer to return points for

	:return: (int)color integer assigned to the layer
	"""
	@classmethod
	def get_color_for_layer_in_divider(cls, divider, layer):
		return DividerModel.get_color_for_layer_in_divider(divider, layer)
