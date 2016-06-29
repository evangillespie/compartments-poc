#!/usr/bin/env python

"""
	For building out compartments to be turned into dividers
"""

__author__ = "Evan Gillespie"


import logging
from ..models.CompartmentModel import CompartmentModel


logger = logging.getLogger( __name__ )


class CompartmentController(object):


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
	:param level: how many generations of parents does this compartment have?

	:return: new Compartment
	"""
	@classmethod
	def create_new_compartment(cls, x_length, y_length, bounding_div_names, height,
								offset=None, level=None, *args, **kwargs):
		return CompartmentModel.create_new_compartment(
			x_length=x_length,
			y_length=y_length,
			bounding_div_names=bounding_div_names,
			height=height,
			offset=offset,
			level=level
		)
