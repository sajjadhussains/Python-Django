from django.urls import path
# from book.views import home,store_book,show_book,edit_book,delete_book
from . import views

urlpatterns = [
    # path('',views.home,name='homepage'),
    # path('',views.TemplateView.as_view(template_name='home.html')),
    path('',views.MyTemplateView.as_view(),name='homepage'),
    path('store_book/',views.store_book,name='storebook'),
    path('show_book/',views.show_book,name='showbook'),
    path('edit_book<int:id>',views.edit_book,name="editbook"),
    path('delete_book/<int:id>',views.delete_book,name="deletebook"),
]
