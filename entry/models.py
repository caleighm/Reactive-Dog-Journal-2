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

	def __str__(self):
		return str(self.Reactions_to_dogs + self.Reactions_to_people 
			+ self.Other_reactions)

	def get_total(self):
		return self.Reactions_to_dogs + self.Reactions_to_people + self.Other_reactions

	def get_data(self):
		data = {'date': [], 'total': [], 'dogs': [], 'ppl': [], 'oth':[]}

		entries = Entry.objects.all()

		for entry in entries:
			data['date'] = entry.Date
			data['total'] = entry.get_total()
			data['dogs'] = entry.Reactions_to_dogs
			data['ppl'] = entry.Reactions_to_people
			data['oth'] = entry.Other_reactions

		return data