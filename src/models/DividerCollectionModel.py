#!/usr/bin/env python

"""
	Model for the Divider Collection object

	A DividerCollection is just a group of Divider Objects
"""

__author__ = "Evan Gillespie"


import logging
from Model import Model

logger = logging.getLogger(__name__)


class DividerCollectionModel(object):


	def __init__(self, *args, **kwargs):
		pass

	"""
	Create a new, empty DividerCollection Object

	:return: a DividerCollection object containing no Divider objects
	"""
	@classmethod
	def create_empty_divider_collection(cls, *args, **kwargs):
		if 'id' in kwargs:
			id = kwargs['id']
		else:
			id = "Sample"

		logger.info("Creating new DividerCollection (%s)" % id)
		return DividerCollection(id)


	"""
	Add a new divider to the collection

	:param collection: the collection to add to
	:param divider: the divider to add

	:return: modified collection
	"""
	@classmethod
	def add_divider_to_collection(cls, collection, divider, *args, **kwargs):
		collection.add_divider_to_collection(divider)

		logger.debug("Adding Divider(%s) to DividerCollection(%s)" % (divider.name, collection.id))
		return collection


	"""
	Return all the dividers in the collection

	:param collection: the collection to fetch dividers from

	:return: list of all dividers in the collection
	"""
	@classmethod
	def get_all_dividers_in_collection(cls, collection):
		return collection.dividers


	"""
	Retreive a particular divider by name

	:param collection: the collection to get it from
	:param name: name of the Divider to get

	:return: Divider in the collection with the name. None if no name found
	"""
	@classmethod
	def get_divider_with_name_from_collection(cls, collection, name):
		for d in collection.dividers:
			if d.name == name:
				return d
		return None


# -----------------------------------------------
# ------------- Data Model Below ----------------
# -----------------------------------------------


class DividerCollection():


	def __init__(self, id, *args, **kwargs):
		self.id = id
		self.dividers = list()



	"""
	Add a new divider to this collection

	:param divider: the divider to be added
	"""
	def add_divider_to_collection(self, divider, *args, **kwargs):
		self.dividers.append(divider)


	"""
	unabiguous string description of the dividercollection
	"""
	def __repr__(self):
		ret = "DividerCollection (%s)[%s]" % (self.id, len(self.dividers))
		if len(self.dividers) > 0:
			ret = ret + " << %s >>" % ",".join([d.name for d in self.dividers])

		return ret


	"""
	basic string description of the divider
	"""
	def __str__(self):
		return "DividerCollection (%s)[%s]" % (self.id, len(self.dividers))

		