from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages

from .models import *


def index(request):
    return render(request,'zigzag_app/index.html')

def process(request):
    errors = User.objects.validator(request.POST)
    print(errors)

    if len(errors) > 0:
        # if the errors dictionary contains anything, loop through each key-value pair and make a flash message
        for key, value in errors.items():
            messages.error(request, value, extra_tags="register")
        return redirect('/')

    matched_email = User.objects.filter(email=request.POST['email'])
    if len(matched_email) > 0:
        print("this is working")
        messages.error(request,'User already exists',extra_tags="register")
        return redirect('/')
    
    else:   
        new_user = User.objects.create(first_name = request.POST['first_name'], last_name = request.POST['last_name'], email = request.POST['email'], password = request.POST['password'])
        request.session['email'] = new_user.email
        request.session['id'] = new_user.id

        return redirect('/jobs')

def register(request):
    print("we are now in the register function")
    current_user = User.objects.get(id=request.session['id'])
    print(current_user)
    context = {
        "reg_user": User.objects.get(email = request.session['email']),
        "everybodys_jobs": Job.objects.exclude(picked_by=current_user),
        "chosen_job": Job.objects.filter(is_chosen=True).filter(picked_by=current_user)
    }
    return render(request,'zigzag_app/jobs.html',context)

def loginprocess(request):
    #check if user is in system
    print(request.POST)
    matched_user = User.objects.filter(email=request.POST['email'])
    
    if len(matched_user) < 1:
        messages.error(request,'User and/or password does not match',extra_tags="login")
        return redirect('/')

    #check if user and password match
    if matched_user[0].password != request.POST['password']:
        messages.error(request,'User and/or password does not match',extra_tags="login")
        return redirect('/')
    else:
        request.session['email'] = request.POST['email']
        request.session['id'] = matched_user[0].id
        return redirect('/jobs')

def new_job(request):
    context = {
        "reg_user": User.objects.get(email=request.session['email'])
    }

    return render(request,"zigzag_app/new_job.html",context)

def addjob(request):
    errors = Job.objects.jobvalidator(request.POST)
    print(errors)

    if len(errors) > 0:
        # if the errors dictionary contains anything, loop through each key-value pair and make a flash message
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/jobs/new')
    print("Finally working")

    current_user = User.objects.get(id=request.session['id'])
    Job.objects.create(title = request.POST['title'],description = request.POST['description'], location= request.POST['location'], created_by = current_user)
    return redirect('/jobs')
    
def delete(request, job_id):
    print("delete function works")
    deleted_job = Job.objects.get(id=job_id)
    deleted_job.delete()
    print("*"*100)
    return redirect('/jobs')

def edit(request, job_id):
    request.session['jobid'] = job_id
    context = {
        "reg_user": User.objects.get(email=request.session['email']),
        "edited_job": Job.objects.get(id=job_id)
    }
    return render(request,'zigzag_app/edit.html', context)

def update(request, job_id):
    errors = Job.objects.jobvalidator(request.POST)
    print(errors)

    if len(errors) > 0:
        # if the errors dictionary contains anything, loop through each key-value pair and make a flash message
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/edit/'+(job_id))
    current_user = User.objects.get(email=request.session['email'])
    updated_job = Job.objects.get(id=job_id)
    updated_job.title = request.POST['title']
    updated_job.description = request.POST['description']
    updated_job.location = request.POST['location']
    updated_job.created_by = current_user
    updated_job.save()
    return redirect('/jobs')

def view(request, job_id):
    request.session['jobid'] = job_id
    context = {
        "reg_user": User.objects.get(id=request.session['id']),
        "selected_job": Job.objects.get(id=job_id)
    }
    return render(request, 'zigzag_app/view.html', context)

def add(request, job_id):
    chosen_job_user = User.objects.get(id=request.session['id'])
    chosen_job = Job.objects.get(id=job_id)
    chosen_job.is_chosen = True
    chosen_job.picked_by.add(chosen_job_user)
    chosen_job.save()
    print('chosen jobs working')
    return redirect('/jobs')

def giveup(request, job_id):
    chosen_job_user = User.objects.get(id=request.session['id'])
    chosen_job = Job.objects.get(id=job_id)
    chosen_job.is_chosen = False
    chosen_job.picked_by.remove(chosen_job_user)
    return redirect('/jobs')


# def granted(request, wish_id):
#     granted_wish = Wish.objects.get(id=wish_id)
#     granted_wish.is_granted = True
#     granted_wish.save()
#     print('this is working')
#     return redirect('/jobs')

# def like(request, wish_id):
#     liked_wish_user = User.objects.get(id=request.session['id'])
#     liked_wish = Wish.objects.get(id=wish_id)
#     liked_wish.liked_by.add(liked_wish_user)
#     return redirect ('/jobs')

# def unlike(request, wish_id):
#     liked_wish_user = User.objects.get(id=request.session['id'])
#     liked_wish = Wish.objects.get(id=wish_id)
#     liked_wish.liked_by.remove(liked_wish_user)
#     return redirect ('/jobs')

# def stats(request):
#     current_user = User.objects.get(id=request.session['id'])
#     context = {
#         "reg_user": User.objects.get(id=request.session['id']),
#         "all_granted_wish": Wish.objects.filter(is_granted=True),
#         "granted_wish": Wish.objects.filter(wished_by=current_user).filter(is_granted=True),
#         "pending_wish": Wish.objects.filter(wished_by=current_user).filter(is_granted=False)
#     }
#     return render(request, 'zigzag_app/viewstats.html', context)


def logout(request):
    request.session.clear()
    return redirect('/')