from setuptools import setup


setup(
	name = 'CompartmentsPOC',
	version='1.0',
	py_modules=[
		'main'
	],
	install_requires=[
		'Click'
	],
	entry_points={
        'console_scripts':[
            'hello = main:hello_world',
            'draw_dxf = main:draw_dxf'
        ]
	},
)
