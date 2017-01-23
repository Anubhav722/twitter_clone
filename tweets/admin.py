from django.contrib import admin

# Register your models here.
from .models import Tweet
from .forms import TweetModelForm

class TweetModelForm(admin.ModelAdmin):
    form = TweetModelForm
    #
    # class Meta:
    #     model = Tweet

admin.site.register(Tweet, TweetModelForm)