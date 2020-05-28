"""pyzza URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from recipe import views as recipe_views
from django.conf.urls import handler404

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',recipe_views.home, name='home'),
    path('recipe/<int:recipe_id>', recipe_views.recipe_detail, name='recipe_detail'),
    path('order', recipe_views.order_new, name="order_new"),
    path('order/all', recipe_views.order_all.as_view(), name='order_list'),
    path('order/<int:pk>', recipe_views.edit_order.as_view(), name='edit_order' ),
    path('order/remove/<int:pk>', recipe_views.remove_order.as_view(), name='remove_order' ),

]

handler404 = recipe_views.error_404