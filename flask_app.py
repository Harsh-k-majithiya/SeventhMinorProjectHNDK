from flask import Flask , render_template
from flask_cors import CORS
import pyrebase
import requests
import os

app = Flask(__name__)
CORS(app=app)


# routes 

@app.route('/')
def hello_world():
   return render_template('index.html')

@app.route('/api/Evaluate') 
def Evalute() :
   print('evaluate hit')

   config = {
      'apiKey': 'AIzaSyD4GymOu2vS_eAtMl1_BcGKyVZGZVvEewU',
      'authDomain': "hndk-solutions.firebaseapp.com",
      'databaseURL': "https://hndk-solutions-default-rtdb.firebaseio.com",
      'projectId': 'hndk-solutions',
      'storageBucket': "hndk-solutions.appspot.com",
      'messagingSenderId': '589019280099',
      'serviceAccount' : 'C:/Users/Harsh Majithiya/Documents/nikhilproject/4IT43_MINOR_PROJECT/hndk-solutions-firebase-adminsdk-6qogr-b8cff5ff7a.json'
   }


   firebase = pyrebase.initialize_app(config)
   storage = firebase.storage()
   all_files = storage.child().list_files()

   directory = "Students_Answer"
   faculty_directory = "Faculty_Answer"
   parent_dir = "C:\\Users\\Harsh Majithiya\\Documents\\nikhilproject\\4IT43_MINOR_PROJECT"
   path = os.path.join(parent_dir, directory)
   if not os.path.exists(path) :
      os.mkdir(path)

   faculty_path = os.path.join(parent_dir , faculty_directory)
   if not os.path.exists(faculty_path) : 
      os.mkdir(path=faculty_path)

   for file in all_files:
      file_name = file.name[6:]
      url = storage.child(file.name).get_url(None)
      data = requests.get(url, stream=True)
      
      if file_name == 'ModelAnswersheet.txt' : 
         with open(faculty_path + '/' + file_name , 'wb') as f :
               f.write(data.content)

   all_files = storage.child().list_files()
   for file in all_files:
      file_name = file.name[6:]
      url = storage.child(file.name).get_url(None)
      data = requests.get(url, stream=True)
      if file_name != 'ModelAnswersheet.txt' : 
         with open(path + '/' + file_name , 'wb') as f : 
            f.write(data.content) 
   

   exec(open('main.py').read())

   return "1"

app.run()