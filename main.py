
import logging
import click
from src.controllers.OrganizerPlanController import OrganizerPlanController
from src.controllers.BuilderController import BuilderController


@click.command()
def hello_world():
	print "Hello, World"



"""
	take a sample plan object and turn it into a dxf drawing
	of a bunch of dividers
"""
@click.command()
def draw_dxf_from_sample_plan():

	logging.basicConfig(
		filename='app.log',
		filemode='w',
		format="%(asctime)-20s %(levelname)s:%(name)s :: %(message)s",
		datefmt='%Y-%M-%d %H:%M:%S',
		level=logging.DEBUG,
	)

	plan = OrganizerPlanController.get_sample_plan()
	# plan = OrganizerPlanController.get_simple_sample_plan()
	
	BuilderController.build_divider_collection_from_plan(plan)
