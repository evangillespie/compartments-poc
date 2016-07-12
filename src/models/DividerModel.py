#!/usr/bin/env python

"""
	Model for the Divider  object

	A Divider is just a representation of the piece of wood
"""

__author__ = "Evan Gillespie"


from ..config import JOINERY_TAB_HEIGHT_PROPORTION, JOINERY_TAB_OFFSET_FROM_EDGE
import logging


logger = logging.getLogger(__name__)


class DividerModel(object):


	def __init__(self, *args, **kwargs):
		pass


	"""
	Create a simple rectangular Divider

	:param x_length: x_length of the rectangle
	:param y_length: y_length of the rectangle
	:param thickness: thickness of the wood the divider will be made from

	:return: a Divider object representing a simple rectangle
	"""
	@classmethod
	def create_rectangular_divider(cls, x_length, y_length, thickness, name=None, *args, **kwargs):
		if not name:
			logger.error("Trying to create a divider without a name. That'll be trouble")

		div = Divider(name=name, x_length=x_length, y_length=y_length, thickness=thickness, *args, **kwargs)

		logger.debug("Creating Divider(%s)" % name)

		return div


	"""
	Add male joinery to the left and right edges of a divider

	:param divider: the divider to add joinery to
	:param width: how far do the male joints extend?

	:return:
	"""
	@classmethod
	def add_male_joinery_to_divider_sides(cls, divider, depth):
		x_length = divider.x_length
		y_length = divider.y_length
		tab_h = y_length * JOINERY_TAB_HEIGHT_PROPORTION

		left_join = {
			'type': 'positive',
			# points are sort of arbitrary
			'points': [
				(0, 0),
				(0, JOINERY_TAB_OFFSET_FROM_EDGE),
				(-depth, JOINERY_TAB_OFFSET_FROM_EDGE),
				(-depth, tab_h + JOINERY_TAB_OFFSET_FROM_EDGE),
				(0, tab_h + JOINERY_TAB_OFFSET_FROM_EDGE),
				(0, y_length - tab_h - JOINERY_TAB_OFFSET_FROM_EDGE),
				(-depth, y_length - tab_h - JOINERY_TAB_OFFSET_FROM_EDGE),
				(-depth, y_length - JOINERY_TAB_OFFSET_FROM_EDGE),
				(0, y_length - JOINERY_TAB_OFFSET_FROM_EDGE),
				(0, y_length)
			]
		}

		right_join = {
			'type': 'positive',
			'points': [
				(x_length, y_length),
				(x_length, y_length - JOINERY_TAB_OFFSET_FROM_EDGE),
				(x_length + depth, y_length - JOINERY_TAB_OFFSET_FROM_EDGE),
				(x_length + depth, y_length - tab_h - JOINERY_TAB_OFFSET_FROM_EDGE),
				(x_length, y_length - tab_h - JOINERY_TAB_OFFSET_FROM_EDGE),
				(x_length, tab_h + JOINERY_TAB_OFFSET_FROM_EDGE),
				(x_length + depth, tab_h + JOINERY_TAB_OFFSET_FROM_EDGE),
				(x_length + depth, JOINERY_TAB_OFFSET_FROM_EDGE),
				(x_length, JOINERY_TAB_OFFSET_FROM_EDGE),
				(x_length, 0)
			]
		}

		divider.joinery.append(left_join)
		divider.joinery.append(right_join)


	"""
	Add female joinery to a divider, starting at a certain distance from the edge

	:param divider: the divider to add female joinery to
	:param offset: distance from the edge of the divider to the start of the female joint (socket)
	:param width: width of the female joint (socket)

	:return:
	"""
	@classmethod
	def add_female_joinery_to_divider(cls, divider, offset, width):
		y_length = divider.y_length
		tab_h = y_length * JOINERY_TAB_HEIGHT_PROPORTION
		joint1 = {
			'type': 'negative',
			'points': [
				(offset, 0 + JOINERY_TAB_OFFSET_FROM_EDGE),
				(offset, tab_h + JOINERY_TAB_OFFSET_FROM_EDGE),
				(offset + width, tab_h + JOINERY_TAB_OFFSET_FROM_EDGE),
				(offset + width, 0 + JOINERY_TAB_OFFSET_FROM_EDGE)
			]
		}
		joint2 = {
			'type': 'negative',
			'points': [
				(offset, y_length - tab_h - JOINERY_TAB_OFFSET_FROM_EDGE),
				(offset, y_length - JOINERY_TAB_OFFSET_FROM_EDGE),
				(offset + width, y_length - JOINERY_TAB_OFFSET_FROM_EDGE),
				(offset + width, y_length - tab_h - JOINERY_TAB_OFFSET_FROM_EDGE)
			]
		}

		divider.joinery.append(joint1)
		divider.joinery.append(joint2)


	"""
	Return a dict of layers of points that represents the divider with all joinery

	:param divider: the divider to export as points
	
	:return: Dictionary where each value is a list of points making up a layer
			{
				'outline': [(0, 0), (0, 10), ...],
				'1': [(1, 3), (1, 5), ...]
			}
	"""
	@classmethod
	def convert_divider_to_points(cls, divider):
		ret = {
			'cuts': [],
			'outline': None
		}
		
		outline = divider.points
		for j in divider.joinery:
			if j['type'] == 'positive':
				outline = cls.update_divider_points_with_positive_joinery(
					outline,
					j['points']
				)

			elif j['type'] == 'negative':
				ret['cuts'].append(j['points'])

		ret['outline'] = outline
		return ret


	"""
	Update a set of outline points to include a set of joinery points

	:param divider_points: the original list of divider points
	:param joinery_points: joinery points to add somewhere

	:return: new set of divider points
	"""
	@classmethod
	def update_divider_points_with_positive_joinery(cls, divider_points, joinery_points):
		start = joinery_points[0]
		end = joinery_points[-1]

		for i in range(len(divider_points)):
			if start == divider_points[i]:
				for j in range(i, len(divider_points)):
					if end == divider_points[j]:
						return divider_points[:i] + joinery_points + divider_points[j+1:]

		return divider_points


# -----------------------------------------------
# ------------- Data Model Below ----------------
# -----------------------------------------------


class Divider():


	def __init__(self, name=None, x_length=None, y_length=None, thickness=None, *args, **kwargs):
		self.name = name
		self.x_length = x_length
		self.y_length = y_length
		self.thickness = thickness
		self.points = [(0, 0), (0, y_length), (x_length, y_length), (x_length, 0)]

		# a list of joinery elements to be added or subtracted from the base rectangle
		self.joinery = []


	"""
	unabiguous string description of the divider
	"""
	def __repr__(self):
		ret = "Divider (%s)[%s,%s]" % (self.name, self.x_length, self.y_length)
		return ret


	"""
	basic string description of the divider
	"""
	def __str__(self):
		if self.name:
			return "Divider (%s)" % (self.name)
		else:
			return "Divider (--)"

