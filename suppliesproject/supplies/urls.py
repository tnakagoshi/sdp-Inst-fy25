from django.urls import path
from . import views

urlpatterns = [
    path('supplies/', views.ListSuppliesView.as_view(), name='list-supplies'),
    path('supplies/<int:pk>/detail/', views.DetailSuppliesView.as_view(), name='detail-supplies'),
    path('supplies/create/', views.CreateSuppliesView.as_view(), name='create-supplies'),
    path('supplies/<int:pk>/update/', views.UpdateSuppliesView.as_view(), name='update-supplies'),
    path('supplies/<int:pk>/delete/', views.DeleteSuppliesView.as_view(), name='delete-supplies'),
    path('supplies/<int:supplies_id>/review/', views.CreateReviewView.as_view(), name='create-review'),
    path('', views.index_view, name='index'),
    path('review/<int:pk>/delete/', views.DeleteReviewView.as_view(), name='delete-review'),  
    path('supplies/<int:pk>/add-order/', views.create_order_view, name='add-order'),
    path('supplies/list_orders/', views.ListOrdersView.as_view(), name='list-orders'),
    path('supplies/apply_orders/', views.apply_order_view, name='apply-orders'),
    path('supplies/complete_orders/', views.complete_order_view, name='complete-orders'),

]

