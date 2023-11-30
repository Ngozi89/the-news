# News Mix

The live link to News Mix webpage can be found here - <https://thenews-527458e708d0.herokuapp.com/>

News Mix is a database-backed Django app for News and happenings around the world. News Mix is created with Design Thinking and Agile approch putting myself users position.
User story was created as a guideline in adding the blog functionality

## Features

### Blog Features

    . The application is hosted on - <https://heroku.com/>
    . Database - <https://elephantsql.com/> was used as external database
    . Heroku PostgreSQL is used to store the blog posts, comments and likes.
    . Cloudinary is used to stor blog's images

### Existing Features for users

    . Users can register an account, signin and signout
    . Users and view and open news on the blog.
    . Users can like and unlike a post.
    . Users can comment on a post.

### Existing features for users

    . There is full fuctioning admin panel where 
    . Admin can draft a post and save to contiune later
    . Admin can manage posts
    . Admin can approve and disapprove comments

This project was deployed using Code Institute's mock terminal for Heroku and the steps for deployment are as followed:

### First step

    . Sign in to Heroku app
    . Create a new app with a unique name

#### Step 2 Database

    . Create account on ElephantSQL.com and create new instance
    . Select a plan name and choose tine turtle (free)
    . Select region and review to make sure everthing is setup correctly
    . Click create instance at the down right side of your windown.
    . Click on the database you just created and cope the URL
    . On the IDE in codeanywhere create a file env.py, tehn import os and create os.environ with DATABASE.URL variable and set the copied url from as the value.
    Create another os.enviro and set the variable SECRET_KEY and create your sectret key

#### Step 3

    . Open setting.py and import os at the top then add the database url, add the env.py file, scroll down and change the secret key value to os.environ.get('SECRET_KEY')
    . Make sure the env.py file is on gitignore so it won't be commited to github.
    . You can use git status to check which files that will be commited to github and make sure the env.py file is not amoung.
    . Comment out the existing DATABASE on setting.py and create another Database and set it to
     'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))

#### Step 4

    . When this is done migrate to see everthing is okay, then return to Heroku and
    . Go to setting and reveal _Config Var_. Add a new key clalled DATABASE_ URL and the value will be the copied url database created earlier.
    . Add another config var key SECRET_KEY and paste the secret key that's added on the env'py file.
    . To improve compatibility with various Python libraries add anothe config var PORT and the value set to 8000

#### Step 5

    . Create a free Cloudinary account.
    . Go to your dashboard and cope the API Enviroment Variable. This is used to connect the app to Cloudinary.
    . Add another os.enviro on env.py file and add the CLOUDINARY_URL and the vlaue is the API Enviroment Variable copied from Cloudinary.
    . Go back to Heroku and add another config var key and paste the Cloudinary api.

### Second step

  Click on deploy at the top left side and select github to connect to github. Confirm your connection to github and search for the github repository name, click connect to link up the Heroku app creacted ealier with the repository.
    . Choose either automatic deploy or manual. I used manual which is deploy branch.
    . Allow the app to build until it shows successful then click view and it takes you to the deployed link.
