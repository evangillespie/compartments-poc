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
		|_______|		|
		|		|		|
		|_______|		|
		|_______|_______|
		'''

		return {
			'x_length': 120,
			'y_length': 200,
			'height': 50,
			'thickness': 6,	# Total heigth, including the base
			'compartments': [
				{
					'level': 1,	# useful for debugging
					#  y means that interior dividers are parallel to the y axis.
					'div_orientation': 'x',
					'x_length': 108,
					'y_length': 188,
					'compartments': [
						{
							'level': 2,
							'div_orientation': 'y',
							'x_length': 108,
							'y_length': 91,
							'compartments': [
								{
									'level': 3,
									'div_orientation': 'x',
									'x_length': 51,
									'y_length': 91,
									'compartments': [
										{
											'level': 4,
											'div_orientation': None,
											'x_length': 51,
											'y_length': 43,
											'compartments': []
										},
										{
											'level': 4,
											'div_orientation': None,
											'x_length': 51,
											'y_length': 18,
											'compartments': []
										},
										{
											'level': 4,
											'div_orientation': None,
											'x_length': 51,
											'y_length': 18,
											'compartments': []
										}
									]
								},
								{
									'level': 3,
									'div_orientation': None,
									'x_length': 51,
									'y_length': 91,
									'compartments': []
								}
							]
						},
						{
							'level': 2,
							'div_orientation': None,
							'x_length': 108,
							'y_length': 91,
							'compartments': []
						}
					]

				}
			]
		}