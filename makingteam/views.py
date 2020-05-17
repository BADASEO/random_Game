from django.shortcuts import render

import random

def home(request):

    list1 =['김재훈','김진우','강채원','김지은','김희찬','박지윤','이명환','BADA SEO','우인아','이민정','이예빈','이은아','정지원','강민지','차주희']
    team = []

    random.shuffle(list1)
    
    temp = []
    for count, value in enumerate(list1):
        print(count,value)
        temp.append(value)

        if (count + 1) % 3 == 0:
            team.append(temp)    
            temp = []    
            
    print(team)
    return render(request, 'home.html', {'hi':team})
