
import operator
import secrets
import sys
import random
from django.http import JsonResponse
import json
import requests
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib import messages, auth
from.models import Profile, Preference

# Create your views here.


def register(request):
    if request.method == 'POST':

        # Get form values
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        # usernm = get_random_string(6, allowed_chars='0123456789')
        # username = first_name + usernm  # single quo
        email = request.POST['email']
        username = email
        password = request.POST['password']
        password2 = request.POST['password2']
        # mobile_no = request.POST['mobile_no']
        # gender = request.POST['gender']
        # location = request.POST['location']

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.error(request, 'Email Id already exist')

                return redirect('register')

            else:
                user = User.objects.create_user(
                    password=password, email=email, first_name=first_name, last_name=last_name, username=username)
                user.save()
                u = User.objects.filter(email=email)
                uid = u[0].id
                # signup = Singup(
                #     user_id=uid, mobile_no=mobile_no, gender=gender, location=location)
                # signup.save()
                pro = Profile(user_id=uid)
                pro.save()
                pref = Preference(user_id=uid)
                pref.save()

                return redirect('login')
        else:

            messages.error(request, 'Passwords do not match')

            return redirect('register')
    else:

        # citydata = city.objects.all()
        return render(request, 'accounts/register.html')
    # return render(request, 'accounts/register.html')


def login(request):
    # if request.user.is_authenticated:
    #     return redirect('/')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:

            auth.login(request, user)

            # messages.success(request, 'You are now logged in')

            return redirect('profile')

        else:

            messages.error(request, 'Invalid credentials')

            return redirect('login')

    else:

        return render(request, 'accounts/login.html')


def profile(request):
    pref = Preference.objects.filter(user_id=request.user.id)
    u = pref[0].Cuisine
    print(u)
    if u:
        return render(request, 'accounts/index.html')

    else:

        if request.method == 'POST':

            # Get form values
            mobile = request.POST['mobile']
            DOB = request.POST['DOB']
            Location = request.POST['Location']
            Budget = request.POST['Budget']
            user_id = request.user.id
            print(user_id)
            u = Profile.objects.filter(user_id=request.user.id).update(
                DOB=DOB, mobile=mobile, Location=Location, Budget=Budget)

            return redirect('lifestyle')
        else:
            prof = Profile.objects.filter(user_id=request.user.id)
            return render(request, 'accounts/newprofile.html', {'prof': prof})


def lifestyle(request):
    if request.method == 'POST':

        Lifestyle = request.POST.getlist('Lifestyle[]')
        user_id = request.user.id
        l = ','.join(Lifestyle)
        request.session['life_style'] = l

        life_style = request.session.get('life_style')
        print(life_style)
        print(type(life_style))

        # user = Preference.objects.filter(
        #     user_id=request.user.id).update(Lifestyle=l)
        return redirect('hobbies')
    else:
        life = Preference.objects.filter(user_id=request.user.id)
        return render(request, 'accounts/lifestyle.html', {'life': life})


def hobbies(request):
    if request.method == 'POST':

        Hobbies = request.POST.getlist('Hobbies[]')
        user_id = request.user.id
        h = ','.join(Hobbies)
        request.session['hobbies'] = h
        # print(life_style)

        # user = Preference.objects.filter(
        #     user_id=request.user.id).update(Hobbies=h)
        return redirect('cuisine')
    else:
        hob = Preference.objects.filter(user_id=request.user.id)
        return render(request, 'accounts/hobbies.html', {'hob': hob})


def cuisine(request):
    if request.method == 'POST':

        Cuisine = request.POST.getlist('Cuisine[]')
        user_id = request.user.id
        c = ','.join(Cuisine)
        request.session['Cuisine'] = c

        # user = Preference.objects.filter(
        #     user_id=request.user.id).update(Cuisine=c)
        return redirect('sport')
    else:
        cuisine = Preference.objects.filter(user_id=request.user.id)
        return render(request, 'accounts/cuisine.html', {'cuisine': cuisine})


def sport(request):
    if request.method == 'POST':

        Sportevent = request.POST.getlist('Sportevent[]')
        user_id = request.user.id
        s = ','.join(Sportevent)
        request.session['Sportevent'] = s

        # user = Preference.objects.filter(
        #     user_id=request.user.id).update(Sportevent=s)
        return redirect('travel')
    else:
        sport = Preference.objects.filter(user_id=request.user.id)
        return render(request, 'accounts/sport.html', {'sport': sport})


def travel(request):
    if request.method == 'POST':

        Travel = request.POST.getlist('Travel[]')
        user_id = request.user.id
        t = ','.join(Travel)
        request.session['Travel'] = t
        # user = Preference.objects.filter(
        #     user_id=request.user.id).update(Travel=t)
        return redirect('event')
    else:
        travel = Preference.objects.filter(user_id=request.user.id)
        return render(request, 'accounts/travel.html', {'travel': travel})


def event(request):
    if request.method == 'POST':
        Entertainment_events = request.POST.getlist('Entertainment_events[]')
        user_id = request.user.id
        e = ','.join(Entertainment_events)
        request.session['Entertainment_events'] = e
        life_style = request.session.get('life_style')
        hobbies = request.session.get('hobbies')
        Cuisine = request.session.get('Cuisine')
        Sportevent = request.session.get('Sportevent')
        Travel = request.session.get('Travel')
        Entertainment_events = request.session.get('Entertainment_events')

        user = Preference.objects.filter(user_id=request.user.id).update(
            Lifestyle=life_style, Hobbies=hobbies, Cuisine=Cuisine, Travel=Travel, Sportevent=Sportevent, Entertainment_events=Entertainment_events)
        return redirect('index')
    else:
        event = Preference.objects.filter(user_id=request.user.id)
        return render(request, 'accounts/event.html', {'event': event})


def index(request):
    return render(request, 'accounts/index.html')


def recomd(request):
    # select cuisine  from pref  where user_id in []
    url = "http://3.6.245.232:5000/api/v1.0/similarcustomer"

    user_id = request.user.id
    print(user_id)
    payload = {'customer_id': user_id, 'top': 2}
    print(payload)
    headers = {
        'Content-Type': 'application/json'
    }
    similar = requests.post(url, headers=headers, data=json.dumps(payload))
    #x = json.load(similar)
    x = similar.json()
    # print("type:--", type(x))
    res = x['results']['similar_customer']
    print("type:--", type(res))
    print(res)
    sim_user_id = ",".join(list(map(str, res)))
    print("sim_user_id:--", sim_user_id)

    # q = Preference.objects.filter(
    #     user_id__in=[3, 4, 5]).values_list('Cuisine')
    query = "SELECT id ,Cuisine FROM account_preference WHERE user_id IN ({})".format(
        sim_user_id)
    print(query)
    user_preference = Preference.objects.raw(query)

    user_preference_list = []
    for p in user_preference:
        pp = p.Cuisine.split(",")
        for ppp in pp:
            user_preference_list.append(ppp)
            # print(ppp)
    ucuisine = list(set(user_preference_list))
    print(ucuisine)

    print("user_preference_list {}".format(user_preference_list))
    print("unique preference {}".format(
        list(set(user_preference_list))))

    c = " ".join(str(ucuisine).split(','))
    print(c)
    # print(random.sample(list(c), 5))
    # print(random.sample(c, 6))
    allcuisine_list = []
    for c in ucuisine:
        cuisine_url = "http://3.6.245.232:5000/api/v1.0/dining"
        print(c)
        payload = {'preference': c}

        headers = {
            'Content-Type': 'application/json'
        }
        cuisin = requests.post(
            cuisine_url, headers=headers, data=json.dumps(payload))
    # return JsonResponse(list(cuisin.values()), safe=False)
        cuisin = cuisin.json()
        recm = cuisin['results']['recommendation']
        # allcuisine_list.append(recm)
        for all_cuisine in recm:
            allcuisine_list.append(all_cuisine)

    # z = allcuisine_list.sort(key=lambda x: x.star.lower())
    # print(z)

    # print(allcuisine_list)
    # print(recm)
    # print(recm)
    # return HttpResponse(allcuisine_list)
    context = {
        'allcuisine_list': allcuisine_list,
    }
    return render(request, 'accounts/dining.html', context)


def dining(request):
    return render(request, 'accounts/dining.html')


def dining_reservation(request):
    return render(request, 'accounts/dining_reservation.html')
