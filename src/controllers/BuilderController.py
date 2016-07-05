#!/usr/bin/env python

"""
	for building a plan into dividers.
"""

__author__ = "Evan Gillespie"


import logging
from ..config import OUTER_DIVIDER_NAME_BASE, OUTER_DIVIDER_NAME_LEFT, \
	OUTER_DIVIDER_NAME_TOP, OUTER_DIVIDER_NAME_RIGHT, OUTER_DIVIDER_NAME_BOTTOM
from CompartmentController import CompartmentController
from DividerController import DividerController
from DividerCollectionController import DividerCollectionController
from DxfWriteController import DxfWriteController


logger = logging.getLogger( __name__ )


class BuilderController(object):


	def __init__(self, *args, **kwargs):
		pass


	"""
	turn an organizer plan into a divider collection.
	This is a real meaty function

	:param plan: the plan to be turned

	:return: a DividerCollection object
	"""
	@classmethod
	def build_divider_collection_from_plan(cls, plan, *args, **kwargs):

		collection = DividerCollectionController.create_empty_divider_collection()

		cls.create_base_and_edge_dividers_from_plan(collection, plan)

		cls.interpret_plan_into_compartments_and_dividers(plan, collection)

		for d in DividerCollectionController.get_all_dividers_in_collection(collection):
			DxfWriteController.draw_layers_and_points_to_dxf(
				DividerController.convert_divider_to_points(d),
				d.name + ".dxf",
				collection.id
			)

		print collection
		for d in DividerCollectionController.get_all_dividers_in_collection(collection):
			print repr(d)
		for c in collection.compartments:
			print repr(c)


	"""
	create the base and outside edge dividers

	:param collection: DividerCollection to store new divders in
	:param plan: the base plan that defines dimensions to use

	:return:
	"""
	@classmethod
	def create_base_and_edge_dividers_from_plan(cls, collection, plan):
		DividerCollectionController.add_rectangular_divider_to_collection(
			collection=collection,
			x_length=plan['x_length'],
			y_length=plan['y_length'],
			thickness=plan['thickness' ],
			name=OUTER_DIVIDER_NAME_BASE
		)

		div_height = plan['height'] - plan['thickness']

		DividerCollectionController.add_rectangular_divider_to_collection(
			collection=collection,
			x_length=plan['y_length'],
			y_length=div_height,
			thickness=plan['thickness' ],
			name=OUTER_DIVIDER_NAME_LEFT
		)
		DividerCollectionController.add_rectangular_divider_to_collection(
			collection=collection,
			x_length=plan['y_length'],
			y_length=div_height,
			thickness=plan['thickness' ],
			name=OUTER_DIVIDER_NAME_RIGHT
		)
		DividerCollectionController.add_rectangular_divider_to_collection(
			collection=collection,
			x_length=plan['x_length'] -  2*plan['thickness'],
			y_length=div_height,
			thickness=plan['thickness' ],
			name=OUTER_DIVIDER_NAME_TOP
		)
		DividerCollectionController.add_rectangular_divider_to_collection(
			collection=collection,
			x_length=plan['x_length'] -  2*plan['thickness'],
			y_length=div_height,
			thickness=plan['thickness' ],
			name=OUTER_DIVIDER_NAME_BOTTOM
		)


	"""
	Read through the plan (json) and create a bunch of suitible objects
	and add those objects to a particular DividerCollection

	:param plan: json plan from the JS app. Expected to be formatted in a certain way
	:param collection: the DividerCollection to add Divider and Compartment objects to

	:return:
	"""
	@classmethod
	def interpret_plan_into_compartments_and_dividers(cls, plan, collection):
		
		div_height = plan['height'] - plan['thickness']


		"""
		Create a compartment object and any dividers inside of it,
		then call recursively for any compartments inside
		"""
		def recursively_interpret_compartment_plan(compartment_json, bounding_div_names, 
				level=1, offset=None, parent_name=None):
			
			if not offset:
				offset = (0,0)

			compartment = DividerCollectionController.add_new_compartment_to_collection(
				collection = collection,
				x_length=compartment_json['x_length'],
				y_length=compartment_json['y_length'],
				bounding_div_names=bounding_div_names,
				height=div_height,
				level=level,
				offset=offset,
				parent_name=parent_name
			)

			child_comp_index = 0
			new_div_name = None
			prev_div_name = None
			new_bounding_div_names = None
			offset = [0, 0]
			for child_comp_index, child_comp_json in enumerate(compartment_json['compartments']):
				prev_div_name = new_div_name
				# only add a new divider to the end of the n-1 compartments
				# the nth compartment is already bounded by the time you reach it 
				if child_comp_index < len(compartment_json['compartments']) - 1:
					# read through the child compartments and put a divider after each one.
					# x direction is read rightward and y is read upward.
					if compartment_json['div_orientation'] == 'x':
						new_div_length = compartment_json['compartments'][child_comp_index]['x_length']
						new_div_offset = compartment_json['compartments'][child_comp_index]['y_length']
					elif compartment_json['div_orientation'] == 'y':
						new_div_length = compartment_json['compartments'][child_comp_index]['y_length']
						new_div_offset = compartment_json['compartments'][child_comp_index]['x_length']
					else:
						logger.error("Weird div_orientation in plan: %s" % compartment_json['div_orientation'])

					new_div = DividerCollectionController.add_rectangular_divider_to_collection(
						collection=collection,
						x_length=new_div_length,
						y_length=div_height,
						thickness=plan['thickness' ]
					)

					# add joinery to new divider and 
					DividerCollectionController.add_joinery_to_divider(
						divider=new_div,
						div_orientation=compartment_json['div_orientation'],
						div_offset_in_comp=tuple(offset),
						containing_compartment=compartment,
						width=plan['thickness']
					)


				#increment the offset
				if child_comp_index > 0:
					if compartment_json['div_orientation'] == 'x':
						offset[1] += compartment_json['compartments'][child_comp_index-1]['y_length']
						offset[1] += plan['thickness']
					elif compartment_json['div_orientation'] == 'y':
						offset[0] += compartment_json['compartments'][child_comp_index-1]['x_length']
						offset[0] += plan['thickness']

				# Update the bounding divider names for child compartments
				new_bounding_div_names = cls.get_new_bounding_div_names(
					parent_bounding_div_names=bounding_div_names,
					orientation=compartment_json['div_orientation'],
					new_div_name=new_div.name,
					prev_div_name=prev_div_name,
					comp_index=child_comp_index,
					num_comps=len(compartment_json['compartments'])
				)

				recursively_interpret_compartment_plan(
					child_comp_json,
					new_bounding_div_names,
					level=level+1,
					parent_name=compartment.name,
					offset=tuple(offset)
				)


		# Call the recursive function for the first time.
		recursively_interpret_compartment_plan(
			compartment_json=plan['compartments'][0],
			bounding_div_names=(
				OUTER_DIVIDER_NAME_LEFT,
				OUTER_DIVIDER_NAME_TOP,
				OUTER_DIVIDER_NAME_RIGHT,
				OUTER_DIVIDER_NAME_BOTTOM
			),
			offset=(0, plan['thickness'])
		)


	"""
	Return a tuple of bounding divider names for a new child compartment

	:param parent_bounding_div_names: bounding divider names of the parent compartment
	:param orientation: which way are the dividers oriented between these child compartments? x or y?
	:param new_div_name: Name of the newest divider created for these child compartments
	:param prev_div_name: Name of the previous divider created for these child compartments
	:param comp_index: which child compartment are we on in the set? starts at 0.
	:param num_comps: number of total child compartments in the set.

	:return: Tuple of divider names for a new compartment (left, top, right, bottom)
	"""
	@classmethod
	def get_new_bounding_div_names(cls, parent_bounding_div_names, orientation,
							new_div_name, prev_div_name, comp_index, num_comps):
		if num_comps == 1:
			return parent_bounding_div_names

		else:	
			if comp_index == 0:
				if orientation == 'x':
					return (
						parent_bounding_div_names[0],
						new_div_name,
						parent_bounding_div_names[2],
						parent_bounding_div_names[3]
					)
				else:
					return (
						parent_bounding_div_names[0],
						parent_bounding_div_names[1],
						new_div_name,
						parent_bounding_div_names[3]
					)
			elif comp_index < num_comps - 1:
				if orientation == 'x':
					return (
						parent_bounding_div_names[0],
						new_div_name,
						parent_bounding_div_names[2],
						prev_div_name
					)
				else:
					return (
						prev_div_name,
						parent_bounding_div_names[1],
						new_div_name,
						parent_bounding_div_names[3]
					)
			else:
				if orientation == 'x':
					return (
						parent_bounding_div_names[0],
						parent_bounding_div_names[1],
						parent_bounding_div_names[2],
						prev_div_name
					)
				else:
					return (
						prev_div_name,
						parent_bounding_div_names[1],
						parent_bounding_div_names[2],
						parent_bounding_div_names[3]
					)