from django.urls import path

from .views import home_view, signup_view, dashboard_view

app_name = "Logout"

urlpatterns = [
    path('', home_view, name='home'),
    path('signup/', signup_view, name='sign-up'),
    path('dashboard/', dashboard_view, name='dashboard'),
]
