from django.shortcuts import render
from django.views import View
from .forms import BlogPostForm
from django.views.generic.edit import FormView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.


class IndexView(View):
    def get(self, request):
        if request.user.is_authenticated:
            login_status = True
            return render(request, "blog/index.html", {
                'login_status': login_status,
                'username': request.user.username
            })
        else:
            login_status = False
            return render(request, "blog/index.html",
                          {'login_status': login_status})


class ComposeBlogPostView(LoginRequiredMixin, FormView):
    '''Only logged in users can access this view, otherwise they will be
    redirected to the login page. After login, people reach the compose site again. 
    This is done be LoginRequiredMixin'''
    
    template_name = 'blog/compose_post.html'
    form_class = BlogPostForm
    success_url = '/userposts'
    raise_exception = False
    
    
    def form_valid(self, form):
        '''Add logged in user instance to form'''
        form.instance.author = self.request.user
        form.save()
        return super(ComposeBlogPostView, self).form_valid(form)

        
#class UserPostsView(View):