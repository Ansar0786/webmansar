from django.db import models

# Create your models here.
# import the standard Django Model
# from built-in library
from django.db import models


# declare a new model with a name "GeeksModel"
class gateModel(models.Model):
    # fields of the model
    moviename = models.CharField(max_length=100)
    poster = models.ImageField(upload_to="media")
    releasedate = models.DateField(auto_created="")
    shortdesc = models.TextField(max_length=100)
    longdesc = models.TextField(max_length=300)
    publishername = models.CharField(max_length=50)


    # renames the instances of the model

    def __str__(self):
        return (self.moviename, self.poster, self.releasedate, self.shortdesc, self.longdesc, self.publishername)

    class Meta:
        db_table = "image"