# AnimeWorld
This is a full-stack framework project built using Django, Python, HTML and CSS. My goal is to create a functioning and responsive website, that allows users to share posts about recent animes they have  watched.  This project has been built for entertainment purposes.

# Table of Contents
1. UX
2. Agile development
3. Scope
4. Structure
5. Wireframe
6. Database schema
7. Surface
8. Technologies used
9. Testing
10. Deployment
11. Credits

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

### Agile Development
While this is a solo project I aimed to follow the Agile methodologies by creating my user stories with issues on github and creating a kanban board to manage deadlines.
![image](https://github.com/user-attachments/assets/f802e19a-61f3-4f68-b670-67a78d92625f)
![image](https://github.com/user-attachments/assets/f6b04a2c-c339-4bb2-b5ad-b4be1a935a9b)




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
- ![image](https://github.com/user-attachments/assets/df7c80ea-937f-47b9-b086-e9de58f86b46)

##### Responsive Design
- Mobile-Friendly Layout: The website features a responsive design, ensuring a good user experience on both desktop and mobile devices.
- Bootstrap Integration: Utilizes Bootstrap for a modern and consistent UI.
  
##### Admin Panel
- Django Admin: Utilizes Django's built-in admin interface for managing users, posts, comments, and other site content.
- ![image](https://github.com/user-attachments/assets/c7c9ad96-c9f7-4adc-b746-fd616f98ec41)


### Database Schema
![Screenshot_19-7-2024_102714_dbdiagram io](https://github.com/user-attachments/assets/de494ce3-3bc1-4e2e-8202-50f27448c6e3)

### Surface
- The home page image is really important as it displays a plethora of characters in various animes all together in one space. It cultures the ethos of the website hence the colors chosen are to support this image.
- The color for the header I chose personally to be a deep gray (#535351) for consistency with the image. 
- For the background colour of the main content section I chose a ghost white (#f8f9fa) for contrast with the dark colour. 
- I intended for the AnimeWorld Logo and various buttons to be red especially because of the demographic the would be mostly made up of to engage with the fiery ideals of popular animes such as demon slayer. I plan to implement this in the future.

#### Bugs and Issues

My header was dissappearing when I deployed because I did not gather my static files properly 'I had to run the collectstatic command line in the terminal'
I couldn't upload an image when sharing a post because firstly my api key was incorrect it had '<>' around them which was needed to be removed, I then needed to make sure it matched the configuration variable settings on heroku.
My home page would not load because I forgot to add an endif tag. I figures this out by reading the error information provided when debug is set to True.
My share post function was not working when debug was set to false.
I raised an error with a debug output of status code 500. My browser would not load. This was because my get_success method was referenced wrongly 'get-success' in my form_valid method. I corrected this by removing the hyphen and adding the correct underscore syntax. 

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
The website’s source code is available on GitHub.

* Font Awesome
Social media links in the footer were enhanced with icons from Font Awesome.

* Bootstrap
Used for styling and making the website responsive  

* Postgres
Employed as the primary database for storing user data, posts, comments.

* Cloudinary
Utilized for managing and serving uploaded images.  

* Bootstrap

### Testing 
###### Functional
Description:

Ensure a user can sign up to the website

Steps:

Navigate to AnimeWorld and click Login/Register displayed on login main section and navigation tab.
Click 'Sign up' link
Enter email, username and password
Click sign up button which submits information
Expected:

They are directed to the home page and are displayed a message confirming success.

Actual:

They are directed to the home page and are displayed a message confirming success.

Description:

Ensure a user can sign out

Steps:

Login to the website
Click the logout button
Click confirm on the confirm logout page
Expected:

User is logged out

Actual:

User is logged out

Description

Ensure users can fillout and submit details required for the anime post

Steps: 
1. Click sharepost tab in navigation
2. Fill out the form
3. click submit

Expected:
User is redirected to browse page displaying their new post.

Actual
User is redirected to browse page displaying their new post.

Description 
We tested all the navigation links to make sure they take you to the right pages. This involved clicking on each link on every page to confirm they work as intended.

Steps:
Click the button/link for each page.
- Home -> index.html
- Browse -> blog_list.html
- SharePost -> share_post.html
- News -> news.html
- Post in detail(select post of choice) -> post_detail.html
- Logout -> logout.html in django accounts
- Login -> login.html in django accounts
- Register -> Signup.html in django accounts

###### Unit Testing 

![image](https://github.com/user-attachments/assets/ca7c74f3-5d1e-4cda-a761-6a3ff756165b)

###### HTML Validation 
![image](https://github.com/user-attachments/assets/e3e44fa4-d3d2-4ca2-82e2-6bc8e9dadbad)
![image](https://github.com/user-attachments/assets/12771181-7f90-4720-bb0e-969e496cb07d)
![image](https://github.com/user-attachments/assets/a96bad9e-76b2-4677-ac9b-68e586760a6a)
![image](https://github.com/user-attachments/assets/914e925c-6695-413e-90ac-39788d3a6750)

###### CSS Validation
![image](https://github.com/user-attachments/assets/ebc0a5e8-a895-446d-a977-85b1de93f9e8)






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







