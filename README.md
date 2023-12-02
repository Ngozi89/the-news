# News Mix

## Table of contents

- [News Mix](#news-mix)
  - [Table of contents](#table-of-contents)
  - [Purpose](#purpose)
- [UX Design](#ux-design)
  - [User stories](#user-stories)
    - [As a **first time user**](#as-a-first-time-user)
    - [As a **returning user**](#as-a-returning-user)
  - [UAC](#uac)
    - [Home Page](#home-page)
    - [Sign Up Page](#sign-up-page)
      - [User Goal:](#user-goal)
      - [Website Goal:](#website-goal)
    - [Sign In Page](#sign-in-page)
      - [User Goal:](#user-goal-1)
      - [Website Goal:](#website-goal-1)
    - [Posts Page](#posts-page)
    - [Post Detail Page](#post-detail-page)
    - [Create/Update Post Page](#createupdate-post-page)
    - [Delete Post Page](#delete-post-page)
- [Development Plan](#development-plan)
  - [Agile design](#agile-design)
- [Design](#design)
  - [Design](#design-1)
    - [Colour Scheme](#colour-scheme)
- [Features](#features)
  - [Auth (uac 1)](#auth-uac-1)
    - [User Authentication (uac 6)](#user-authentication-uac-6)
    - [Reset password (uac 18)](#reset-password-uac-18)
  - [Responsive (uac 1)](#responsive-uac-1)
  - [Accessibility](#accessibility)
    - [Navbar (uac 3, uac 4)](#navbar-uac-3-uac-4)
    - [Blog Features](#blog-features)
    - [Existing Features for users](#existing-features-for-users)
    - [Existing features for users](#existing-features-for-users-1)
    - [First step](#first-step)
      - [Step 2 Database](#step-2-database)
      - [Step 3](#step-3)
      - [Step 4](#step-4)
      - [Step 5](#step-5)
    - [Second step](#second-step)

## Purpose

The website is built using Django framework, which provides the backend functionality, such as user authentication, data management, and routing which handles the majority of the frontend. The website combines the power and flexibility of Django with the dynamic capabilities of React and WebSockets to deliver a smooth and responsive user experience.

The website provides all the essential features, such as creating a personal account, searching and filtering posts, the ability to add and manage posts, commenting on posts and liking or unlike any post.

The website was developed as a Milestone Project#4 for the Code Institute's Full Stack Developer course.

The live link to News Mix webpage can be found here - <https://thenews-527458e708d0.herokuapp.com/>

News Mix is a database-backed Django app for News and happenings around the world. News Mix is created with Design Thinking and Agile approch putting myself users position.
User story was created as a guideline in adding the blog functionality

# UX Design

## User stories

Target audiences:

- Aged 45 and above who are not too convansent with social media. (U)
- Individuals who are interested in reading news about happenings around the world (I)

### As a **first time user**

- I want to be able to access the website from any device.
- I want to easily understand the main purpose of the site and learn more about the topic.
- I want to be able to easily navigate and find content.
- I want to create my personal account to see posts.
- I want to create an account fast, but I want it to be secure.
- I want to easily access a category of posts I need and to be able to search through them.
- I want to open a post on a separate page to see all the details.
- I want to be able to create a post myself.

### As a **returning user**

- I want to be sure my data is protected.
-
- I want the server to recognise my device so I can login without entering my information again
-
- I want to access comments from any post on the website.

- I want to be able to access the navbar at any point or go back to the top to navigate fast.

- I want posts to be paginated so it helps me remember on what page I saw something interesting or stay on the same page if I accidentally refresh the page or there are problems with the internet connection.

- I want to be able to report comments that I find offensive, unsafe or inappropriate.
-
- I want the comments to be moderated, so I don't need to report it.

- I want to be able to write comments to give my opinion on any news

- I want to be able to update and delete my posts.

- I want to be able to reset my password if I forget it.

## UAC

User Acceptance Criteria based on the user stories:

<span id="uac1">1.</span> The website should be fully responsive and accessible on any device, including desktop, tablet, and mobile.

<span id="uac2">2.</span> The website should have a clear and concise homepage that display news.

<span id="uac3">3.</span> The website should have a clear and intuitive navigation menu that allows users to easily find and access the content.

<span id="uac5">4.</span> The website should have a registration form that allows users to create a personal account.

<span id="uac6">5.</span> The website should allow users to sign up with their existing social media accounts, such as Google or Facebook.

<span id="uac7">6.</span> The registration process should be fast and easy, but also secure, using encryption and other security measures.

<span id="uac10">7.</span> Each post should have a link that allows users to view it on a separate page, where they can see all the details and information about the post.

<span id="uac12">8.</span> The website should have a form that allows registered users to create their own posts.

<span id="uac13">9.</span> Each post should have a name of author that allows users know who publish news.

<span id="uac13">10.</span> Each post should display date and time of publication to that allows users know most current news.

<span id="uac14">11.</span> The website should have a user profile page that displays information about other users to allow other users know who wrote a particular comment.

<span id="uac16">12.</span> The website should have links to its social media pages, such as Facebook, Twitter, Instagram, etc.

<span id="uac21">13.</span> The website should have robust security measures in place to protect user data, such as encryption and secure servers.

<span id="uac23">14.</span> The website should divide the posts into pages so that users can easily navigate through them.

<span id="uac25">15.</span> The website should have a moderation system that reviews and approves or removes content that does not meet the standards of the website.

<span id="uac26">16.</span> The website should allow registered users to leave comments on posts, in order to share their opinion.

<span id="uac27">17.</span> The website should allow registered users to edit and delete their own posts, if they need to.

<span id="uac30">18.</span> The website should have a password reset feature that allows registered users to reset their password in case they forget it.

<span id="uac31">19.</span> The website should provide feedback about the status of the processes.

### Home Page

![]()

- Displays the main purpose and topic of the site.
- Addresses questions and doubts the first-time users might have and provides a registration form.
- Presents opportunities for possible further actions

* #### User Goal

    >
    > * Understand the main purpose of the website.
    > * Be able to signing up/in.
    > * Easily navigate and interact with the website.
    > * Access social media.
    >

* #### Website Goal

    >
    > * Inform the user about the main purpose.
    > * Engage the user.
    > * Call to action.
    > * Initiate future engagement, such as following on social media
    > * Provide aesthetically pleasing user experience.
    >

### Sign Up Page

![]()

- Allows to sign up.

  #### User Goal:

  > - Sign up.

  #### Website Goal:

  > - Allow the user to sign up easily.
  > - Provide aesthetically pleasing user experience.

### Sign In Page

![]()

- Allows to sign in.
  #### User Goal:
  > - Sign in.
  #### Website Goal:
  > - Allow the user to sign in easily.
  > - Provide aesthetically pleasing user experience.

### Posts Page

![]()

- Shows posts.
- Allows users to easily find and access posts.
- Allows opening each post on a separate page.
- Available only for authenticated users.

* #### User Goal
  > - Browse the posts.
  > - Easily find and access specific categories of posts
  > - Open posts to see them in detail.
* #### Website Goal
  > - Provide a list of posts.
  > - Provide comprehensive information on each post in a preview.
  > - Provide aesthetically pleasing user experience.

### Post Detail Page

![]()

- Shows a post in detail including an image.
- Allows to see and write comments about the post.
- Allows like and dislike post.
- Allows see the author name and published date.
- Allows you to manage the post if you are the author.
- Available only for authenticated users.

- #### User Goal
  > - See a post in detail.
  > - See comments other users left about the post.
  > - Leave your comments.
  > - Manage the post, if you are the author.
- #### Website Goal
  > - Show a post in detail.
  > - Allow the user to interact with the post.
  > - Provide aesthetically pleasing user experience.

### Create/Update Post Page

![]()

- Creates a new post.
- Allows updating an existing post.
- Available only for authenticated users.

- #### User Goal
  > - Create a new post.
  > - Update your posts.
- #### Website Goal
  > - Allow the user to create/update a post.
  > - Provide aesthetically pleasing user experience.

### Delete Post Page

![]()

- Confirms if the user wants to delete their post.
- Available only for authenticated users.

- #### User Goal
  > - Delete a post.
- #### Website Goal
  > - Confirm with the user deletion of the post.
  > - Provide aesthetically pleasing user experience.

# Development Plan

## Agile design

The development of the website has followed an Agile methodology, using GitHub's projects to prioritize and track user stories and features. The approach enabled the implementation of ideas based on their level of importance, ensuring that the website functionality and user experience were not compromised. The following categories were applied

- must have
- should have
- would have
- could have

![]()

![]()

# Design

## Design

The website is meant to have a simple layout and a clean design. The home page is aimed at giving a professional and informative impression.

### Colour Scheme

![Palette]()

The colour scheme is mainly red and white to create a visually appealing and cohesive design that is easily recognizable as being associated to news website.

# Features

## Auth ([uac 1](#uac1))

Authentication is particularly important for Help U, as the subject is quite sensitive and people are vulnerable asking for help, so it should be confidential within the community and available only for authenticated users. Thus the website, besides the home page is available only for authenticated users.

In a Django project, there are several ways to handle authentication and authorization. One of the most popular libraries [django-allauth](https://django-allauth.readthedocs.io/en/latest/), provides a flexible solution for handling user authentication and registration. It supports both traditional username and password authentication as well as social authentication through providers like Google, Facebook, and Twitter. It uses session-based authentication and stores user authentication information in the user's session, instead of Django's built-in token-based authentication. When a user logs in, the library creates a new session for the user and stores the user's identifying information (such as the user's ID or username) in the session. The library then sends a session ID to the client, as a session cookie, which the client stores in the browser. With each subsequent request, the client sends the session ID back to the server in the Cookie header of the HTTP request. django-allauth then uses the session ID to look up the associated session and authenticate the user.

One of the key features of [django-allauth](https://django-allauth.readthedocs.io/en/latest/) is its support for OAuth. OAuth is an open standard for authorization that allows users to share their private resources stored on one site with another site, without having to share their credentials. OAuth allows users to grant a third-party application access to their resources without having to reveal their password. This is useful for scenarios where users want to give access to their resources to a third-party application without having to provide their credentials.

One of the main reasons I chose to use [django-allauth](https://django-allauth.readthedocs.io/en/latest/) is because of its flexibility and support for various authentication methods. Another reason is because of its scalability. The library is built on top of the Django framework and it is actively maintained and widely used in production, which means that it is likely to be compatible with the latest Django versions and have a solid user base.

### User Authentication ([uac 6](#uac6))

![](signin.png)

The project uses Django's built-in User model, which means that users can register and log in to the website with email, username. However, users will not be logged in automatically after resetting their password. The ACCOUNT_SESSION_REMEMBER is set to True which means that the session will be remembered even if the user closes the browser.

### Reset password ([uac 18](#uac18))

The website also provides a password reset feature, which is an important security feature that allows users to reset their password if they have forgotten it or if their account has been compromised.

## Responsive ([uac 1](#uac1))

The website is designed with flexibility and aesthetic appeal in mind, ensuring that it is responsive and visually pleasing on all screen sizes and resolutions, starting at 350px.
Responsiveness was achieved by utilizing Bootstrap. This allowed for the rearrangement of page components to optimize the user experience on different screen sizes. Breakpoints were chosen based on typical device screen sizes and the goal of providing the best possible presentation of content for all screens. Breakpoints are not strictly consistent (\*particularly for smaller screens) but it is done intentionally to provide a better presentation of the content for all screens.

## Accessibility

The website is designed and developed with accessibility in mind: it provides alternative text for images, using semantic HTML elements, aria-labels and providing adequate colour contrast. Keyboard navigation is possible. It also works with screen readers, however, there's room for improvement in this aspect, to ensure that it is fully accessible to users with disabilities.

### Navbar ([uac 3](#uac3), [uac 4](#uac4))

![](navbar.png)

The navbar is a key feature of the website, located at the top of the page. It also include links that aid navigation on the website. The "Registration" link provides form for new users to register and the login allows users already registered users to login. The "Login" and "Register" links are used for user authentication and are only visible to unauthenticated users. Once the user logs in, they will not see these links anymore and "Log out" will be displayed instead.
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
