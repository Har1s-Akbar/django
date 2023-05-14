from django.urls import path, include
from .views import BookView, BookDetail

urlpatterns = [
    path('book/', BookView.as_view(), name='book'),
    path('<uuid:pk>', BookDetail.as_view(), name='book_detail')
]
