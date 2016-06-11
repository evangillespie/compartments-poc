#!/usr/bin/env python

"""
	for building a plan into dividers.
"""

__author__ = "Evan Gillespie"


import logging
from DividerCollectionController import DividerCollectionController


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

		print collection
		for d in DividerCollectionController.get_all_dividers_in_collection(collection):
			print repr(d)


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
			name="BASE"
		)

		div_height = plan['height'] - plan['thickness']

		DividerCollectionController.add_rectangular_divider_to_collection(
			collection=collection,
			x_length=plan['y_length'],
			y_length=div_height,
			thickness=plan['thickness' ],
			name="LFT",
			joinery_offset=plan['thickness']
		)
		DividerCollectionController.add_rectangular_divider_to_collection(
			collection=collection,
			x_length=plan['y_length'],
			y_length=div_height,
			thickness=plan['thickness' ],
			name="RHT",
			joinery_offset=plan['thickness']
		)
		DividerCollectionController.add_rectangular_divider_to_collection(
			collection=collection,
			x_length=plan['x_length'] -  2*plan['thickness'],
			y_length=div_height,
			thickness=plan['thickness' ],
			name="TOP"
		)
		DividerCollectionController.add_rectangular_divider_to_collection(
			collection=collection,
			x_length=plan['x_length'] -  2*plan['thickness'],
			y_length=div_height,
			thickness=plan['thickness' ],
			name="BTM"
		)
