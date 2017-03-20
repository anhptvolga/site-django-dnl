from django import forms
from .models import Feedback


class FeedbackForm(forms.ModelForm):
    """
        User feedback
    """
    class Meta:
        model = Feedback
        fields = '__all__'


class BuyForm(forms.Form):
    """
        User informations when buy
    """
    email = forms.EmailField()
    phone = forms.CharField(max_length=15)
