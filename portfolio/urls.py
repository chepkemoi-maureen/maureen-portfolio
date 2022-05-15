from django.urls import path

from portfolio.views import HomeView

app_name = "portfolio"

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
]
