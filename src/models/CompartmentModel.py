#!/usr/bin/env python

"""
	Model for the Compartment object
"""

__author__ = "Evan Gillespie"


import logging

logger = logging.getLogger(__name__)


class CompartmentModel(object):


	def __init__(self, *args, **kwargs):
		pass


	"""
	Create a new compartment

	:param x_length: length of compartment in x_direction
	:param y_length: length of compartment in y_direction
	:param bounding_div_names: Tuple of names of the dividers that enclose this 
						compartment (left, top, right, bottom)
	:param height: height of the compartment. Should be the same for each compartment in the collection
	:param offset: Tuple of offsets from the parent compartment
	:param name: name for this compartment. Unique in the collection

	:return: new Compartment object
	"""
	@classmethod
	def create_new_compartment(cls, x_length, y_length, bounding_div_names, height,
								offset=None, level=None, name=None, *args, **kwargs):
		comp = Compartment(x_length, y_length, height, name=name)
		comp.bounding_div_names['left'] = bounding_div_names[0]
		comp.bounding_div_names['top'] = bounding_div_names[1]
		comp.bounding_div_names['right'] = bounding_div_names[2]
		comp.bounding_div_names['bottom'] = bounding_div_names[3]
		
		if level:
			comp.level = level

		if offset:
			comp.offset=offset

		return comp


# -----------------------------------------------
# ------------- Data Model Below ----------------
# -----------------------------------------------


class Compartment():


	def __init__(self, x_length, y_length, height, name=None, *args, **kwargs):

		self.name = name

		self.x_length = x_length
		self.y_length = y_length
		self.height=height

		self.level=None

		self.bounding_div_names={}

		self.offset=None

	"""
	unabiguous string description of the dividercollection
	"""
	def __repr__(self):
		ret = "Compartment"
		if self.name:
			ret += " (%s)" % self.name
		if self.level:
			ret += "[%s]" % self.level
		ret += " (%s x %s x %s)" % (self.x_length, self.y_length, self.height)
		if self.offset:
			ret += "{%s,%s}" % (self.offset[0], self.offset[1])
		if self.bounding_div_names:
			ret += "< %s, %s, %s, %s >" % \
				(self.bounding_div_names['left'], self.bounding_div_names['top'], 
					self.bounding_div_names['right'], self.bounding_div_names['bottom'])
		return ret


	"""
	basic string description of the divider
	"""
	def __str__(self):
		return "Compartment (%s x %s)" % (self.x_length, self.y_length)
