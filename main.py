import click


@click.command()
def hello_world():
	print "Hello, World"



@click.command()
def draw_dxf():
	print "Drawing..."
