import logging
import click
from src.controllers.OrganizerPlanController import OrganizerPlanController
from src.controllers.BuilderController import BuilderController

"""
	take a sample plan object and turn it into a dxf drawing
	of a bunch of dividers

	:param plan_number: which plan should I use? They're in the sample_plans folder.
"""
@click.command()
@click.option('--plan-number', prompt=True)
def draw_dxf_from_sample_plan(plan_number):

	logging.basicConfig(
		filename='app.log',
		filemode='w',
		format="%(asctime)-20s %(levelname)s:%(name)s :: %(message)s",
		datefmt='%Y-%M-%d %H:%M:%S',
		level=logging.DEBUG,
	)

	plan = OrganizerPlanController.get_sample_plan(plan_number)
	
	BuilderController.build_divider_collection_from_plan(plan)


if __name__ == "__main__":
	draw_dxf_from_sample_plan()