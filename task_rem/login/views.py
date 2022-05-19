import token
from django.shortcuts import render
import mysql as sql

# Create your views here.
def login_action(request):

    global pwd , id 
    if request.method== 'POST':
        m = sql.connect(host= "localhost" , user = "root" , passwd = "admin123" , database = 'task_reminder') # connecting to database
        cursor = m.cursor() #to import cursor
        d=request.POST #for data entering
    
        id = d["username"]
        pwd = d["psswd"]
        i = "select * from users where user_name = '{}'and pass = '{}'  ".format(id , pwd)
        cursor.execute(i)
        t = tuple(cursor.fetchall())
        if t == ():
            return render(request , 'error.html')
        else:
            return render(request , 'dashboard.html')



    return render(request , 'login.html')