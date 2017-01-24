from django.shortcuts import render
from django.views.generic import DetailView, ListView, CreateView

from .forms import TweetModelForm
from .models import Tweet

# importing login mixin here
from django.contrib.auth.mixins import LoginRequiredMixin
from .mixins import FormUserNeededMixin
# Create your views here.

# learn about this CreateView
class TweetCreateView(FormUserNeededMixin, CreateView):
    form_class = TweetModelForm
    template_name = 'tweets/create_view.html'
    success_url = '/tweet/'
    login_url = '/admin/'

    # def form_valid(self, form):
    #     #form.send_email()
    #     form.instance.user = self.request.user
    #     return super(TweetCreateView, self).form_valid(form)

#learn about DetailView
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
        #print (context)
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


