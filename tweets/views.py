from django.shortcuts import render
from django.views.generic import DetailView, ListView, CreateView

from .forms import TweetModelForm
from .models import Tweet
from django.http import HttpResponse


# added in this branch
from django.views import View
from django.views.generic.base import TemplateView, RedirectView
from django.shortcuts import get_object_or_404

# Create your views here.



class TweetCreateView(CreateView):
    form_class = TweetModelForm
    template_name = 'tweets/create_view.html'
    success_url = '/tweet/create/'

    def form_valid(self, form):
        #form.send_email()
        form.instance.user = self.request.user
        return super(TweetCreateView, self).form_valid(form)

# These here are generic display views
class TweetDetailView(DetailView):
    queryset = Tweet.objects.all()
    # template_name = 'tweets/detail_view.html'
    # by default the name of the template will be tweet_detail.html
    # learn about get_object(self)

    # def get_object(self):
    #     print (self.kwargs) # here it is pk
    #     pk = self.kwargs.get('pk')
    #     return Tweet.objects.get(id=pk)

class TweetListView(ListView):
    queryset = Tweet.objects.all()
    # template_name = 'tweets/list_view.html'
    # by default the name of the template will be tweet_list.html
    def get_context_data(self, *args, **kwargs):
        context= super(TweetListView, self).get_context_data(*args, **kwargs)
        print (context)
        return context



# def tweet_create_view(request):
#     form = TweetModelForm(request.POST or None)
#     if form.is_valid():
#         instance = form.save(commit=False)
#         instance.user = request.user
#         instance.save()
#     context = {
#         "form": form
#     }
#     return render(request, 'tweets/create_view.html', context)


        # def tweet_detail_view(request, pk=None):
#     obj = Tweet.objects.get(id=pk)
#     context ={
#         'object':obj
#     }
#
#     return render(request, 'tweets/detail_view.html', context)
#
# def tweet_list_view(request):
#     queryset = Tweet.objects.all()
#     context = {
#         'object_list':queryset
#     }
#     return render(request, 'tweets/list_view.html', context)


# These have been added to understand the class based views

# These here are base views
class MyView(View):
    # diff typesof requests can be sent such as post, get, put, patch, delete etc.
    def get(self, request, *args, **kwargs):
        return HttpResponse('Hello, World!')

    # not working correctly. bcz post request requires some input
    def post(self, request, *args, **kwargs):
        print ('hi there')
        return render(request, 'tweets/my_view_test.html', {})

class HomePageView(TemplateView):
    template_name = "tweets/home.html"

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context['latest_articles'] = Tweet.objects.all()[:5]
        return context


class TweetCounterRedirectView(RedirectView):
# Whether the redirect should be permanent. The only difference here is the HTTP status code returned. If True, then the redirect will use status code 301. If False, then the redirect will use status code 302. By default, permanent is False.
    permanent = False
    query_string = True
    pattern_name = 'detail' # name of the url to redirect to.

    def get_redirect_url(self, *args, **kwargs):
        tweet = get_object_or_404(Tweet, pk=kwargs['pk'])
        #tweet.update_counter()
        return super(TweetCounterRedirectView, self).get_redirect_url(*args, **kwargs)

