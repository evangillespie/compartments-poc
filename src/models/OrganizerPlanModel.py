#!/usr/bin/env python

"""
	Model for the organizer plans as they come out of the user
	and before they are broken into dividers
"""

__author__ = "Evan Gillespie"


class OrganizerPlanModel(object):


	def __init__(self):
		pass


	@classmethod
	def get_sample_plan(cls):
		'''
		Return a sample plan for the proof of concept

		The real plans won't exist until there is a way for the user to create them
		Eventually, the plan model should get a lot more rubust than this dictionary
		'''
		return {
			'width': 120,
			'length': 200,
			'height': 15,
			'thickness': 6,
			'compartments': [
				# @TODO: how do i do this?
			]
		}