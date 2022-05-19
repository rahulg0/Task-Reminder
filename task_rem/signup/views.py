from django.shortcuts import render
import mysql.connector as sql
from colorama import Cursor

# Create your views here.
def signup_action(request):

    global fn , ln , em , pwd , id 
    if request.method== 'POST':
        m = sql.connect(host= "localhost" , user = "root" , passwd = "admin123" , database = 'task_reminder') # connecting to database
        cursor = m.cursor() #to import cursor
        d=request.POST #for data entering
    
        fn = d["fname"]
        ln = d["lname"]
        em = d["email"]
        id = d["username"]
        pwd = d["psswd"]
        i = "insert into users values ('{}' , '{}' , '{}', '{}', '{}' )".format(fn , ln ,id, em , pwd)
        cursor.execute(i)
        m.commit()

        i = "select * from users where user_name = '{}'and email = '{}'  ".format(id , em)
        cursor.execute(i)
        t = tuple(cursor.fetchall())
        if t == ():
            return render(request , 'error.html')
        else:
            return render(request , 'dashboard.html')

    return render(request , 'signup.html')