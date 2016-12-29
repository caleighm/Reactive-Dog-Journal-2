from django.db import models
from django.core.urlresolvers import reverse
from django.utils import timezone
from datetime import date, datetime
import calendar

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

	def getTotal(self):
		return self.Reactions_to_dogs + self.Reactions_to_people + self.Other_reactions

	def localToUTC(self):
		midnight = datetime.combine(self.Date, datetime.min.time())
		return calendar.timegm(midnight.utctimetuple()) * 1000.0 + midnight.microsecond

	def allData():
		entries = Entry.objects.filter(Date__lte=date.today()).order_by('Date')
		data = {'total': [], 'dogs': [], 'ppl': [], 'oth': []}

		for entry in entries:
			UTCtime = entry.localToUTC()
			data['total'].append({'x':UTCtime, 'y':entry.getTotal(), 'notes':entry.Notes[:50] + "..."})
			data['dogs'].append({'x':UTCtime, 'y':entry.Reactions_to_dogs, 'notes':""})
			data['ppl'].append({'x':UTCtime, 'y':entry.Reactions_to_people, 'notes':""})
			data['oth'].append({'x':UTCtime, 'y':entry.Other_reactions, 'notes':""})

		return data