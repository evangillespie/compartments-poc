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

	:param plan_number: which plan should I return? they're numbered in the order they were created

	:return: json object containing all the data for a set of compartments
	"""
	@classmethod
	def get_sample_plan(cls, plan_number):
		return OrganizerPlanModel.get_sample_plan(plan_number)
