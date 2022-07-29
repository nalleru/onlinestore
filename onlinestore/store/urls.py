from django.contrib.auth.views import LogoutView
from django.urls import path
from . import views
from .views import Userlogin, Categorieslist, Categorydetail, Categoryedit, Categoryupdate, Categorydelete, Productlist, Productdetail, Productedit, Productupdate, Productdelete


urlpatterns = [
    path('login/', Userlogin.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('navigations/', views.Navigations, name='navigations'),
    path('categories/', Categorieslist.as_view(), name='categories'),
    path('products/', Productlist.as_view(), name='products'),
    path('category/<int:pk>', Categorydetail.as_view(), name='category'),
    path('product/<int:pk>', Productdetail.as_view(), name='product'),
    path('category-add/', Categoryedit.as_view(), name='category-add'),
    path('product-add/', Productedit.as_view(), name='product-add'),
    path('category-edit/<int:pk>', Categoryupdate.as_view(), name='category-edit'),
    path('product-edit/<int:pk>', Productupdate.as_view(), name='product-edit'),
    path('category-delete/<int:pk>', Categorydelete.as_view(), name='category-delete'),
    path('product-delete/<int:pk>', Productdelete.as_view(), name='product-delete'),
]
