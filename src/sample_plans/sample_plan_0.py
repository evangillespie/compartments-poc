#	_________________
#	|				|
#	|				|
#	|				|
#	|				|
#	|_______________|
#	|				|
#	|		 		|
#	|		 		|
#	|		 		|
#	|_______________|

plan = {
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
					'compartments': []
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