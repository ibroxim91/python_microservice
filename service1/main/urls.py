from django.urls import path
from .views import SubmitFormView


urlpatterns = [
   
    path('send', SubmitFormView.as_view() ),
]
