from django import forms
from .models import Comment
from django.urls import reverse, reverse_lazy

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'comment',)
        success_url = reverse_lazy('home')