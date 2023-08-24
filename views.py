from flask import make_response,Flask, flash, redirect, render_template, request, url_for, session
from app import *
import sqlite3

conn = sqlite3.connect("database/database.db", check_same_thread=False)
cursor = conn.cursor()
coon = sqlite3.connect("database/donardata.db", check_same_thread=False)
cursor = coon.cursor()


# ---------------------------------------------------------- #
# Main Page
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login',methods=['POST','GET'])
def login():
    if request.method =='POST':    
        email=request.form['email']
        password=request.form['password']

        
        cur=conn.cursor()
        data = cur.execute("SELECT * FROM userdata WHERE email = '{}' AND Password = '{}'".format(email, password))
        data = cur.fetchone()
        
        if data:
            return redirect ('/dashboard')
        else:
            return "Wrong Password"
            
    else:
        #flash("Wrong password")
        return render_template('sign-inpage.html')
    

@app.route('/register',methods=['POST','GET'])
def register():
    if request.method == 'POST':
        nm = request.form['nm']
        an=request.form['an']
        em=request.form['em']
        pn=request.form['pn']
        dob=request.form['dob']
        age=request.form['age']
        bg=request.form['bg']
        pc=request.form['pc']
        pw=request.form['pw']
        cpw=request.form['cpw']
        add=request.form['add']
        city=request.form['city']
        pincode=request.form['pincode']
        gen=request.form['gen']
        typ=request.form['typ']

        cursor.execute("INSERT INTO userdata(Name,Type,Age,aadharnumber,Gender,Bloodtype,Physicallychallanged, email,phone, address,city,pincode,password,confpassword) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)",(nm,typ,age,an,gen,bg,pc,em,pn,add,city,pincode,pw,cpw))
        
        conn.commit()

        return redirect('/login')
    else:
        return render_template('register.html')
    
@app.route('/forgetpassword')
def forget ():
    return render_template('forget password.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/campaign')
def campaign():
    return render_template('campaign.html')

@app.route('/profile')
def profile():
    return render_template('profile-page.html')

@app.route('/stock')
def stock():
    return render_template('stock.html')

@app.route('/donate',methods=['POST','GET'])
def donate():
     if request.method == 'POST':
        nm = request.form['nm']
        an=request.form['an']
        em=request.form['em']
        pn=request.form['pn']
        gen=request.form['gen']
        age=request.form['age']
        pl=request.form['pl']
        date=request.form['date']
        time=request.form['time']
        bg=request.form['bg']
        donate=request.form['donate']

        cursor.execute("INSERT INTO donardata(name,aadhar,email,phone,gender,age,place,date,time,donate,bloodgroup) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)",(nm,an,em,pn,gen,age,pl,date,time,donate,bg))
        
        coon.commit()
       
        return redirect('/dashboard')
        flash('Registerd Sucessfully')    

     else:
        flash('Insert correct value')
        return redirect('/dashboard')
        
