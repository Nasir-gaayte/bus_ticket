from django.urls import path
from . import views
from acc import api

urlpatterns = [
    path('login/',views.log,name='login'),
    path('register/',views.Reg.as_view(),name='register'),
    path('logout/',views.logout_req,name='logout'),
    path('ApiUL',api.UserApiList.as_view(),name='ApiUL'),
    path('ApiUD/<int:id>/',api.UserApiDetail.as_view(),name='ApiUD'),
]
