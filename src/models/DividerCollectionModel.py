#!/usr/bin/env python

"""
	Model for the Divider Collection object

	A DividerCollection is just a group of Divider Objects
"""

__author__ = "Evan Gillespie"


import logging
import random
import string
from ..config import GENERATED_NAME_LENGTH

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

		logger.debug("Creating new DividerCollection (%s)" % id)
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
		collection.names.append(divider.name)

		logger.debug("Adding Divider(%s) to DividerCollection(%s)" % (divider.name, collection.id))
		return collection


	"""
	Add a compartment to the collection

	:param collection: the DividerCollection that will contain the Compartment
	:param compartment: the Compartment that we are adding to the DividerCollection

	:return:
	"""
	@classmethod
	def add_compartment_to_collection(cls, collection, compartment):
		collection.add_compartment_to_collection(compartment)


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


	"""
	register one compartment as the parent of another within a collection

	:param collection: the collection in question
	:param child_name: name of the child object
	:param parent_name: name of the parent object

	:return:
	"""
	@classmethod
	def register_child_parent_names(cls, collection, child_name, parent_name):
		collection.parents[child_name] = parent_name


	"""
	Return a new (unused) name for a Divider or Compartment in the collection

	:param collection:

	:return: (string) a new name
	"""
	@classmethod
	def get_new_name(cls, collection):
		choice = None
		while not choice or choice in collection.names:
			choice = ''.join(
							[
								random.choice(string.ascii_uppercase) \
									for _ in range(GENERATED_NAME_LENGTH)
							]
						)
		return choice


# -----------------------------------------------
# ------------- Data Model Below ----------------
# -----------------------------------------------


class DividerCollection():


	def __init__(self, id, *args, **kwargs):
		self.id = id
		self.dividers = []
		self.compartments = []

		self.names = []	#used divider or collection names

		self.parents = {} #record of the parent of each compartment

	"""
	Add a new divider to this collection

	:param divider: the divider to be added
	"""
	def add_divider_to_collection(self, divider, *args, **kwargs):
		self.dividers.append(divider)


	"""
	Add a new compartment to this collection

	:param compartment: the compartment to be added
	"""
	def add_compartment_to_collection(self, compartment, *args, **kwargs):
		self.compartments.append(compartment)


	"""
	unabiguous string description of the dividercollection
	"""
	def __repr__(self):
		ret = "DividerCollection (%s)[D:%s C:%s]" % (self.id, len(self.dividers), len(self.compartments))
		if len(self.dividers) > 0:
			ret = ret + " << %s >>" % ",".join([d.name for d in self.dividers])

		return ret


	"""
	basic string description of the divider
	"""
	def __str__(self):
		return "DividerCollection (%s)[D:%s C:%s]" % (self.id, len(self.dividers), len(self.compartments))

		