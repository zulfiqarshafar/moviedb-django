from django.db import models

class MPAA_Rating_Type(models.Model):
    type = models.CharField(max_length=10)

    def __str__(self):
        return self.type

class MPAA_Rating(models.Model):
    type = models.ForeignKey(MPAA_Rating_Type, on_delete=models.CASCADE)
    label = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.type} - {self.label}"

class Genre(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Movie(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    imgPath = models.FileField(max_length=250, upload_to='assets/images/')
    duration = models.IntegerField()
    genre = models.ManyToManyField(Genre)
    language = models.CharField(max_length=50)
    mpaaRating = models.ForeignKey(MPAA_Rating, on_delete=models.CASCADE)
    userRating = models.CharField(max_length=3)

    def __str__(self):
        return self.name