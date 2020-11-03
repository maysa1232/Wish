from django.shortcuts import render, redirect
from .models import User, Wish, Granted_wish
from django.contrib import messages
import bcrypt
# Create your views here.
def Login_Reg(request):
    return render(request, 'login_reg.html')

def Register(request):
    print(request.POST)
    errors = User.objects.validate_register(request.POST)
    if len(errors) > 0:
        print("Errors",errors)
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else:
        pwhash = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
        user = User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'], password=pwhash.decode())
        print("User: ", user)
        request.session['id'] = user.id
    return redirect('/success')

def Login(request):
    errors = User.objects.validate_login(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else:
        user = User.objects.get(email=request.POST['email'])
        request.session['id'] = user.id
    return redirect('/success')

def Success(request):
    context = {
    'user': User.objects.get(id=request.session['id'])
    }
    return render(request, "AllWishes.html", context)

def Logout(request):
    request.session.clear()
    print("Logged Out")
    return redirect('/')

def wishes(request):
    if 'id' not in request.session:
        return render(request, '/')
    else:
        context = {
            'user': User.objects.get(id=request.session['id']),
            'wishes': Wish.objects.all(),
            'granted_wishes': Granted_wish.objects.all()
        }
        return render(request, 'AllWishes.html', context)

def new(request):
    if 'id' not in request.session:
        return redirect('/')
    else:
        context = {
            'user': User.objects.get(id=request.session['id'])
        }
        return render(request, 'NewWish.html', context)

def new_wish(request):
    if request.method == 'POST':
        errors = Wish.objects.wish_validator(request.POST)
        if len(errors):
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/new')
        else:
            Wish.objects.create(item=request.POST['item'], desc=request.POST['desc'], user=User.objects.get(id=request.POST['user_id']))
            return redirect('/wishes')
    else:
        return redirect('/')

def stats(request):
    if 'id' not in request.session:
        return render(request, '/')
    else:
        context = {
            'user': User.objects.get(id=request.session['id']),
            'granted_wishes': Granted_wish.objects.count(),
            'user_granted_wishes': User.objects.get(id=request.session['id']).granted_wishes.count(),
            'user_pending_wishes': User.objects.get(id=request.session['id']).wish.all().count()
        }
        return render(request, 'stats.html', context)

def edit(request, id):
    if 'id' not in request.session:
        return render(request, '/')
    else:
        context = {
            'user': User.objects.get(id=request.session['id']),
            'wish': Wish.objects.get(id=id)
        }
        return render(request, 'edit.html', context)


def update(request, id):
    if request.method == 'POST':
        errors = Wish.objects.wish_validator(request.POST)
        if len(errors):
            for key, value in errors.items():
                messages.error(request, value)
                return redirect('/edit')
        else:
            wish = Wish.objects.get(id= id)
            wish.item = request.POST['item']
            wish.desc = request.POST['desc']
            wish.save()
            return redirect('/wishes')    
    else:
        return redirect('/')


def delete(request):
    if request.method == 'POST':
        wish = Wish.objects.get(id=request.POST['wish_id'])
        wish.delete()
        return redirect('/wishes')
    else:
        return redirect('/success')

def grant(request):
    if request.method == 'POST':
        Granted_wish.objects.create(item=request.POST['wish_item'], user=User.objects.get(id=request.POST['user_id']), date_added=request.POST['wish_created'])
        wish = Wish.objects.get(id=request.POST['wish_id'])
        wish.delete()
        return redirect('/wishes')
    else:
        return redirect('/success')

def like(request):
    if request.method == 'POST':
        granted = Granted_wish.objects.get(id=request.POST['grant_id'])
        user = User.objects.get(id=request.POST['user_id'])
        if granted.user_id == user.id:
            messages.error(request, "Users may not like their own wishes.")
            return redirect('/wishes')
        else:
            granted.likes.add(user)
            return redirect('/wishes')