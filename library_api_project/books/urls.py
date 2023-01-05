from django.urls import path
from . import views
from .views import BookList

urlpatterns = [
    # path('', views.book_list),
    # path('Science/', views.book_list),

    #URLS for class based views
    path('', views.BookList.as_view()),

]