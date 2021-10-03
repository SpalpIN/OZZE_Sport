from django.urls import path

from . import views

urlpatterns = [
    path('', views.start),
    path('write_us/', views.WriteUs.as_view()),

    path('catalog/', views.catalog),
    path('filter/', views.CatalogFilter.as_view()),
    path('catalog_filtered/', views.catalog, {'products': 1}),

    path('products/<int:pk>/', views.product_detail, name='product_detail'),

    path('cart/', views.cart_view),
    path('cart_add/', views.add_to_cart),
    path('cart_del/', views.del_from_cart),

    path('one_click_buing/', views.one_click_buing),
    path('checkout/', views.CheckOut.as_view()),

    path('size_chart/', views.size_chart),
    path('return_change/', views.return_and_change),
    path('delivery_payment/', views.delivery_payment),
    path('wholesale_customers/', views.wholesale_customers),
]
