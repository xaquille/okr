from flask import Flask, render_template, send_from_directory
from flask import Flask, render_template, request, flash
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap

from flask_wtf import FlaskForm
from wtforms import SubmitField, SelectField, RadioField, HiddenField, StringField, IntegerField, FloatField
from wtforms.validators import InputRequired, Length, Regexp, NumberRange
from datetime import date

import json
from flask_mysqldb import MySQL

import os
import time

# import redirect

app = Flask(__name__)
app.config['SECRET_KEY'] = 'redteam'

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'network'
app.config['MYSQL_PASSWORD'] = '123qweasd'
app.config['MYSQL_DB'] = 'network'
mysql = MySQL(app)


@app.route('/')
def home():
   cur = mysql.connection.cursor()
   cur.execute('''SELECT domain, source, waf,link, exploit, shellcode FROM domain''')
   rv = cur.fetchall()
   return render_template("index.html",value=rv)
   # return render_template('index.html')
   
@app.route('/url', methods=["GET","POST"])
def url():
   return redirect("www.google.com")


@app.route('/add/' , methods=["POST", "GET"])
def add():
   msg =''
   if request.method == "POST" and 'domain' in request.form and 'source' in request.form :
      domain = request.form["domain"]
      source = request.form["source"]
      
      #waf process
      # os.system('wafw00f '+domain+' -o wafwoof/'+domain+'.json')
      os.system('python3 wafwoof/tes.py -u '+domain)
      time.sleep(10)
      #add to db
      f = open('wafwoof/'+domain+'.json')
      data = json.load(f)
      try:
         print(data[0]["firewall"])
         waf = (data[0]["firewall"])
      except IndexError:
         waf = 'Scan WAF Error'
      
      
      
      #nmap process
      os.system('nmap -sV -T5 '+domain+' -Pn -oX nmap/'+domain+'.xml')
      
      #searchploit process
      os.system('searchsploit nmap/'+domain+'.xml -j > searchploit/'+domain+'.json &&  xsltproc nmap/'+domain+'.xml -o static/nmap/'+domain+'.html && rm nmap/'+domain+".xml && weasyprint static/nmap/"+domain+".html static/nmap/"+domain+".pdf && rm static/nmap/"+domain+".html")
      #Add to db
      f = open('searchploit/'+domain+'.json')
      data = json.load(f)
      exploit = (data["RESULTS_EXPLOIT"])
      try:
         if exploit in ("", [], None, 0, False):
            exploit = "Comming Soon"
         else:
            exploit = exploit
         shellcode = (data["RESULTS_SHELLCODE"])
         if shellcode in ("", [], None, 0, False):
            shellcode = "Comming Soon"
         else:
            shellcode = shellcode
      except IndexError:
         exploit = 'null'
         shellcode = 'null'
         
      #link
      link = domain+".pdf"
      
      #cleaning Wafwoof
      os.system('rm wafwoof/'+domain+'.json && rm searchploit/'+domain+'.json')
      
      #saving all the values to db
      cur = mysql.connection.cursor()
      cur.execute("INSERT INTO domain(domain, source, waf, link, exploit, shellcode) VALUES (%s, %s, %s, %s, %s, %s)", (domain, source, waf, link, exploit, shellcode))
      mysql.connection.commit()
      cur.close()
      msg = 'add '+domain+' success'
      
   elif request.method == 'POST':
       msg = 'Please fill out the form!'
   return render_template('add.html', msg=msg)



if __name__ == '__main__':
   app.run()