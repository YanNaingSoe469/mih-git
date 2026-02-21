from django import forms

from .models import Comment, Rating


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["message"]
        widgets = {
            "message": forms.Textarea(attrs={
                "class": "form-control",
                "placeholder": "Write your comment..."
            })
        }


class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ["count"]
        widgets = {
            "count": forms.NumberInput(attrs={
                "min": 1,
                "max": 5,
                "class": "form-control"
            })
        }
