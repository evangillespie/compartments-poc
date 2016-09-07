#	_________________
#	|				|
#	|_______________|
#	|	|	|	|	|
#	|	|	|	|	|
#	|	|	|	|	|
#	|	|	|	|	|
#	|___|___|___|___|
#	|		|		|
#	|_______|_______|


plan = {
	"x_length": 400,
	"y_length": 500,
	"height": 70,	# Total height, including the base
	"thickness": 5,
	"compartments": [
		{
			"level": 1,
			"div_orientation": "x",
			"x_length": 390,
			"y_length": 490,
			"compartments": [
				{
					"level": 2,
					"div_orientation": "y",
					"x_length": 390,
					"y_length": 80,
					"compartments": [
						{
							"level": 3,
							"div_orientation": "x",
							"x_length": 200,
							"y_length": 80,
							"compartments": []
						},
						{
							"level": 3,
							"div_orientation": "x",
							"x_length": 185,
							"y_length": 80,
							"compartments": []
						}
					]
				},
				{
					"level": 2,
					"div_orientation": "y",
					"x_length": 390,
					"y_length": 300,
					"compartments": [
						{
							"level": 3,
							"div_orientation": "x",
							"x_length": 75,
							"y_length": 300,
							"compartments": []
						},
						{
							"level": 3,
							"div_orientation": "x",
							"x_length": 100,
							"y_length": 300,
							"compartments": []
						},
						{
							"level": 3,
							"div_orientation": "x",
							"x_length": 100,
							"y_length": 300,
							"compartments": []
						},
						{
							"level": 3,
							"div_orientation": "x",
							"x_length": 100,
							"y_length": 300,
							"compartments": []
						}
					]
				},
				{
					"level": 2,
					"div_orientation": "y",
					"x_length": 390,
					"y_length": 100,
					"compartments": [
					]
				}
			]
		}
	]
}