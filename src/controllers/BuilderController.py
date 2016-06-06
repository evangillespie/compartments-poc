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

		DividerCollectionController.add_rectangular_divider_to_collection(
			name="base",
			collection=collection,
			x_length=plan['x_length'],
			y_length=plan['y_length'],
			thickness=6
		)

		print collection
		for d in DividerCollectionController.get_all_dividers_in_collection(collection):
			print d

		# @TODO: break the plan down into dividers
