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
	Create a new compartment and add it to a collection

	:param collection: The collection to add the new compartment to
	:param x_length: x length of the new compartment
	:param y_length: y length of the new compartment
	:param bounding_div_names: Tuple of names of the dividers that enclose this 
						compartment (left, top, right, bottom)
	:param height: height of the compartment. Should be the same for each compartment in the collection
	:param level: depth of this compartment. top level is 1
	:param offset: Tuple of offsets from the parent compartment
	:param name: name for this compartment. Unique in the collection
	:param parent_name: name of the parent compartment

	:return: newly created Compartment
	"""
	@classmethod
	def add_new_compartment_to_collection(cls, collection, x_length, y_length, 
			bounding_div_names, height, level=None, offset=None, name=None, parent_name=None):
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

		if parent_name:
			DividerCollectionModel.register_child_parent_names(
				collection=collection,
				child_name=name,
				parent_name=parent_name
			)

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


	"""
	return the parent of a given compartment

	:param collection: collection to get the parent from
	:param compartment: compartment to get the parent of

	:return: Compartment which is the parent of compartment(argument). None if it has no parent
	"""
	@classmethod
	def get_compartment_parent(cls, collection, compartment):
		return DividerCollectionModel.get_compartment_parent(collection, compartment)


	"""
	calculate the total offset for a compartment and all parents in this collection

	:param collection: the collection
	:param compartment: compartment to calculate the total offset of

	:return: total offset of this compartment and all parents
	"""
	@classmethod
	def get_compartment_total_offset(cls, collection, compartment):
		
		total_offset_x = compartment.offset[0]
		total_offset_y = compartment.offset[1]

		parent = cls.get_compartment_parent(collection, compartment)
		while parent:
			total_offset_x += parent.offset[0]
			total_offset_y += parent.offset[1]
			parent = cls.get_compartment_parent(collection, parent)

		return (total_offset_x, total_offset_y)
