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
	def create_rectangular_divider(cls, x_length, y_length, thickness, *args, **kwargs):
		return DividerModel.create_rectangular_divider(x_length, y_length, thickness, *args, **kwargs)
