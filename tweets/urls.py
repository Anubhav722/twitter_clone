from django.conf.urls import url
from .views import  TweetDetailView, TweetListView, TweetCreateView, TweetUpdateView, TweetDeleteView #tweet_detail_view, tweet_list_view,

from django.views.generic.base import RedirectView

urlpatterns = [
    #url(r'^$', tweet_list_view, name='list'),
    #url(r'^1/$', tweet_detail_view, name='detail'),

    url(r'^$', RedirectView.as_view(url="/")), # this is a nice way to redirect
    url(r'^search/$', TweetListView.as_view() , name='list'),
    url(r'^(?P<pk>\d+)/$', TweetDetailView.as_view() , name='detail'),
    url(r'^create/$', TweetCreateView.as_view() , name='create'),
    url(r'^(?P<pk>\d+)/update/$', TweetUpdateView.as_view(), name='update'),
    url(r'^(?P<pk>\d+)/delete/$', TweetDeleteView.as_view(), name='delete'),
]