#!/usr/bin/env python

"""
	Model for the Divider Collection object

	A DividerCollection is just a group of Divider Objects
"""

__author__ = "Evan Gillespie"


from Model import Model


class DividerCollectionModel(Model):


	def __init__(self):
		pass

	"""
	Create a new, empty DividerCollection Object

	:return: a DividerCollection object containing no Divider objects
	"""
	@classmethod
	def create_empty_divider_collection(cls):
		return DividerCollection()


# -----------------------------------------------
# ------------- Data Model Below ----------------
# -----------------------------------------------


class DividerCollection():


	def __init__(self, *args, **kwargs):
		self.dividers = list()


	"""
	Add a new divider to this collection
	"""
	def add_divider_to_collection(self):
		pass