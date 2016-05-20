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
