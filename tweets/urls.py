from django.conf.urls import url
from .views import TweetDetailView, TweetListView, TweetCreateView #tweet_detail_view, tweet_list_view

from .models import Tweet
from django.views.generic.base import RedirectView
# These are base views
from .views import MyView, HomePageView, TweetCounterRedirectView

# These are generic editing views
from .views import ContactView, TweetUpdateView, TweetDeleteView

# These are Generic date views
from django.views.generic.dates import ArchiveIndexView
from .views import TweetYearArchiveView

urlpatterns = [
    #url(r'^$', tweet_list_view, name='list'),
    #url(r'^1/$', tweet_detail_view, name='detail'),

    url(r'^$', TweetListView.as_view() , name='list'),
    url(r'^(?P<pk>\d+)/$', TweetDetailView.as_view() , name='detail'),
    url(r'^create/$', TweetCreateView.as_view() , name='create'),


    #added to this branch only
    url(r'^mine/$', MyView.as_view(), name='my-view'),
    url(r'^home/$', HomePageView.as_view(), name='home-page-view'),
    url(r'^counter/(?P<pk>[0-9]+)/$', TweetCounterRedirectView.as_view(), name='tweet-counter'),
    url(r'^go-to-django/$', RedirectView.as_view(url='https://djangoproject.com'), name='go-to-django'),
    url(r'^form/$', ContactView.as_view(), name='contact'),
    url(r'^update/(?P<pk>[0-9]+)/$', TweetUpdateView.as_view(), name='update'),
    url(r'^delete/(?P<pk>[0-9]+)/$', TweetDeleteView.as_view(), name='delete'),

    # Generic Date views
    url(r'^archive/$', ArchiveIndexView.as_view(model=Tweet, date_field="timestamp"),name="tweet_archive"),
    url(r'^(?P<year>[0-9]{4})/$', TweetYearArchiveView.as_view, name="tweet_year_archive"),
]