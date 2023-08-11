# pages/urls.py
from django.urls import path  # new
from .views import homePageView  # import homePageView inside the views.py

# the function based view (FBVs you created in views.py)

urlpatterns = [
    path("", homePageView, name="home"),
    # if the user request the homepage, represented by the empty string, Django should use the view called "homePageView"
]
