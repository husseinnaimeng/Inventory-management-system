from django.urls import path
from . import views

urlpatterns = [
    path("",views.ListCreateInventory.as_view()),
    # This view's result is controled by the request method (GET,PUT,DELETE)
    path("<int:pk>/",views.RetrieveUpdateDestroyInventoryAPIView.as_view()),
    path("product/type-variation/",views.ListCreateTypeVariationAPIView.as_view()),
    path('product/',views.ListCreateProductAPIView.as_view())
]
