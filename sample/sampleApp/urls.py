
from django.urls import path

from .views import *

urlpatterns = [
    path('', LoginPage.as_view(), name="login_page"),  
    path('Add_Page/', AddPage.as_view(),name="Add_Page"),
    path('AdminDashboardPage/', AdminDashboardPage.as_view(),name="AdminDahboard_Page"),
    path('ApprovePage/', ApprovePage.as_view(),name="Approve_page"),
    path('user_reg/', UserReg.as_view(),name="user_reg"),
    path('manufacture/', Manufacture.as_view(),name="manufacture"),
    path('AddProduct/', AddProduct.as_view(),name="AddProduct"),
    path('FeedBack/',viewFeedBack.as_view(),name="feedback"),
]
