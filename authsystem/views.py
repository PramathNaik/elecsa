from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from participants.models import participant
from posts.models import elecsa_post
from votes.models import vote

def home(request):
    if request.user.is_authenticated:
        return redirect('/dashboard')
    else:
        if request.method=="POST":
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/dashboard')
            else:
                messages.error(request,messages.ERROR,'username or password doesnot match')
                return redirect('/')
    return render(request,'login.html')

def dashboard(request):
    if request.user.is_authenticated:
        context = {}
        context['posts'] = elecsa_post.objects.all()
        return render(request,'dashboard.html',context)
    else:
        return redirect('/')

def voting(request,id=None):
    if request.user.is_authenticated:
        context = {}
        post = elecsa_post.objects.get(id=id)
        try:
            votedone = vote.objects.get(post=id,voter=request.user)
            return render(request,'alreadyvoted.html')
        except:
            participants = participant.objects.filter(post=id)
            context['post']= post
            context['participants'] = participants
            return render(request,'voting.html',context)
            
    else:
        return redirect('/')

def votesys(request,id=None,per=None):
    if request.user.is_authenticated:
        try:
            votedone = vote.objects.get(post=id,voter=request.user)
            return render(request,'alreadyvoted.html')
        except:
            post = elecsa_post.objects.get(id=id)
            participants = participant.objects.get(id=per)
            user = request.user
            votes = vote(participant=participants,post=post,voter=user)
            votes.save()
            return render(request,'votingsuccess.html')
    else:
        return redirect('/')

def results(request):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            context = {}
            votes = vote.objects.all()
            posts = elecsa_post.objects.all()
            participants = participant.objects.all()
            context['votes'] = votes
            context['posts'] = posts
            context['participant'] = participants
            return render(request,'results.html',context) 
        else:
            return HttpResponse("Only admins can view the result")       
    else:
        return redirect('/')

def logout_session(request):
    logout(request)
    return redirect('/')