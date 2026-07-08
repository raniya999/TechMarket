from django.urls import path
from . import views

urlpatterns = [
    # --- Аутентификация (Function-Based Views) ---
    path('auth/login/', views.login_view, name='login'),
    path('auth/logout/', views.logout_view, name='logout'),

    # --- Заказы: Full CRUD (Class-Based Views / APIView) ---
    path('orders/', views.OrderListCreateView.as_view(), name='order-list-create'),
    path('orders/<int:pk>/', views.OrderDetailView.as_view(), name='order-detail'),
]