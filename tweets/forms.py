from django import forms

from .models import Tweet


from django.core.mail import send_mail

class TweetModelForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = [
            #'user',
            'content',
        ]

    # raising a ValidationError # this one gives directly on the field

    # def clean_content(self, *args, **kwargs):
    #     content = self.cleaned_data.get('content')
    #
    #     if content == 'abc':
    #         raise forms.ValidationError('Cannnot be ABC')
    #
    #     return content

class ContactForm(forms.Form):
    #name = forms.CharField()
    email = forms.CharField()
    subject = forms.CharField()
    message = forms.CharField(widget=forms.Textarea)

    def send_email(self):
        # send email using the self.cleaned_data dictionary
        send_mail(
            self.cleaned_data['subject'],
            self.cleaned_data['message'],
            self.cleaned_data.get('email', 'anubhavs286@gmail.com'),
            ['anubhavs722@gmail.com']
        )
