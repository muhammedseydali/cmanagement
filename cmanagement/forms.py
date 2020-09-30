from django import forms
from django.forms import widgets
from cmanagement.models import category
from cmanagement.models import items,vendor,locationn,inventory

class catform(forms.ModelForm):
	class Meta:
		model=category
		fields='__all__'

class itemform(forms.ModelForm):
	class Meta:
		model=items
		fields='__all__'

class vendorform(forms.ModelForm):
		name = forms.CharField()
		compony=forms.CharField()
		email=forms.EmailField()
		phone=forms.CharField()
		remark=forms.CharField()
		description=forms.CharField(widget=forms.Textarea)
		class Meta:
			model=vendor
			fields='__all__'

class locationform(forms.ModelForm):
	class Meta:
		model=locationn
		fields='__all__'


class inventoryform(forms.ModelForm):
	class Meta:
		model=inventory
		fields='__all__'					

	     