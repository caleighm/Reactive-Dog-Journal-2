from django.shortcuts import render
from datetime import date
from .models import Entry

def entry_list(request):
	entries = Entry.objects.filter(Date__lte=date.today()).order_by('Date')
	return render(request, 'entry/entry_list.html', {'entries': entries})