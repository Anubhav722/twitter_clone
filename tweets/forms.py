from django import forms

from .models import Tweet

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