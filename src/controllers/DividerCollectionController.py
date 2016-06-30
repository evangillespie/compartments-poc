#!/usr/bin/env python

"""
	for controlling DividerCollection objects
"""

__author__ = "Evan Gillespie"


from ..models.DividerCollectionModel import DividerCollectionModel
from .DividerController import DividerController
from .CompartmentController import CompartmentController


class DividerCollectionController(object):


	def __init__(self, *args, **kwargs):
		pass

	"""
	Create a new, empty DividerCollection Object

	:return: a DividerCollection object containing no Divider objects
	"""
	@classmethod
	def create_empty_divider_collection(cls, *args, **kwargs):
		return DividerCollectionModel.create_empty_divider_collection(*args, **kwargs)


	"""
	Add a new rectangualar Divider to a DividerCollection

	:param collection: the collection to add the newe divider to
	:param x_length: x_length of the new divider
	:param y_length: y_length of the new divider
	:param thickness: thickness of the new divider

	:return: name of the divider
	"""
	@classmethod
	def add_rectangular_divider_to_collection(cls, collection, x_length, y_length, thickness, name=None, *args, **kwargs):
		if not name:
			name = DividerCollectionModel.get_new_name(collection)

		div = DividerController.create_rectangular_divider(x_length, y_length, thickness, name)
		DividerCollectionModel.add_divider_to_collection(collection, div)

		return name


	"""
	"""
	@classmethod
	def add_new_compartment_to_collection(cls, collection, x_length, y_length, 
			bounding_div_names, height, level=None, offset=None, name=None):
		if not name:
			name = DividerCollectionModel.get_new_name(collection)

		com = CompartmentController.create_new_compartment(
			x_length=x_length,
			y_length=y_length,
			bounding_div_names=bounding_div_names,
			height=height,
			offset=offset,
			level=level,
			name=name)
		DividerCollectionModel.add_compartment_to_collection(collection, com)

		return com


	"""
	Return all the dividers in the collection

	:param collection: the collection to fetch dividers from

	:return: list of all dividers in the collection
	"""
	@classmethod
	def get_all_dividers_in_collection(cls, collection):
		return DividerCollectionModel.get_all_dividers_in_collection(collection)

	"""
	Retreive a particular divider by name

	:param collection: the collection to get it from
	:param name: name of the Divider to get

	:return: Divider in the collection with the name. None if no name found
	"""
	@classmethod
	def get_divider_with_name_from_collection(cls, collection, name):
		return DividerCollectionModel.get_divider_with_name_from_collection(collection, name)

