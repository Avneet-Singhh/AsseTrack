from django.urls import path
from . import views

urlpatterns = [
    path('dashboard', views.index, name="dashboard-index"),
    path('brand', views.brand, name="dashboard-brand"),
    path('brand/delete/<int:pk>', views.brand_delete, name="dashboard-brand-delete"),
    path('brand/update/<int:pk>', views.brand_update, name="dashboard-brand-update"),
    path('product', views.product, name="dashboard-product"),
    path('product/delete/<int:pk>', views.product_delete, name="dashboard-product-delete"),
    path('product/update/<int:pk>', views.product_update, name="dashboard-product-update"),
    path('staff', views.staff, name="dashboard-staff"),
    path('order', views.order, name="dashboard-order"),
]   