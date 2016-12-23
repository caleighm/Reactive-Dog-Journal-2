from django.db import models
from django.utils import timezone
from datetime import date

class Entry(models.Model):
	author = models.ForeignKey('auth.User')
	Date = models.DateField(default=date.today())
	Reactions_to_dogs = models.SmallIntegerField()
	Reactions_to_people = models.SmallIntegerField()
	Other_reactions = models.SmallIntegerField()
	Notes = models.TextField()
	Last_modified = models.DateTimeField(blank=True, null=True)

	def saveEntry(self):
		self.Last_modified = timezone.now()
		self.save()

	# Access entry details
	def __notes__(self):
		return self.Notes
	
	def __numDogReactions__(self):
		return self.Reactions_to_dogs

	def __numPplReactions__(self):
		return self.Reactions_to_people

	def __numOthReactions__(self):
		return self.Other_reactions