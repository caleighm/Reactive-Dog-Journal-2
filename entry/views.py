from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.http import JsonResponse
from datetime import date
from .models import Entry
from .forms import EntryForm

def entry_list(request):
	entries = Entry.objects.filter(Date__lte=date.today()).order_by('Date')
	return render(request, 'entry/entry_list.html', {'entries': entries})

def entry_detail(request, pk):
	entry = get_object_or_404(Entry, pk=pk)
	return render(request, 'entry/entry_detail.html', {'entry': entry})

def entry_new(request):
	if request.method == "POST":
		form = EntryForm(request.POST)
		if form.is_valid():
			entry = form.save(commit=False)
			entry.author = request.user
			entry.Last_modified = timezone.now()
			entry.save()
			return redirect('entry_detail', pk=entry.pk)
	else:
		form = EntryForm()
	return render(request, 'entry/entry_edit.html', {'form': form})

def entry_edit(request, pk):
	entry = get_object_or_404(Entry, pk=pk)

	if request.method == "POST":
		form = EntryForm(request.POST, instance=entry)
		if form.is_valid():
			entry = form.save(commit=False)
			entry.author = request.user
			entry.Last_modified = timezone.now()
			entry.save()
			return redirect('entry_detail', pk=entry.pk)
	else:
		form = EntryForm(instance=entry)

	return render(request, 'entry/entry_edit.html', {'form': form})

def entry_remove(request, pk):
	entry = get_object_or_404(Entry, pk=pk)
	entry.delete()
	return redirect('entry_list')

def entry_report(request, chartID = 'chartID', chart_type = 'line', chart_height = 500):
	data = Entry.allData()

	chart = {"renderTo": chartID, "type": chart_type, "height": chart_height}  
	title = {"text": 'Reaction History'}
	xAxis = {"title": {"text": 'Date'}, "type": 'datetime',"dateTimeLabelFormats": {"month": '%e. %b', "year": '%b'}}
	yAxis = {"title": {"text": 'Reactions'}}
	series = [
		{"name": 'Total Reactions', "data": data['total']}, 
		{"name": 'Reactions to Dogs', "data": data['dogs']},
		{"name": 'Reactions to People', "data": data['ppl']},
		{"name": 'Other Reactions', "data": data['oth']}
	]

	return render(request, 'entry/entry_report.html', {'chartID': chartID, 'chart': chart,
													'series': series, 'title': title, 
													'xAxis': xAxis, 'yAxis': yAxis})