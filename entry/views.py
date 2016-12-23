from django.shortcuts import render
from datetime import date

def entry_list(request):
	return render(request, 'entry/entry_list.html', {})