from django.shortcuts import render, get_object_or_404
from datetime import date
from .models import Entry

def entry_list(request):
	entries = Entry.objects.filter(Date__lte=date.today()).order_by('Date')
	return render(request, 'entry/entry_list.html', {'entries': entries})

def entry_detail(request, pk):
	entry = get_object_or_404(Entry, pk=pk)
	return render(request, 'entry/entry_detail.html', {'entry': entry})