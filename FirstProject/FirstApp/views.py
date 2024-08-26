from django.shortcuts import render
from django.views.generic import TemplateView,ListView
from FirstApp.models import Post

# Create your views here.
'''class MyHome(ListView):
    model = Post
    template_name = 'home.html'
    context_object_name = 'all_posts'''


def MyHome(request):
    context = {
        'all_posts': Post.objects.all()
    }
    return render(request, 'home.html',context)

def MyAbout(request):
    return render(request, 'about.html')

