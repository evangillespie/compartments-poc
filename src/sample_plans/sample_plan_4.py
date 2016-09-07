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

# TRANSPOSED!!!!


plan = {
	"y_length": 120,
	"x_length": 200,
	"height": 50,	# Total height, including the base
	"thickness": 6,
	"compartments": [
		{
			"level": 1,	# useful for debugging
			"div_orientation": "y", #  'y' means that interior dividers are parallel to the y ayis.
			"y_length": 108,
			"x_length": 188,
			"compartments": [
				{
					"level": 2,
					"div_orientation": "x",
					"y_length": 108,
					"x_length": 91,
					"compartments": [
						{
							"level": 3,
							"div_orientation": "y",
							"y_length": 51,
							"x_length": 91,
							"compartments": [
								{
									"level": 4,
									"div_orientation": None,
									"y_length": 51,
									"x_length": 43,
									"compartments": []
								},
								{
									"level": 4,
									"div_orientation": None,
									"y_length": 51,
									"x_length": 18,
									"compartments": []
								},
								{
									"level": 4,
									"div_orientation": None,
									"y_length": 51,
									"x_length": 18,
									"compartments": []
								}
							]
						},
						{
							"level": 3,
							"div_orientation": None,
							"y_length": 51,
							"x_length": 91,
							"compartments": []
						}
					]
				},
				{
					"level": 2,
					"div_orientation": None,
					"y_length": 108,
					"x_length": 91,
					"compartments": []
				}
			]

		}
	]
}