from django.urls import path

from .views import FinanceView

app_name = "repositories"

urlpatterns = [
    path("api/finance", FinanceView.as_view(), name="finance-list"),
]
