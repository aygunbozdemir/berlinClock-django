from django.conf.urls import url
from django.urls import path
from berlinClock import views

urlpatterns = [
    # url(r'^$', views.HomePageView.as_view()),
    # url(r'^aboutme/$', views.AboutMePageView.as_view()),
    # url(r'^contact/$', views.ContactPageView.as_view()),
    path('', views.HomePageView.as_view()),
    path('aboutme/', views.AboutMePageView.as_view()),
    path('contact/', views.ContactPageView.as_view()),
]
