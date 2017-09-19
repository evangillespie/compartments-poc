#!/usr/bin/env python

"""
	Model for the organizer plans as they come out of the user
	and before they are broken into dividers
"""

__author__ = "Evan Gillespie"


import sys
import logging
from importlib import import_module


logger = logging.getLogger(__name__)


class OrganizerPlanModel(object):


	def __init__(self):
		pass


	"""
	Return a sample plan for the proof of concept

	The real plans won't exist until there is a way for the user to create them
	Eventually, the plan model should get a lot more rubust than this dictionary

	:param plan_number: which plan should I return? they're numbered in the order they were created

	:return: json object containing all the data for a set of compartments
	"""
	@classmethod
	def get_sample_plan(cls, plan_number):

		try:
			sample_plan = import_module("src.sample_plans.sample_plan_" + str(plan_number))
			return sample_plan.plan
		except:
			logger.error("Can't import plan %s" % plan_number)
			sys.exit()
