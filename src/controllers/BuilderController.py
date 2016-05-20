#!/usr/bin/env python

"""
	for building a plan into dividers.
"""

__author__ = "Evan Gillespie"


import logging
from Controller import Controller
from DividerCollectionController import DividerCollectionController

logger = logging.getLogger( __name__ )

class BuilderController(Controller):


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

		# create the base and edge dividers in the collection
		base_div = DividerCollectionController.add_rectangualar_divider_to_collection(
				collection,
				plan['width'],
				plan['length'],
				plan['thickness'],
				name='base',
			)

		base_div = DividerCollectionController.add_rectangualar_divider_to_collection(
				collection,
				plan['length'],
				plan['height'],
				plan['thickness'],
				name='left_edge',
			)
		base_div = DividerCollectionController.add_rectangualar_divider_to_collection(
				collection,
				plan['length'],
				plan['height'],
				plan['thickness'],
				name='right_edge',
			)
		base_div = DividerCollectionController.add_rectangualar_divider_to_collection(
				collection,
				plan['width'],
				plan['height'],
				plan['thickness'],
				name='top_edge',
			)
		base_div = DividerCollectionController.add_rectangualar_divider_to_collection(
				collection,
				plan['width'],
				plan['height'],
				plan['thickness'],
				name='bottom_edge',
			)
