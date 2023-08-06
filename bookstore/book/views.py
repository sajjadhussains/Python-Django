from typing import Any, Dict
from django.shortcuts import render,redirect
from . forms import BookStoreForm,BookStoreModel
from django.views.generic import TemplateView

# Create your views here.

# functional based view
# def home(request):
#     return render(request,'home.html')

# class based view
class MyTemplateView(TemplateView):
    template_name='home.html'
    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context = {'name':'rahim','age':23}
        # print(kwargs)
        return context

def store_book(request):
    if request.method == 'POST':
        book = BookStoreForm(request.POST)
        if book.is_valid():
            book.save()
            print(book.cleaned_data)
            return redirect('showbook')
    else:
        book = BookStoreForm()
    return render(request,'store_book.html',{'form':book})

def show_book(request):
    book = BookStoreModel.objects.all()
    print(book)
    return render(request,'show_book.html',{'datas':book})

def edit_book(request,id):
    book = BookStoreModel.objects.get(pk = id)
    form = BookStoreForm(instance = book)
    if request.method == 'POST':
        form = BookStoreForm(request.POST,instance = book)
        if form.is_valid():
            form.save()
            return redirect('showbook')
    return render(request,'store_book.html',{'form':form})

def delete_book(request,id):
    book = BookStoreModel.objects.get(pk=id)
    book.delete()
    return redirect('showbook')