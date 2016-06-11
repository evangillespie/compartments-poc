#!/usr/bin/env python

"""
	Model for the Divider  object

	A Divider is just a representation of the piece of wood
"""

__author__ = "Evan Gillespie"


import logging


logger = logging.getLogger(__name__)


class DividerModel(object):


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
		if not name:
			logger.error("Trying to create a divider without a name. That'll be trouble")

		div = Divider(name=name, x_length=x_length, y_length=y_length, thickness=thickness, *args, **kwargs)

		logger.debug("Creating Divider(%s)" % name)

		return div


# -----------------------------------------------
# ------------- Data Model Below ----------------
# -----------------------------------------------


class Divider():


	def __init__(self, name=None, x_length=None, y_length=None, thickness=None, *args, **kwargs):
		self.name = name
		self.x_length = x_length
		self.y_length = y_length
		self.thickness = thickness

		# Distance that this divider overlaps another.
		# Joinery meansurements are ofset because of this.
		self.joinery_offset=None

		if 'joinery_offset' in kwargs:
			self.joinery_offset = kwargs['joinery_offset']

		# a list of joinery elements to be added or subtracted from the base rectangle
		self.joinery = []


	"""
	unabiguous string description of the divider
	"""
	def __repr__(self):
		ret = "Divider (%s)[%s,%s]" % (self.name, self.x_length, self.y_length)
		return ret


	"""
	basic string description of the divider
	"""
	def __str__(self):
		if self.name:
			return "Divider (%s)" % (self.name)
		else:
			return "Divider (--)"

