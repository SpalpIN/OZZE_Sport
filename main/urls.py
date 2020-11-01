from django.urls import path, re_path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [

    path('', views.start),
    re_path('write_us/', views.WriteUs.as_view()),
    re_path('catalog/', views.catalog),
    re_path('filter/', views.CatalogFilter.as_view()),
    re_path('catalog_filtered/', views.catalog, {'products': 1}),
    path('cart/', views.cart_view),
    re_path('cart_add/', views.add_to_cart),
    re_path('cart_del/', views.del_from_cart),
    path('checkout/', views.CheckOut.as_view()),
    re_path('one_click_buing/', views.one_click_buing),

    re_path('size_chart/', views.size_chart),
    re_path('return_change/', views.return_change),
    re_path('delivery_payment/', views.delivery_payment),
    re_path('wholesale_customers/', views.wholesale_customers),

    path('<int:pk>/', views.product_detail, name='product_detail'),




    # re_path('register/', views.RegisterForm.as_view()),
    # re_path('auth/', views.AuthForm.as_view()),
    # re_path('logout/', views.LogoutForm.as_view()),
    #
    # path('reset_password/', auth_views.PasswordResetView.as_view(template_name="password_reset.html"), name="reset_password"),
    # path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name="password_reset_sent.html"), name="password_reset_done"),
    # path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_form.html"), name="password_reset_confirm"),
    # path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="password_reset_done.html"), name="password_reset_complete"),\
    #
    # re_path('account/', views.Account.as_view()),
    # re_path('changeAccData/',views.ChangeAccData.as_view()),
    # re_path('sale_catalog/', views.OnSaleCatalog.as_view()),
    # path('product/<int:pk>/', views.product_detail, name='product_detail'),
    #



]
