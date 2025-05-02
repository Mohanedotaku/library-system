from django.urls import path
from .views import BorrowBookView, ReturnBookView

urlpatterns = [
    path('borrow/<int:pk>/', BorrowBookView.as_view(), name='borrow_book'),
    path('return/<int:pk>/', ReturnBookView.as_view(), name='return_book'),

]