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

	:param length: length of the rectangle
	:param width: width of the rectangle
	:param thickness: thickness of the wood the divider will be made from

	:return: a Divider object representing a simple rectangle
	"""
	@classmethod
	def create_rectangular_divider(cls, length, width, thickness, *args, **kwargs):
		if 'name' in kwargs:
			name = kwargs['name']
		else:
			name = None

		div = Divider(name=name, length=length, width=width, thickness=thickness)

		logger.debug("Creating Divider(%s)" % name)

		return div


# -----------------------------------------------
# ------------- Data Model Below ----------------
# -----------------------------------------------


class Divider():


	def __init__(self, name=None, length=None, width=None, thickness=None, *args, **kwargs):
		self.name = name
		self.length = length
		self.width = width
		self.thickness = thickness

		# list of (x,y) points that make up the outer perimeter
		self.points = []
		self.points.append((0,0))
		self.points.append((0, width))
		self.points.append((length, width))
		self.points.append((length, 0))


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

