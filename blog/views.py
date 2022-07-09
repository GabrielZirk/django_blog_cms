from django.shortcuts import render
from django.views import View
from .forms import BlogPostForm
from .models import BlogPost
from django.views.generic.edit import FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.models import User
from django.urls import reverse

# Create your views here.


class IndexView(View):
    '''Manages the requests on the landing page
    Only the 5 latest posts shall be seen'''

    def get(self, request):
        sorted_posts = BlogPost.objects.order_by('-id')
        latest_posts = sorted_posts[:4]
        print(latest_posts)
        if request.user.is_authenticated:
            login_status = True
            return render(
                request, "blog/index.html", {
                    'login_status': login_status,
                    'username': request.user.username,
                    'latest_posts': latest_posts
                })
        else:
            login_status = False
            return render(request, "blog/index.html", {
                'login_status': login_status,
                'latest_posts': latest_posts
            })


class ComposeBlogPostView(LoginRequiredMixin, FormView):
    '''Only logged in users can access this view, otherwise they will be
    redirected to the login page. After login, people reach the compose site again. 
    This is done be LoginRequiredMixin'''

    template_name = 'blog/compose_post.html'
    form_class = BlogPostForm
    # success_url = '/userposts'
    raise_exception = False

    def get_success_url(self):
        '''After submitting a post, the user is redirected to his own blog site'''
        return reverse('user_posts',
                       kwargs={'author': self.request.user.username})

    def form_valid(self, form):
        '''Add logged in user instance to form'''
        form.instance.author = self.request.user
        form.save()
        return super(ComposeBlogPostView, self).form_valid(form)


class UserPostsView(ListView):
    model = BlogPost
    context_object_name = 'user_posts'
    template_name = "blog/user_posts.html"

    def get_queryset(self, *args, **kwargs):
        '''Query the dataset to fetch the posts of a specific user
        ordered by date, showing the latest post first'''
        author = User.objects.get(username=self.kwargs["author"])
        print(author)
        query = super(UserPostsView, self).get_queryset(*args, **kwargs)
        user_posts = query.filter(author=author).order_by('-date')
        return user_posts

class DetailedPostView(LoginRequiredMixin, DetailView):
    model = BlogPost
    context_object_name = 'detailed_post'
    template_name = "blog/detailed_post.html"
    
    def get_object(self, *args, **kwargs):
        print(BlogPost.objects.get(slug=self.kwargs["slug"]))
        return BlogPost.objects.get(slug=self.kwargs["slug"])
        