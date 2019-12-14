from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from languages import views

urlpatterns = [
    path('languages/', views.LanguageList.as_view()),
    path('languages/<int:pk>/', views.LanguageDetail.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)
