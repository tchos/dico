from django.urls import path
from .views import CreateMotView, SearchMotView, EditMotView

app_name = "mot"

urlpatterns = [
    path('create/', CreateMotView.as_view(), name="add"),
    path('search/', SearchMotView.as_view(), name="search"),
    path('edit/<int:pk>/', EditMotView.as_view(), name="edit"),
]