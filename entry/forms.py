from django import forms
from .models import Entry

class EntryForm(forms.ModelForm):

	class Meta:
		model = Entry
		fields = ('Date',
			'Reactions_to_dogs',
			'Reactions_to_people',
			'Other_reactions',
			'Notes',
		)