from django.shortcuts import render
from django.views import View

# Create your views here.

class IndexView(View):
    def get(self, request):
        if request.user.is_authenticated:
            login_status = True
            return render(request, "blog/index.html", {'login_status': login_status})
        else:
            login_status = False
            return render(request, "blog/index.html", {'login_status': login_status})
    
class LoginView(View):
    def get(self, request):
        return render(request, "blog/index.html")
    
class RegisterView(View):
    def get(self, request):
        return render(request, "blog/index.html")