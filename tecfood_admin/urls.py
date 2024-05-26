from django.urls import path
from tecfood_admin.views.user_view import register , login, profile, update_profile, user_list
from tecfood_admin.views.role_view import RoleViewSet

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('profile/', profile, name='profile'),
    path('update_profile/', update_profile, name='update_profile'),
    path('list/', user_list, name='list'),
    
    path('role/', RoleViewSet.as_view({'get': 'list', 'post': 'create'}), name='role'),
]
