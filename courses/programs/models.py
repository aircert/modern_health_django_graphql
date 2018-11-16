from django.db import models


from enum import Enum

class ProgramCategoryChoice(Enum):   # A subclass of Enum
    Finance = "Finance"
    Emotions = "Emotions"
    Physical = "Physical"
    Life = "Life"

class Page(models.Model):
    # use models.URLField()
    name = models.CharField(max_length=255, blank=False, unique=False)
    complete = models.BooleanField(default=False)
    audio = models.URLField()
    video = models.URLField()
    article = models.URLField()
    question = models.URLField()
    form = models.URLField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Return a human readable representation of the model instance."""
        return "{}".format(self.name) 

class Week(models.Model):
    name = models.CharField(max_length=255, blank=False, unique=False)
    pages = models.ManyToManyField(Page)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    # complete = models.BooleanField(default=False)

    def __str__(self):
        """Return a human readable representation of the model instance."""
        return "{}".format(self.name)

class Program(models.Model):
    """This class represents the bucketlist model."""
    name = models.CharField(max_length=255, blank=False, unique=True)
    description = models.TextField()
    image = models.CharField(max_length=255, blank=False, unique=False)
    weeks = models.ManyToManyField(Week, blank=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    progress = models.IntegerField(db_column='progress')
    # category = models.CharField(
    #     max_length=3,
    #     choices=[(tag, tag.value) for tag in ProgramCategoryChoice],
    #     default=None)

    def __str__(self):
        """Return a human readable representation of the model instance."""
        return "{}".format(self.name)
