#!/usr/bin/env python

"""
	Model for the organizer plans as they come out of the user
	and before they are broken into dividers
"""

__author__ = "Evan Gillespie"


class OrganizerPlanModel(object):


	def __init__(self):
		pass


	"""
	Return a sample plan for the proof of concept

	The real plans won't exist until there is a way for the user to create them
	Eventually, the plan model should get a lot more rubust than this dictionary
	"""
	@classmethod
	def get_sample_plan(cls):
		'''
		_________________
		|				|
		|				|
		|				|
		|				|
		|_______________|
		|		|		|
		|		|		|
		|		|		|
		|		|		|
		|_______|_______|
		'''

		return {
			'x_length': 120,
			'y_length': 200,
			'height': 50,
			'thickness': 6,	# Total heigth, including the base
			'compartments': [
				{
					#  y means that interior dividers are parallel to the x axis. Useful for interior compartments
					'orientation': 'y',
					'length': 102,
					'compartments': [
						{
							'orientation': 'x',
							'length': 91,
							'compartments': [
								{
									'orientation': None,
									'length': 48,
									'compartments': []
								},
								{
									'orientation': None,
									'length': 48,
									'compartments': []
								}
							]
						},
						{
							'orientation': None,
							'length': 91,
							'compartments': []
						}
					]

				}
			]
		}