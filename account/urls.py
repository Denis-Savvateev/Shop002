# from django.contrib.auth.forms import UserCreationForm
from django.urls import (
    path,
    include,
    # reverse_lazy,
)
# from django.views.generic.edit import CreateView

from account import views

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('register/', views.register, name='register'),
    # path('login/', include('django.contrib.auth.urls')),
    # path(
    #     'register/',
    #     CreateView.as_view(
    #         template_name='account/register.html',
    #         form_class=UserCreationForm,
    #         success_url=reverse_lazy('config:home'),
    #     ),
    #     name='register',
    # ),
]
