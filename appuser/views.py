import json
from pprint import pprint

from django.shortcuts import render
from django.http import HttpResponse
from appuser.models import User
from api import api_user

def createUser(request, nbre=1):
    users = []
    for n in range(nbre):
        result = api_user()
        user = User(gender=result[0]['gender'], first_name=result[0]['name']['first'], last_name=result[0]['name']['last'], title_name=result[0]['name']['title'],
                    number_location=result[0]['location']['street']['number'], name_location=result[0]['location']['street']['name'],
                    city=result[0]['location']['city'], state=result[0]['location']['state'], country=result[0]['location']['country'], postcode=result[0]['location']['postcode'], latitude=result[0]['location']['coordinates']['latitude'],
                    longitude=result[0]['location']['coordinates']['longitude'], offset=result[0]['location']['timezone']['offset'], description=result[0]['location']['timezone']['description'],
                    email=result[0]['email'], uuid=result[0]['login']['uuid'], username=result[0]['login']['username'], password=result[0]['login']['password'],
                    salt=result[0]['login']['salt'], md5=result[0]['login']['md5'], sha1=result[0]['login']['sha1'], sha256=result[0]['login']['sha256'],
                    date=result[0]['dob']['date'], age=result[0]['dob']['age'], phone=result[0]['phone'], cell=result[0]['cell'])
        user.save()
        users.append(user)

    print(users)
    context = {
        'users': users,
    }
    return render(request, 'appuser/user.html', context)

def listUser(request):
    users = []
    for s in User.objects.all():
        users.append(s)

    context = {
        'users': users,
    }

    return render(request, 'appuser/list_users.html', context)