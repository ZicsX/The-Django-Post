from django import forms
from ckeditor.widgets import CKEditorWidget
from .models import Blog

class BlogForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget())  # Use the CKEditorWidget for the content field

    class Meta:
        model = Blog
        fields = ['title', 'content']
