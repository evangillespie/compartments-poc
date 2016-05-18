from src.controllers.OrganizerPlanController import OrganizerPlanController
from src.controllers.BuilderController import BuilderController
import click


@click.command()
def hello_world():
	print "Hello, World"



@click.command()
def draw_dxf_from_sample_plan():
	"""
		take a sample plan object and turn it into a dxf drawing
		of a bunch of dividers
	"""

	plan = OrganizerPlanController.get_sample_plan()

	BuilderController.build_divider_collection_from_plan(plan)
