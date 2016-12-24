from django.shortcuts import render, get_object_or_404
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