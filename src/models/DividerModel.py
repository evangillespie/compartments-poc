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
		div.add_point(0, height)
		div.add_point(width, height)
		div.add_point(width, 0)

		logger.info("Creating Divider(%s)" % name)
		return div


# -----------------------------------------------
# ------------- Data Model Below ----------------
# -----------------------------------------------


class Divider():


	def __init__(self, name=None, thickness=None, *args, **kwargs):
		self.name = name
		self.thickness = thickness

		# points is a list of (x,y) tuples that represent points at the ends of lines
		self.points = list()


	"""
	add a single point to the end of the divider list of points

	:param x: x coordinate of the new point
	:param y: y coordinate of the new point

	:return: None
	"""
	def add_point(self, x, y):

		# if we don't have a point yet, start at 0
		if not self.points:
			self.points.append((0, 0))

		self.points.append((x, y))


	"""
	unabiguous string description of the divider
	"""
	def __repr__(self):
		ret = "Divider (%s)[%s]" % (self.name, len(self.points))
		if len(self.points) > 0:
			ret = ret + " << "
			ret = ret + "[%s, %s]" % (self.points[0][0], self.points[0]	[1])
			for p in self.points[1:]:
				ret = ret + "->[%s, %s]" % (p[0], p[1])
			ret = ret + " >>"

		return ret


	"""
	basic string description of the divider
	"""
	def __str__(self):
		return "Divider (%s)[%s]" % (self.name, len(self.points))

