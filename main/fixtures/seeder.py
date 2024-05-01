#!/usr/bin/env python
import os
import sys
import logging
import traceback
import django
from django.db import transaction

# Call django from python standalone
sys.path.append('./')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'moviedb.settings')
django.setup()

import json
from main.models import Movie, Genre, MPAA_Rating, MPAA_Rating_Type

jsonFile = open('main/fixtures/movies.json')
data = json.load(jsonFile)
bulkData = []
print ('Seeding start')

try:
    with transaction.atomic():
        # Iterating through the json list
        for movie in data:
            mpaaRatingType, isRatingTypeCreated = MPAA_Rating_Type.objects.get_or_create(type=movie['mpaaRating']['type'])
            mpaaRating, isRatingCreated = MPAA_Rating.objects.get_or_create(type=mpaaRatingType, label=movie['mpaaRating']['label'])

            body = {
                'id': movie['id'],
                'name': movie['name'],
                'description': movie['description'],
                # imgPath: models.CharField(max_length=200)
                'imgPath': movie['imgPath'],
                'duration': movie['duration'],
                'language': movie['language'],
                'mpaaRating': mpaaRating,
                'userRating': movie['userRating'],
            }

            newMovie = Movie.objects.create(**body)

            for movieGenre in movie['genre']:
                genre, isGenreCreated = Genre.objects.get_or_create(name=movieGenre)
                newMovie.genre.add(genre)

except:
    logging.error(traceback.format_exc())
    print('Error, See log for detail')

jsonFile.close()

print('Process done!')
