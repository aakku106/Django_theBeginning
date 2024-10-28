from django.shortcuts import render

from django.http import HttpResponse


def homi(request):
    
    context = {'page' : '1st django try '}

    people = [
        {'name' : 'Aakku' , 'age' : 16},
        {'name' : 'CCN' , 'age' : 106},
        {'name' : 'TOfu' , 'age' : 6},
        {'name' : 'Axix' , 'age' : 20},
    ]
    
    aboutme = '''Hey there! I'm Adarasha Gaihre (Aakku), an IT student currently pursuing my BSc in Computer Science and Information Technology (BSc.CSIT) in Nepal. I'm passionate about coding, anime (huge Naruto fan!), and working on creative web projects. I enjoy spending time with friends, drawing, and continuously learning new skills in the world of development.'''
    
    return render(request,"homi/index.html" , context={'page' : '1st django','peoples' : people, 'text':aboutme},)




def contact_page(request):
    context = {'page' : 'Contacts'}
    return render(request,"homi/contact.html" ,context  )


def about_page(request):
    context = {'page' : 'About'}
    return render(request,"homi/about.html" ,context ,)



# def success_page(request):
#     return HttpResponse("<h1> hui hui hi success huii</h1>")