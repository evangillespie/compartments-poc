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
		cls.write_collection_dividers_to_dxf(collection)


	"""
	create the base and outside edge dividers

	:param collection: DividerCollection to store new divders in
	:param plan: the base plan that defines dimensions to use

	:return:
	"""
	# @TODO: break this into smaller functions
	@classmethod
	def create_base_and_edge_dividers_from_plan(cls, collection, plan):

		# create the base
		base = DividerCollectionController.add_rectangular_divider_to_collection(
			collection=collection,
			x_length=plan['x_length'],
			y_length=plan['y_length'],
			thickness=plan['thickness' ],
			name=OUTER_DIVIDER_NAME_BASE
		)


		#create the outer edges
		div_height = plan['height'] - plan['thickness']

		left = DividerCollectionController.add_rectangular_divider_to_collection(
			collection=collection,
			x_length=plan['y_length'],
			y_length=div_height,
			thickness=plan['thickness' ],
			name=OUTER_DIVIDER_NAME_LEFT
		)
		right = DividerCollectionController.add_rectangular_divider_to_collection(
			collection=collection,
			x_length=plan['y_length'],
			y_length=div_height,
			thickness=plan['thickness' ],
			name=OUTER_DIVIDER_NAME_RIGHT
		)
		top = DividerCollectionController.add_rectangular_divider_to_collection(
			collection=collection,
			x_length=plan['x_length'] -  2*plan['thickness'],
			y_length=div_height,
			thickness=plan['thickness' ],
			name=OUTER_DIVIDER_NAME_TOP
		)
		bottom = DividerCollectionController.add_rectangular_divider_to_collection(
			collection=collection,
			x_length=plan['x_length'] -  2*plan['thickness'],
			y_length=div_height,
			thickness=plan['thickness' ],
			name=OUTER_DIVIDER_NAME_BOTTOM
		)

		#add joinery to the outer edges
		#male edge joinery on the top, bottom, female on the left, right
		for d in [top, bottom]:
			DividerController.add_male_joinery_to_divider(d, plan['thickness'])
			
			DividerController.add_base_joinery_to_vertical_divider(d)

		# add female base joinery to the base divider
		DividerController.add_female_joinery_to_base(
			base,
			plan['x_length'] -  2*plan['thickness'],
			plan['thickness'],
			(plan['thickness'], 0)
		)
		DividerController.add_female_joinery_to_base(
			base,
			plan['x_length'] -  2*plan['thickness'],
			plan['thickness'],
			(plan['thickness'], plan['y_length'] - plan['thickness'])
		)

		for d in [left, right]:
			DividerController.add_base_joinery_to_vertical_divider(d)
			DividerController.add_female_joinery_to_divider(
				d,
				0,
				plan['thickness']
			)
			DividerController.add_female_joinery_to_divider(
				d,
				d.x_length - plan['thickness'],
				plan['thickness']
			)
		DividerController.add_female_joinery_to_base(
			base,
			plan['thickness'],
			plan['y_length'],
			(0, 0)
		)
		DividerController.add_female_joinery_to_base(
			base,
			plan['thickness'],
			plan['y_length'],
			(plan['x_length'] - plan['thickness'], 0)
		)


	"""
	Read through the plan (json) and create a bunch of suitible objects
	and add those objects to a particular DividerCollection

	:param plan: json plan from the JS app. Expected to be formatted in a certain way
	:param collection: the DividerCollection to add Divider and Compartment objects to

	:return:
	"""
	# @TODO: this function is too long. Break it out into smaller ones.
	@classmethod
	def interpret_plan_into_compartments_and_dividers(cls, plan, collection):
		
		# height of the vertical Dividers. They sit on top of the base Divider
		div_height = plan['height'] - plan['thickness']


		"""
		Create a compartment object and any dividers inside of it,
		then call recursively for any compartments inside.
		Put those objects into the collection
		"""
		def recursively_interpret_compartment_plan(compartment_json, bounding_div_names, 
				level=1, offset=None, parent_name=None):

			# (0,0) is the bottom left corner
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
			new_div = None
			prev_div_name = None
			new_bounding_div_names = None
			running_offset = [0, 0]

			for child_comp_index, child_comp_json in enumerate(compartment_json['compartments']):

				if new_div:
					prev_div_name = new_div.name
				# read through the child compartments and put a divider after each one.
				# only add a new divider to the end of the n-1 compartments
				# the nth compartment is already bounded by the time you reach it 
				if child_comp_index < len(compartment_json['compartments']) - 1:
					# x direction is read rightward and y is read upward.
					if compartment_json['div_orientation'] == 'x':
						new_div_length = compartment_json['compartments'][child_comp_index]['x_length']
					elif compartment_json['div_orientation'] == 'y':
						new_div_length = compartment_json['compartments'][child_comp_index]['y_length']
					else:
						logger.error("Weird div_orientation in plan: %s" % compartment_json['div_orientation'])

					new_div = DividerCollectionController.add_rectangular_divider_to_collection(
						collection=collection,
						x_length=new_div_length,
						y_length=div_height,
						thickness=plan['thickness' ]
					)


					# add joinery to new divider 
					div_offset = list(running_offset)	# need to use the list() constructor to make a duplicate, not just a ref
					if compartment_json['div_orientation'] == 'x':
						div_offset[1] += compartment_json['compartments'][child_comp_index-1]['y_length']
					else:
						div_offset[0] += compartment_json['compartments'][child_comp_index-1]['x_length']

					DividerCollectionController.add_joinery_to_divider(
						collection=collection,
						divider=new_div,
						div_orientation=compartment_json['div_orientation'],
						div_offset_in_comp=tuple(div_offset),
						containing_compartment=compartment,
						width=plan['thickness']
					)

				# increment the running_offset
				if child_comp_index > 0:
					if compartment_json['div_orientation'] == 'x':
						running_offset[1] += compartment_json['compartments'][child_comp_index-1]['y_length']
						running_offset[1] += plan['thickness']
					elif compartment_json['div_orientation'] == 'y':
						running_offset[0] += compartment_json['compartments'][child_comp_index-1]['x_length']
						running_offset[0] += plan['thickness']

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
					offset=tuple(running_offset)
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
			# @HACK: offsets start non-zero to account for overlap in the outside edges
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


	"""
	Turn the Dividers in a DividerCollection in to a bunch of DXF files

	:param collection: the collection to turn into DXFs

	:return:
	"""
	# @TODO: Some of this logic should move to the DxfWriteController
	@classmethod
	def write_collection_dividers_to_dxf(cls, collection):
		DxfWriteController.create_empty_dxf_directory(collection.id)
		for d in DividerCollectionController.get_all_dividers_in_collection(collection):
			DxfWriteController.draw_layers_and_points_to_dxf(
				DividerController.convert_divider_to_points(d),
				str(d.name)	 + ".dxf",
				collection.id
			)
