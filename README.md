DJANGO API BASED CMS APP

Step 1: Make a dir with any desired name and type the below command :
 $ git init

 Step 2 : Now add or clone the repository, use the following command to do that

For add the repo link ( recommended )
 $ git remote add origin https://github.com/dev-codflaw/django-cms-app.git

For clone the repo
 $ git clone https://github.com/dev-codflaw/django-cms-app.git

 Now you can check through the below command:

 $ git remote -v

 output: 

origin	https://github.com/dev-codflaw/django-cms-app.git (fetch)
origin	https://github.com/dev-codflaw/django-cms-app.git (push)

Now pull / copy the repo data

$ git pull origin master

Step 3 : Now create the virtual env dir using the following commands:

$ python3 -m venv env

$ source env/bin/activate

$ pip install - r requirements.txt

Step 4 : Now create three files for production server for security purpose

$ touch siteconf.py emailconf.py dbconf.py

$ using the nano command edit and paste your credentials 

$ python manage.py migrate

$ python manage.py runserver
