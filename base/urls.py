from django.urls import path
from .views import register,login_view_s,login_view_r,success_s,success_r,jobs_creation,jobs_recruit_view

urlpatterns = [
    path('register/', register, name='register'),
    path('login_s/', login_view_s, name='login_s'),
    path('login_r/', login_view_r, name='login_r'),
    path('success_s/', success_s, name='success_s'),
    path('success_r/', success_r, name='success_r'),
    path('jobs_c/', jobs_creation, name='jobs_creation'),
    path('jobs_rec_view/', jobs_recruit_view, name='jobs_recruit_view'),
]

