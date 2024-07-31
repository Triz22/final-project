# AnimeWorld
This is a full-stack framework project built using Django, Python, HTML and CSS. My goal is to create a functioning and responsive website, that allows users to share posts about recent animes they have  watched.  This project has been built for entertainment purposes.

# Table of Contents
1. UX
2. Scope
3. Structure
4. Wireframe
5. Database schema
6. Surface
7. Technologies used
8. Testing
9. Deployment
10. Credits

## UX

Using the core UX principles I first started with Strategy, thinking about the target audience & the features they would benefit from.

The target audience for 'AnimeWorld' are:

* is inclusive of all age groups however targets the younger demographic between 12-18
* everyone who is looking for new animes to watch.
* people who like to talk about their experience with others
  
These users will be looking for:

* An fun website, with information allowing them to further explore their interests supported by the opinions of others
* A website that clearly displays the range of animes being watched by the community
* Ability to make a user account in order to interact with the site content
* Ability to post, comment and like posts
* This website will offer all of these things whilst also allowing for intuitive navigation and conformability of use.

### User Stories 

* As a registered user, I want to comment on blog posts and to engage in conversations and share my opinions.
* As a logged-in User I can like and unlike posts so that I can identify which animes I might explore in the future.
* As a user, I would like to view a blog post likes so that I can find the most interesting one.
* As a mobile user, I want the site to be responsive so that I can easily browse and interact with the blog on my smartphone or tablet.
* As a user, I want to embed and watch images/trailers within blog posts so that I can get a visual preview of the anime being discussed.
* As an anime enthusiast, I want to stay updated with the latest news and releases in the anime industry so that I don't miss out on new shows and events.
* As a user, I want to see if the anime in discussion would be recommended alongside ratings from other users to help me decide whether an anime is worth watching.
* As a writer, I want to publish blog posts so that I can share my insights and opinions on various anime series with the community.
* As a User, I can register for an account so that I can interact with the site content.
* As a User, I can log in/out off my account if I wish so that I can connect or disconnect from the website.
* As a User, I can easily navigate through the site so that I can view desired content.
* As a site Admin, I can access the admin panel so that I can manage posts,comments and news content.

### Scope
#### Features Implemented

##### Home page 
- Welcome Image:
The home page features a vibrant and engaging image of popular anime characters, instantly capturing the essence of the AnimeWorld blog. This image serves as a visual introduction, setting the tone for the content and community spirit of the site.
- Welcome message:
A text box beside the image welcomes visitors, encouraging them to join the AnimeWorld community by logging in or registering.

![image](https://github.com/user-attachments/assets/9233cfd8-7042-458b-801b-ff2acd0d5d16)


##### User Authentication and Authorization
- User Registration and Login: Secure user registration and login functionality, allowing users to create accounts and access personalized features.
- Users can see that they're logged in when they receive a success message at the top of the screen and the last two elements of the navigation bar change to one 'logout'
  ![image](https://github.com/user-attachments/assets/f163553b-38c5-4d65-9e2b-d27a7fe36330)

##### Post Management
- Create, Read, Update, and Delete (CRUD) Posts: Users can create new posts, view detailed post pages, edit their posts, and delete them if necessary.
- Users can see their post has successfully been created as they are redirected back to the browse page.
- Image Upload: Users can upload images to accompany their posts.
- ![image](https://github.com/user-attachments/assets/d29685b8-0cbb-4824-a2bd-1993bc6a2335)
- ![image](https://github.com/user-attachments/assets/ceb6c07e-eb18-4492-8b4d-a06faa1fcb48)
- ![image](https://github.com/user-attachments/assets/9775abbd-0335-4ea5-bf36-7042c0d8d9b6)
 
##### Comments
- Comment on Posts: Authenticated users can leave comments on posts, fostering community interaction.
- Display Comments: Comments are displayed on the post detail page, showing the author and timestamp.
- ![image](https://github.com/user-attachments/assets/79bcab8a-242f-4bc1-8cf9-b295c64d2386)


##### Likes
- Like/Unlike Posts: Users can like or unlike posts to show their appreciation.
- Like Count: Display the total number of likes each post has received.
- ![image](https://github.com/user-attachments/assets/e62200e6-0f98-4b0f-8d87-c8c8cac6399f)


##### Post Recommendations & Ratings
- Recommendation Indicator: Posts can be marked as recommended by the author.
- Display Recommendation: A clear indicator shows whether a post is recommended or not.
- Anime Ratings: Users can rate animes, providing more insight on their experience of animes.
 ![image](https://github.com/user-attachments/assets/df7c80ea-937f-47b9-b086-e9de58f86b46)

##### Responsive Design
- Mobile-Friendly Layout: The website features a responsive design, ensuring a good user experience on both desktop and mobile devices.
- Bootstrap Integration: Utilizes Bootstrap for a modern and consistent UI.
  
##### Admin Panel
- Django Admin: Utilizes Django's built-in admin interface for managing users, posts, comments, and other site content.
- ![image](https://github.com/user-attachments/assets/c7c9ad96-c9f7-4adc-b746-fd616f98ec41)


### Database Schema
![Screenshot_19-7-2024_102714_dbdiagram io](https://github.com/user-attachments/assets/de494ce3-3bc1-4e2e-8202-50f27448c6e3)

### Surface

#### Bugs and Issues

My header was dissappearing when I deployed because I did not gather my static files properly 'I had to run the collectstatic command line in the terminal'
I couldn't upload an image when sharing a post because firstly my api key was incorrect it had '<>' around them which was needed to be removed, I then needed to make sure it matched the configuration variable settings on heroku.
My home page would not load because I forgot to add an endif tag. I figures this out by reading the error information provided when debug is set to True.
My share post function was not working when debug was set to false

### Technologies used
* Gitpod
The website was developed using the Gitpod IDE.

* HTML
HTML served as the primary language for constructing the website’s structure.

* CSS
Styling for the website was applied using a separate CSS file.

* Python
Python was utilized in the development of the application.

* Git
Version control was managed with Git, including regular commits and pushes during development.

* GitHub
The website’s source code is available on GitHub and deployed via GitHub Pages.

* Font Awesome
Social media links in the footer were enhanced with icons from Font Awesome.

* Bootstrap

* Postgres

* Cloudinary 

* Bootstrap

### Deployment 
#### Github Deployment 

The website was developed using Gitpod and uploaded to the 'final-project' repository on GitHub.

The following Git commands were used during development to push the code to the remote repository:

git add [file]: Added files to the staging area before committing.
git commit -m [commit message]: Recorded and saved changes to the local repository.
git push: Uploaded all committed changes to the GitHub repository.

#### Heroku 

- Open the Heroku website and click "New" to create a new app.
- Provide an app name and region, then click "Create app".
- Navigate to "Settings" and click on "Config Vars". Add the following configuration variables:
 1. DISABLE_COLLECTSTATIC: 1 2. SECRET_KEY: (Your secret key) 3. DATABASE_URL: (Your database URL)
4. CLOUDINARY_URL: (Your Cloudinary storage URL) 
- Go to the "Deploy" tab, select "GitHub" as the deployment method, enter the repository name, and connect.
- Under "Manual Deploy" at the bottom of the page, select the "main" branch and click "Deploy Branch".
- Once the deployment process is complete, the app will be live on Heroku after a short wait.

### Credits







