from django import forms
from annotation_app.models import Bill, Comment

class BillAddForm(forms.Form):
  text = forms.CharField(label='text')

class BillEditForm(BillAddForm):
  id = forms.HiddenInput()

class AnnotationAddForm(forms.Form):
  bill_id = forms.HiddenInput()
  text = forms.CharField(label='text')

class AnnotationEditForm(AnnotationAddForm):
  id = forms.HiddenInput()

class CommentAddForm(forms.Form):
  annotation_id = forms.HiddenInput()
  text = forms.CharField(label='text')

class CommentEditForm(CommentAddForm):
  id = forms.HiddenInput()
