from django.contrib import admin

from .models import AdvUser

admin.site.register(AdvUser)

from django.contrib.auth.views import LoginView

class BBLoginView(LoginView):
   template_name = 'main/login.html'

# Register your models here.
