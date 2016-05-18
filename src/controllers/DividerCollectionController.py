#!/usr/bin/env python

"""
	for controlling DividerCollection objects
"""

__author__ = "Evan Gillespie"


from Controller import Controller
from ..models.DividerCollectionModel import DividerCollectionModel


class DividerCollectionController(Controller):


	def __init__(self):
		pass


	"""
	Create a new, empty DividerCollection Object

	:return: a DividerCollection object containing no Divider objects
	"""
	@classmethod
	def create_empty_divider_collection(cls):
		return DividerCollectionModel.create_empty_divider_collection()