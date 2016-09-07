#	_________________
#	|				|
#	|				|
#	|				|
#	|				|
#	|_______________|
#	|		|		|
#	|_______|		|
#	|		|		|
#	|_______|		|
#	|_______|_______|


plan = {
	"x_length": 120,
	"y_length": 200,
	"height": 50,	# Total height, including the base
	"thickness": 6,
	"compartments": [
		{
			"level": 1,	# useful for debugging
			"div_orientation": "x", #  'x' means that interior dividers are parallel to the x axis.
			"x_length": 108,
			"y_length": 188,
			"compartments": [
				{
					"level": 2,
					"div_orientation": "y",
					"x_length": 108,
					"y_length": 91,
					"compartments": [
						{
							"level": 3,
							"div_orientation": "x",
							"x_length": 51,
							"y_length": 91,
							"compartments": [
								{
									"level": 4,
									"div_orientation": None,
									"x_length": 51,
									"y_length": 43,
									"compartments": []
								},
								{
									"level": 4,
									"div_orientation": None,
									"x_length": 51,
									"y_length": 18,
									"compartments": []
								},
								{
									"level": 4,
									"div_orientation": None,
									"x_length": 51,
									"y_length": 18,
									"compartments": []
								}
							]
						},
						{
							"level": 3,
							"div_orientation": None,
							"x_length": 51,
							"y_length": 91,
							"compartments": []
						}
					]
				},
				{
					"level": 2,
					"div_orientation": None,
					"x_length": 108,
					"y_length": 91,
					"compartments": []
				}
			]

		}
	]
}