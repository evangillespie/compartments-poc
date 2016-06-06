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

	:param length: length of the rectangle
	:param width: width of the rectangle
	:param thickness: thickness of the wood the divider will be made from

	:return: a Divider object representing a simple rectangle
	"""
	@classmethod
	def create_rectangular_divider(cls, length, width, thickness, *args, **kwargs):
		return DividerModel.create_rectangular_divider(length, width, thickness, *args, **kwargs)
