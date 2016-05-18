#!/usr/bin/env python

"""
	for building a plan into dividers.
"""

__author__ = "Evan Gillespie"


from Controller import Controller
from DividerCollectionController import DividerCollectionController


class BuilderController(Controller):


	def __init__(self):
		pass


	"""
	turn an organizer plan into a divider collection.
	This is a real meaty function

	:param plan: the plan to be turned

	:return: a DividerCollection object
	"""
	@classmethod
	def build_divider_collection_from_plan(cls, plan):
		collection = DividerCollectionController.create_empty_divider_collection()

		print collection