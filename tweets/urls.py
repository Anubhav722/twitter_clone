from django.conf.urls import url
from .views import TweetDetailView, TweetListView, TweetCreateView #tweet_detail_view, tweet_list_view


from django.views.generic.base import RedirectView
# These are base views
from .views import MyView, HomePageView, TweetCounterRedirectView, ContactView
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
]