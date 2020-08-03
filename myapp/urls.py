from django.urls import path
from myapp import views
app_name="myapp"

urlpatterns = [
    path('trails/',views.trail,name="Trail"),
    path('profile/',views.profile,name="profile"),
]
