from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):
    class Meta():
        model = Post 
        fields = ('author', 'title', 'text') # fields we want to be editable

        #connecting the fields to CSS classes through widgets
        widgets = {
            'title': forms.TextInput(attrs= {'class':'textinputclass'}),
            'text': forms.Textarea(attrs= {'class':'editable medium-editor-textarea postcontent'}),
        }

class CommentForm(forms.ModelForm):
    class Meta():
        model = Comment
        fields = ('author', 'text')

        widgets = {
            'author': forms.TextInput(attrs= {'class':'textinputclass'}),
            'text': forms.Textarea(attrs= {'class':'editable medium-editor-textarea'}),
        }