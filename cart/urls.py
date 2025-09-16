from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='cart.index'),
    path('<int:id>/add/', views.add, name='cart.add'),
    path('clear/', views.clear, name='cart.clear'),
    path('purchase/', views.purchase,
        name='cart.purchase'),
    path("leave-feedback/", views.leave_feedback, name="leave_feedback"),
    path("thank-you/", views.feedback_thankyou, name="feedback_thankyou"),
    path("feedbacks/", views.feedback_list, name="feedback_list"),
]