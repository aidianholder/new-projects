from django.urls import path, re_path

from . import views

urlpatterns = [
    path('/', views.index, name="index"),
    path('facility/<str:facility>/', views.facility_by_name, name="by_name"),
    path('facility/<uuid:facility_id>/', views.facilty_by_id, name="by_id"),
]


urlpatterns += [
    re_path(r'^json/all/$', views.alljsonp, name="alljsonp")
]