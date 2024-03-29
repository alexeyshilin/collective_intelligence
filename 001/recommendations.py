
critics={
	'Lisa Rose':
	{
		'Lady in the Water': 2.5
		,'Snakes on a Plane': 3.5
		,'Just My Luck': 3.0
		,'Superman Returns': 3.5
		,'You, Me and Dupree': 2.5
		,'The Night Listener': 3.0
	},
	'Gene Seymour':
	{
		'Lady in the Water': 3.0
		,'Snakes on a Plane': 3.5
		,'Just My Luck': 1.5
		,'Superman Returns': 5.0
		,'The Night Listener': 3.0
		,'You, Me and Dupree': 3.5
	},
	'Michael Phillips':
	{
		'Lady in the Water': 2.5
		,'Snakes on a Plane': 3.0
		,'Superman Returns': 3.5
		,'The Night Listener': 4.0
	},
	'Claudia Puig':
	{
		'Snakes on a Plane': 3.5
		,'Just My Luck': 3.0
		,'The Night Listener': 4.5
		,'Superman Returns': 4.0
		,'You, Me and Dupree': 2.5
	},
	'Mick LaSalle':
	{
		'Lady in the Water': 3.0
		,'Snakes on a Plane': 4.0
		,'Just My Luck': 2.0
		,'Superman Returns': 3.0
		,'The Night Listener': 3.0
		,'You, Me and Dupree': 2.0
	},
	'Jack Matthews':
	{
		'Lady in the Water': 3.0
		,'Snakes on a Plane': 4.0
		,'The Night Listener': 3.0
		,'Superman Returns': 5.0
		,'You, Me and Dupree': 3.5
	},
	'Toby':
	{
		'Snakes on a Plane':4.5
		,'You, Me and Dupree':1.0
		,'Superman Returns':4.0
	},

	'Some User 1':
	{
		'Movie 1':4.5
	},

	'Some User 2':
	{
		'Movie 2':4.5
	},
}

#> from recommendations import critics
#> critics['Lisa Rose']['Lady in the Water']
#> critics['Toby']['Snakes on a Plane']=4.5
#> critics['Toby']

def similarity_euclidian(data, username1, username2):

	matches = True if sum([ 1 for i in data[username1] if i in data[username2] ]) >0 else False
	if not matches:
		return 0

	#res = sum([ pow(data[username1][k]-data[username2][k], 2) for k in data[username1] if k in data[username2] ])
	res = sum([ pow(v-data[username2][k], 2) for (k, v) in data[username1].items() if k in data[username2] ])

	return 1/(1+res)

#> from importlib import reload
#> reload(recommendations)

#> import recommendations
#> reload(recommendations)

#> recommendations.similarity_euclidian(recommendations.critics, 'Lisa Rose', 'Gene Seymour')

def sim_distance(prefs,person1,person2):
	return similarity_euclidian(prefs,person1,person2)

#> recommendations.sim_distance(recommendations.critics, 'Lisa Rose','Gene Seymour')
