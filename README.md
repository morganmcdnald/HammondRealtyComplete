# Hammond Realty

Link to deployed site:
[hammondrealty.herokuapp.com](hammondrealty.herokuapp.com)

## Description

This is a real estate agency website that I created using the Django Framework. I created this full-stack web app as part of my personal portfolio in order to showcase my skills in different areas of the web design and development process.


## Technologies Used
- HTML
- CSS
- JavaScript
- Python
- Django Framework
- PostgreSQL


## Features
- User Accounts - Register/Login/Logout
  - I used the Django CSRF Tokens for this functionality. The navbar displays different depending on whether or not a user is logged in. Also, when a user registers for an account they are auto assigned a role without permissions to the admin area.
- Dynamic Content
  - All content on the site is loaded from the PostgreSQL database, where many of the tables like through foreign keys. Content can be updated through the admin panel and changes will be reflected instantly.
- User Functionality
  - There is functionality reserved specifically for logged in users. This includes adding a listing to a list of favourites, adding a blog post to a list of favourites and leaving a comment on a blog post. Functionality for all users includes submission of a contact form on the home page and the submission of an enquiry about a listing. If a user is logged in when performing any of these actions, their submissions can be viewed from a user account page.
- Search
  - There are 2 searches implemented in the site, one for each of listings and blog posts. Both searches support multiple parameters for specific results.
- Page Design
  - I used Bootstrap for the bulk of the CSS design along with a fair amount of custom styles. With the HTML I made use of base.html and templates for each page, as well as partials for the recurring sections of pages like the navbar and footer.

## Disclaimer
This is an unofficial site and is completely unaffiliated with the show 'Santa Clarita Diet' or its distributor and property owners 'Netflix'. This site was created as a showcase for my personal portfolio only with no commercial intentions. No copyright infringement is intended.

Links to all images used in the site can be found in a downloadable text file in the footer of the site, viewable on every page.
