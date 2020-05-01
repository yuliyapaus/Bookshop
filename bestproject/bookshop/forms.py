from django import forms
from bookshop.models import Comment

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['text']
        widget ={'text':
                forms.Textarea(
                    attrs={'class':
                        'form-control'})}

