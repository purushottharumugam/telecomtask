from django.urls import path
from .views import CustomerListView, CustomerCreateView, CustomerDetailView,\
    RenewPlanView

urlpatterns = [
    path("customers/", CustomerListView.as_view(), name='customer_list'),
    path("customers/create/", CustomerCreateView.as_view(),
         name='create_customer'),
    path("customers/<int:pk>/", CustomerDetailView.as_view(),
         name='customer_details'),
    path("renew/<int:pk>/", RenewPlanView.as_view(),
         name='customer_details')
]
