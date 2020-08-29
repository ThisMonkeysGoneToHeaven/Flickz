from django.urls import path
from .views import api_detail_ticket

app_name = "moviez"

urlpatterns = [path("<int:slug>/", api_detail_ticket, name="detail")]
