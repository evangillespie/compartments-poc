#!/usr/bin/env python

"""
	for controlling DividerCollection objects
"""

__author__ = "Evan Gillespie"


from ..models.DividerCollectionModel import DividerCollectionModel
from .DividerController import DividerController


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
	:param length: length of the new divider
	:param width: width of the new divider
	:param thickness: thickness of the new divider

	:return: None
	"""
	@classmethod
	def add_rectangular_divider_to_collection(cls, collection, length, width, thickness, *args, **kwargs):
		div = DividerController.create_rectangular_divider(length, width, thickness, *args, **kwargs)
		cls.add_divider_to_collection(collection, div)


	"""
	Add a Divider to a DividerCollection

	:param collection: the collection to add it to
	:param divider: the Divider to add to the collection

	:return: updated DividerCollection
	"""
	@classmethod
	def add_divider_to_collection(cls, collection, divider, *args, **kwargs):
		DividerCollectionModel.add_divider_to_collection(collection, divider)


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

