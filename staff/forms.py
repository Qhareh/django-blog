from email import message
from socket import fromshare
from django import forms

class ReplyFeedbackForm(forms.Form):
    subject = forms.CharField(label="Subject", max_length=255)
    message = forms.CharField(widget=forms.Textarea)