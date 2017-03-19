from django import forms

class FeedbackForm(forms.Form):
    """
        User feedback
    """
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)


class BuyForm(forms.Form):
    """
        User informations when buy
    """
    email = forms.EmailField()
    phone = forms.CharField(max_length=15)
