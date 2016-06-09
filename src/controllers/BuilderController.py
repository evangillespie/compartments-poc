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

		"""
		read a compartments list and save dividers and relations or that compartment
		"""
		# @TODO: add name of left, top, right, bottom dividers to arguments for referencing
		def validate_and_interpret_compartments(compartments):
			# if there are no compartments, this is the bottom level
			if not compartments:
				return

			for c in compartments:
				validate_and_interpret_compartments(c['compartments'])



		DividerCollectionController.add_rectangular_divider_to_collection(
			collection=collection,
			x_length=plan['x_length'],
			y_length=plan['y_length'],
			thickness=plan['thickness' ],
			name="BASE"
		)

		DividerCollectionController.add_rectangular_divider_to_collection(
			collection=collection,
			x_length=100,
			y_length=200,
			thickness=plan['thickness' ]
		)

		validate_and_interpret_compartments(plan['compartments'])
