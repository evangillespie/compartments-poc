#!/usr/bin/env python

"""
	for controlling Divider objects
"""

__author__ = "Evan Gillespie"


from ..models.DividerModel import DividerModel


class DividerController(object):


	def __init__(self, *args, **kwargs):
		pass


	"""
	Create a simple rectangular Divider

	:param x_length: x_length of the rectangle
	:param y_length: y_length of the rectangle
	:param thickness: thickness of the wood the divider will be made from

	:return: a Divider object representing a simple rectangle
	"""
	@classmethod
	def create_rectangular_divider(cls, x_length, y_length, thickness, name=None, *args, **kwargs):
		return DividerModel.create_rectangular_divider(x_length, y_length, thickness, name, *args, **kwargs)


	"""
	Add male joinery to the left and right edges of a divider

	:param divider: the divider to add joinery to
	:param width: width of the joinery to add. Usually the thickness of material.

	:return:
	"""
	@classmethod
	def add_male_joinery_to_divider(cls, divider, width):
		DividerModel.add_male_joinery_to_divider_sides(divider, width)


	"""
	Add male joinery to the bottom of the divider. For connecting vertical bits to the base

	:param divider: the divider to add jonery to
	:param depth: how deep into the base will the pieces go?

	:return:
	"""
	@classmethod
	def add_base_joinery_to_vertical_divider(cls, divider, depth=None):
		DividerModel.add_base_joinery_to_vertical_divider(divider, depth)


	"""
	Add female joinery to the base that will connect with the vertical dividers

	:param base_divider: the base Divider object
	:param x_length: length of the joint in the x direction
	:param y_length: length of the joint in the y direction
	:param offsets: (x,y) tuple of offsets to the lower left corner of the joint
	:param depth: how deep does this joinery go?

	:return:
	"""
	@classmethod
	def add_female_joinery_to_base(cls, base_divider, x_length, y_length, offsets, depth=None):
		DividerModel.add_female_joinery_to_base(base_divider, x_length, y_length, offsets)


	"""
	Add female joinery to a divider, starting at a certain distance from the edge

	:param divider: the divider to add female joinery to
	:param offset: distance from the edge of the divider to the start of the female joint (socket)
	:param width: width of the female joint (socket)

	:return:
	"""
	@classmethod
	def add_female_joinery_to_divider(cls, divider, offset, width):
		DividerModel.add_female_joinery_to_divider(divider, offset, width)


	"""
	Return a dict of layers of points that represents the divider with all joinery

	:param divider: the divider to export as points
	
	:return: Dictionary where each value is a list of points making up a layer.
				one layer must be names 'outline'. The rest dont matter
			{
				'outline': [(0, 0), (0, 10), ...],
				'1': [(1, 3), (1, 5), ...]
			}
	"""
	@classmethod
	def convert_divider_to_points(cls, divider):
		return DividerModel.convert_divider_to_points(divider)
