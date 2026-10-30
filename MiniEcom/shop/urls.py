from django.urls import path
from . import views

urlpatterns = [

    # Customer CRUD
    path("customers/", views.customer_list, name="customer_list"),
    path("customers/add/", views.customer_create, name="customer_create"),
    path("customers/<int:id>/edit/", views.customer_update, name="customer_update"),
    path("customers/<int:id>/delete/", views.customer_delete, name="customer_delete"),

    # Product CRUD
    path("products/", views.product_list, name="product_list"),
    path("products/add/", views.product_create, name="product_create"),
    path("products/<int:id>/edit/", views.product_update, name="product_update"),
    path("products/<int:id>/delete/", views.product_delete, name="product_delete"),
]