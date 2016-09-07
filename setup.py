from setuptools import setup


setup(
	name = 'CompartmentsPOC',
	version='1.0',
	py_modules=[
		'main'
	],
	install_requires=[
		'Click',
		'ezdxf',
	],
	entry_points={
        'console_scripts':[
            'draw_dxf_from_sample_plan = main:draw_dxf_from_sample_plan',
        ]
	},
)
