# The Crown Jewels Booking System

[View page deployed on heroku here](https://crown-jewels-5cd0c00fe74f.herokuapp.com/)
[View my github repo here](https://github.com/townsend75/Portfolio-4)


## About the site

The site is has a simple opening page including a navbar with links depending on whether a user is logged in or not. If the user is logged in, they can book a table in the restaurant, view, edit and delete existing bookings and choose to log out. If the user is not yet registered, they can sign up and then use the features as well. There is also a brief description of the restaurant and links to the usual social media pages in the footer. The design is deliberately very simple, so as to focus on the functionality.. 

## Website Goals

### Customer Goals

- To be able to book a table for a specific date and time in the future

- To be able to alter the booking or delete it entirely, should circumstances change


### Business Goals

- Better planning capabilities through advance knowledge of bookings on any particular day

- 

-

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


## Deployment

The site was deployed to GitHub Pages. The steps to deploy are as follows:

- In the [GitHub Repository](https://github.com/townsend75/Portfolio-4), navigate to the Settings tab
- From the source section drop-down menu, select the Main Branch, then click "Save".
- The page will be automatically refreshed with a detailed ribbon display to indicate the successful deployment.

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


## Acknowledgements

- I would like to thank my Code Institute mentor, Sheryl Goldberg for her valuable support

- I would also like to thank the Code Institute tutors who helped me sort out multiple issues