# The Crown Jewels Booking System

[View page deployed on heroku here](https://crown-jewels-5cd0c00fe74f.herokuapp.com/)

[View my github repo here](https://github.com/townsend75/Portfolio-4)


## The Crown Jewels

The Crown Jewels is a booking page for a fictitious London pub. Users can register with the site and then book tables in the restaurant via a booking page. It is also possible for logged in users to view, update and delete any bookings they have made. 

![Homepage Desktop](../Portfolio-4/static/images/Crown%20Jewels%20Homepage.png)
![Homepage Tablet](../Portfolio-4/static/images/Crown%20Jewels%20Home%20Tablet.png)
![Homepage Mobile](../Portfolio-4/static/images/Crown%20Jewels%20Home%20Mobile.png)


The site is has a simple opening page including a navbar with links depending on whether a user is logged in or not. If the user is logged in, they can book a table in the restaurant, view, edit and delete existing bookings and choose to log out. If the user is not yet registered, they can sign up and then use the features as well. There is also a brief description of the restaurant, opening times and links to the usual social media pages in the footer. The design is deliberately very simple, so as to focus on the functionality.. 




## Website Goals

### Customer Goals

- To be able to book a table for a specific date and time in the future

- To be able to alter the booking or delete it entirely, should circumstances change


### Business Goals

- Better planning capabilities through advance knowledge of bookings on any particular day

- Ability to see registered users and contact them ( possibly also for advertising purposes depending on permissions)


## Agile Planning

This project was developed using agile methodologies. Since the scope of the project was not huge in terms of user stories, I decided against using epics and milestones, concentrating instead on user stories on a Kanban board. The Kanban board can be found [here](../Portfolio-4/static/images/Kanban%20board.png)


## User Stories

### New User

- I want to be able to register as a user

- I want to be able to book a table once I have registered

### Existing Users

- I want to be able to login securely

- I want to be able to book a table

-I want the option of editing or deleting my existing bookings

- I want the option of following the restaurant on social media

### Site Administrator

- I want the pages to be easily manageable

- I need to see all the bookings in one place so that i can better plan my staffing and stock

- I need to be able to add and delete bookings through the admin site, should bookings be made by telephone or in person

_ I would like access to registered users email address so that I can contact them should something be wrong with their booking


##Design

### Colour

The site has a uniform sunny yellow #ece279 background. The header and footer are both dark  with light text for a pleasant contrast.

### Font Family

Roboto and Lato fonts are used throughout the site.


### Images


### Wireframes

Wireframes of the homepage were sketched out for desktop, tablet and mobile

![Wirefraome of desktop view](../Portfolio-4/static/images/Wireframe%20Crown%20Jewels%20Desktop.png)
![Wireframe of tablet view](../Portfolio-4/static/images/Wireframe%20Crown%20Jewels%20Tablet.png)
![Wireframe of mobile view](../Portfolio-4/static/images/Wireframe%20Crown%20Jewels%20Mobile.png)



## Features

### Landing Page

The landing page features a bootstrap carousel of images as well as a navbar and a footer. The navbar initially shows Home, Register and Login buttons. Once the user has registered or logged in, the navbar switches to offer "Logout", "Book a table" and" View my bookings" buttons. 

### Register
The register page offers new users a chance to register. There is also a prompt for user who are already members, directing them tho the sign in page. Registrees must create a username and a password.

### Sign in
The sign in page asks for username and password. There is also a redirect to the register page, if users are not yet registered.

### Book a table
Contains a form requesting name, email, number of guests, date and time of the booking. An alert tells the user that their booking was submitted successfully.

### View Your Bookings
Here the user can see all of the bookings they have made in a table. There are also two buttons, one to delete the booking and one to update it.The user is alerted that either of the two actions has been successfully completed. 

### Navbar
The navbar is present on all pages. Before a user logs in, the options are to register or to sign in. Once a user is signed in, the navbar shows options to logout, book a table or view/edit their bookings.

### Footer
The footer is present on all pages and contains links to the standard social media pages as well a the address of the gastropub.


## Future Considerations

- Given more time, I would devise a table containing the number of tables in the restaurant and could then avoid double bookings for larger parties as well as making it impossible to exceed a maximum customer capacity.

- In a real world scenario, I would add background images of the restaurant on all of the pages, particularly the form pages, which are currently slightly austere.

- A review section would be created, allowing customers to leave comments about their experience.


## Languages and resources

- [HTML](https://html.spec.whatwg.org/multipage/) - Markup language which makes up the contents of the site
- [CSS](https://www.w3.org/TR/css-2022/) - Used to style elements of the site
- [Bootstrap v5](https://getbootstrap.com)- Open source framework for mobile-first frontend development
- [Google Fontshttps://fonts.google.com]() - Source for the site's fonts
- [Github](https://github.com) - Repository for the code
- [Gitpod](https://www.gitpod.io) - IDE used to write the site code
- [FontAwesome](https://fontawesome.com/icons) - All icons on the site are from FontAwesome


## Testing

For all testing, please refer to the [testing.md](testing.md) file.

## Version Control

The site was created using Gitpod and pushed to the GitHub repository "Portfolio-4"

The following git commands were used throughout development to push code to the remote repo:

`git add <file>` - This command was used to add the files to the staging area before they are committed

`git commit -m "commit message` - This command was used to commit changes to the local repository queue ready for the final step

`git push` - This command was used to push all committed code to the remote repository on GitHub

## Deployment

The site was deployed to Heroku. The steps to deploy are as follows:

- Navigate to Heroku and create an account

- Click the new button in the right hand corner

- Select create new app

- Enter app name

- Select region and click create app

- Click the settings tab, followed by reveal config vars

- Add config vars to link postgres and cloudinary accounts, the port number and the secret key

- Click the deploy tab and select "connect to GitHub"

- Locate the repository you would like to connect to

- Scroll down and click the manual deploy button

### Run locally

Navigate to the github repository

- Click on the code dropdown button

- Click on HTTP5

- Copy the repository link to the clipboard

- Open your IDE of choice (git must be installed for the next steps)

- Type git clone copied-git-url into the IDE terminal

The project will now have been cloned on your local machine for use

Install Dependencies:

`npm install`

Run Application:

`npm start`

### Forking

Most commonly, forks are used to either propose changes to someone else's project or to use someone else's project as a starting point for your own idea.

- Navigate to the GitHub repository you wish to fork

- On the top right of the page under the header click the fork button

- This will create a duplicate of the full project in your GitHub repository





## Credits

Here is a list of resources that I have used to create my site. 

| Source | Location | Notes |
| ----------- | ----------- | ----------- |
| [Django Documentation](https://docs.djangoproject.com/en/4.2/) | Entire page | MVT research |
| [Bootstrap v5](https://getbootstrap.com) | entire site | Creating bootstrap forms and tables, centering objects, navbar |
| [Programming with Harry ](https://www.youtube.com/c/ProgrammingWithHarry) | Django Tutorial | Youtube channel which helped my understanding a django structures |
| [Stack overflow](https://stackoverflow.com) | Entire site | Very helpful for researching different solutions to many many problems |
| [Unsplash](https://unsplash.com) | Entire site | Royalty free photo stock. The restaurant images are all taken from here |




## Content

- The fonts used on this site are from Google Fonts

- Instructions relating to Github deployment come from Github's docs pages

- Icons in the footer come from Font Awesome

- Heroku deployment instructions were taken from the Heroku website


## Acknowledgements

- I would like to thank my mentor, Sheryl Goldberg for her invaluable help throughout this project. Countless tips and articles helped fill the gaps in my knowledge. 

- I would also like to thank the Code Institute tutors who helped me sort out multiple issues.

## Bugs and fixes

After initial submission, I was made aware of a security issue involving users being able to access and alter bookings not related to their own accounts by entering certain URLs. I resolved this issue by adding the @login_required decorator to the applicable views and also adding code making sure the user can only access booking made by themselves. If a user attempts to access a URL related to another booking, they are now redirected to the hompage and receive a message informing them that they do not have permission to view the requested page. 