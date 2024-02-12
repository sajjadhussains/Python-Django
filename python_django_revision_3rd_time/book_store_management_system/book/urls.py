from django.urls import path

# from book.views import home,show_book,store_book,edit_book,delete_book
from . import views

urlpatterns = [
    # path('',home,name="homepage"),
    path('',views.TemplateView.as_view(template_name='base.html')),
    # path('show_book/',views.show_book,name="showbook"),
    # path('sotre_book',views.store_book,name="storebook"),
    # path('edit_book/<int:id>',views.edit_book,name="editbook"),
    # path('delete_book/<int:id>',views.delete_book,name="deletebook")
]
