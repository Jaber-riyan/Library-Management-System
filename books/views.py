from django.shortcuts import render,get_object_or_404,redirect
from .import models
from django.views.generic import DetailView
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
class DetailViewOfBook(DetailView):
    model = models.BookModel
    pk_url_kwarg = 'pk'
    template_name = 'book_detail.html'
    
    
@login_required
def profile(request,id):
    data = models.BorrowHistoryModel.objects.filter(user=request.user)
    messages.success(request,'Profile Opening')
    return render(request,'profile.html',{'data':data})




@login_required
def borrowHistory(request, id):
    book = models.BookModel.objects.get(pk=id)
    user = models.UserModel.objects.get(user=request.user)
    if request.user:
        order_history = models.BorrowHistoryModel(
            book_name=book.book_name,
            price=book.book_price,
            category=book.category,
            user=request.user,
            after_decreament = user.balance - book.book_price,
        )
        if book.queantity > 0:
            user = models.UserModel.objects.get(user=request.user)
            user.balance -= book.book_price
            book.queantity -=1
            user.save()
            order_history.save()
            book.save()
            
        elif book.book_price > user.balance:
            messages.error(request,'Book Price is more than Your balance')
        
        elif book.queantity == 0:
            messages.error(request,'Book Copy for borrowed is out of range Plz Borrow another book')    
        
    messages.success(request,'Book Borrowed Successfully')
    return redirect('homepage')



@login_required
def return_book(request, id): 
    returnBook = models.BorrowHistoryModel.objects.get(pk=id) 
    User = models.UserModel.objects.get(user=request.user) 
    book_instance = models.BookModel.objects.get(book_name=returnBook.book_name) 
    User.balance += int(float(returnBook.price))
    book_instance.queantity += 1 
    book_instance.save() 
    User.save() 
    returnBook.delete() 
    messages.success(request,'Book Return Successfully')
    return redirect('homepage')

    
    

