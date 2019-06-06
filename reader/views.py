from django.shortcuts import render, redirect

# Create your views here.
from reader.forms import AccountCreationForm,ReaderForm
from reader.models import Account



def signup(request):
    if request.method == 'POST':
        form = AccountCreationForm(request.POST)
        if form.is_valid():
            form.save()
            user = Account.objects.get(username = request.POST.get('username'))

            request.session['user_name'] = request.POST.get('username')

            if user.u_type.id == 1:
                return redirect('/ReaderForm')
            elif user.u_type.id == 2:
                return redirect('/WriterForm')
    else:
        form = AccountCreationForm()
    return render(request, 'reader/signup.html' , {'form':form})

def readerup(request):
    if request.method == 'POST':
        form = ReaderForm(request.POST)
        if form.is_valid():

            form.save()
            return redirect('home')
    else:
        form = ReaderForm()
    return  render(request,'reader/readerform.html',{'form':form})

