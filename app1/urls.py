from django.urls import path

from . import views

urlpatterns = [

    path('', views.create_view, name='create'),
    path('<id>/detail', views.detail_view,name='detail' ),
    path('<id>/update', views.update_view,name='detail' ),
    path('<id>/delete',views.delete_view,name='delete'),



]