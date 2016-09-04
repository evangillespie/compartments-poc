#!/usr/bin/env python

"""
	Controller for organizer plans
"""

__author__ = "Evan Gillespie"


from ..models.OrganizerPlanModel import OrganizerPlanModel


class OrganizerPlanController(object):


	def __init__(self):
		pass


	"""
	Return a sample plan for the proof of concept

	The real plans won't exist until there is a way for the user to create them
	"""
	@classmethod
	def get_sample_plan(cls):
		return OrganizerPlanModel.get_sample_plan()


	"""
	return a very simple sample plan for debugging
	"""
	@classmethod
	def get_simple_sample_plan(cls):
		return OrganizerPlanModel.get_simple_sample_plan()
