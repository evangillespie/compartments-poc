#!/usr/bin/env python

"""
	for controlling DividerCollection objects
"""

__author__ = "Evan Gillespie"


import logging
from ..models.DividerCollectionModel import DividerCollectionModel
from .DividerController import DividerController
from .CompartmentController import CompartmentController
from ..config import OUTER_DIVIDER_NAME_BASE


logger = logging.getLogger(__name__)


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

	:return: new Divider object
	"""
	@classmethod
	def add_rectangular_divider_to_collection(cls, collection, x_length, y_length, thickness, name=None, *args, **kwargs):
		if not name:
			name = DividerCollectionModel.get_new_name(collection)

		div = DividerController.create_rectangular_divider(x_length, y_length, thickness, name)
		DividerCollectionModel.add_divider_to_collection(collection, div)

		return div


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


	"""
	get total offset for a compartment along one divider edge
	ie. If a compartment is is the middle of the overall structure but joined to the left outside
		edge on one side and a partway inner edge on the right side, those have different offsets

	:param collection: the collection to look within
	:param compartment: the compartment to calculate offset of
	:param ref_edge: 'left', 'top', 'right' or 'bottom'

	:return: the total compartment offset along the desired edge
	"""
	@classmethod
	def get_compartment_total_offset_along_edge(cls, collection, compartment, ref_edge):

		edge_div_name = CompartmentController.get_bounding_div_name_for_compartment_on_side(compartment, ref_edge)

		if ref_edge == 'left' or ref_edge == 'right':
			offset_ind = 1
		else:
			offset_ind = 0

		offset_along_edge = compartment.offset[offset_ind]

		parent = cls.get_compartment_parent(collection, compartment)
		while parent:
			parent_edge_div_name = CompartmentController.get_bounding_div_name_for_compartment_on_side(parent, ref_edge)
			if parent_edge_div_name == edge_div_name:
				offset_along_edge += parent.offset[offset_ind]
			parent = cls.get_compartment_parent(collection, parent)

		return offset_along_edge


	"""
	add joinery to a divider and it's mate. Male joinery on the divider and female on
		bounding dividers of the compartment

	:param collection: the DividerCollection that these dividers and compartments live in
	:param divider: Divider object to add male joinery to
	:param div_orientation: orientation of the Divider in the overall plan
	:param div_offset_in_comp: where does this Divider lie in the containing Compartment
	:param containing_compartment: Compartment that the Divider lives inside of
	:param width: the width of the joinery. For male how far it extends, for female how wide the slots are

	:return:
	"""
	@classmethod
	def add_joinery_to_divider(cls, collection, divider, div_orientation, div_offset_in_comp, containing_compartment, width):

		# add male joinery to left and right edges
		DividerController.add_male_joinery_to_divider(divider, width)

		# add female joinery to the bounding dividers
		if div_orientation == 'x':
			female_edges = ['left', 'right']
			fem_offset = div_offset_in_comp[1]
			base_fem_x_length = divider.x_length # x length of the divider is how long it is
			base_fem_y_length = divider.thickness
		else:
			female_edges = ['top', 'bottom']
			fem_offset = div_offset_in_comp[0]
			base_fem_y_length = divider.x_length
			base_fem_x_length = divider.thickness

		for edge_name in female_edges:
			com_offset = cls.get_compartment_total_offset_along_edge(collection, containing_compartment, edge_name)
			edge_div = cls.get_divider_with_name_from_collection(
				collection, 
				CompartmentController.get_bounding_div_name_for_compartment_on_side(containing_compartment, edge_name)
			)
			DividerController.add_female_joinery_to_divider(edge_div, fem_offset + com_offset, divider.thickness)

		containing_offset = cls.get_compartment_total_offset(collection, containing_compartment)

		# Add male joinery for the base
		DividerController.add_base_joinery_to_vertical_divider(divider)

		# Add female joinery to the base		
		base_fem_join_offset = (
			div_offset_in_comp[0] + containing_offset[0] + divider.thickness,
			div_offset_in_comp[1] + containing_offset[1],
		)
		# @HACK: thickness added to the first argument to compensate for the starting 0,6) offset

		DividerController.add_female_joinery_to_base(
			cls.get_divider_with_name_from_collection(collection, OUTER_DIVIDER_NAME_BASE),
			base_fem_x_length,
			base_fem_y_length,
			base_fem_join_offset
		)
