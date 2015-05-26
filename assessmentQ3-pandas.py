import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.style.use('ggplot')

artists = pd.read_table("artists.tsv")
listens = pd.read_table("listens.tsv")
users = pd.read_table("users.tsv")

# rename artist_id to artist_seed to make merge possible
artists.columns = ['artist_seed', 'artist_name', 'genre']
listens_genres = pd.merge(listens, artists)
# now we merge this with users to get genres and users in same dataframe
users_genres = pd.merge(users, listens_genres)

# let's toss extraneous data
users_genres = users_genres.iloc[:,[1,2,7]]

# first let's extract genre/gender info (because that's easier)
genres_genders = users_genres.groupby(['genre', 'gender']).size()
genres_ages = users_genres.groupby(['genre', 'age']).size()

subplot_dims = (3,3)

print genres_genders

fig = plt.figure()
plt_genres=['Blues',"Children's",'Classical','Country','Electronic','Jazz','Pop','R&B','Rap']


for i in range(0, subplot_dims[0] * subplot_dims[1]):
	ax = fig.add_subplot(subplot_dims[0], subplot_dims[1], i+1)

	# Uncomment this block for ages
	# genres_ages[plt_genres[i]].plot(kind='area', ax=ax, title=plt_genres[i])
	# ax.set_yticklabels([])

	# Uncomment this block for genders
	plt_series = genres_genders[plt_genres[i]]
	plt_series.name = plt_genres[i]
	plt_series.plot(kind='pie', ax=ax)

plt.show()