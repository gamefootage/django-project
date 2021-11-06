## This is the final Milestone Project, from Ben Kelly.

### A Online E-commerce Store designed for the fictitious company named "Jersey Rewind"

#### An online store setup for an imaginary company that sells throwback jerseys of 3 main sports (basketball, American football, and football). The owner of the company wants to be able to reach a global market, and believes that an online store is the way to do this.

# UX

## Goals

### Visitor Goals


The target audience to the web store would be:
- Fans of sports fashion
- People with high interest in sports
- People who cannot purchase these unique Products in their own country
- People who are too busy to visit the actual stores where these items may also be sold


### User Stories:
As a new User to this website, I want to:
* be able to view the range of products for sale in this store, online.
* be able to purchase these products, and pay for them online.
* be able to easily navigate around the website.
* be able to add a product (or more than one) to a cart, but have the option to continue to look in the shop section, before I decide to pay.
* be able to search through the many items in the online store, to narrow down the items that are of interest to me.

### Wireframes: 
* The wireframes were handdrawn and can be found by click on each link below:
[Homepage wireframe](./docs/home_wire.jpg)
[Products wireframe](./docs/products_wire.jpg)
[Checkout wireframe](./docs/checkout_wire.jpg)

## Features

### Layout
This is a multi-page layout, but designed with simplicity in mind. There are three different templates used:
1. Base template for the home page, login, logout, register, forgot password
2. Products template used for the display of the products for sale.
3. Cart template used for the cart, checkout and payment forms.

I was going for clean and simple after feedback on my previous projects. In design, sometimes less is more.


### Buttons
The buttons are big, bright and simple. They are mainly Green, Red or Blue. Each button has text or an icon with a label to describe it's purpose.

### Font
The font used is a google font, called "Georama". It is a visually appealing fonts, easy to read and give a nice finish to the web store.

### Existing Features

#### Navigation Bar
* Navigation Bar - This is on the top of every page on the site. In tablet and mobile view, it becomes a collapsable sidebar. 

On large devices, the left hand side has the logo of the company, and when clicked, will return the user to the home page. The rest of the navigation items on the left hand side are:

1. Home
2. All Products
3. Collections

On the right hand side of the navigation bar:
1. Search
2. My Account
3. Cart

(When the Superuser has logged in)
1. Product Management Login

#### The Footer

The Footer is on every page. The footer has been kept clean and simple. There is a link to contact the company. Also included at the bottom of the logo is Copyright 2021 & name of the developer.

#### The Register Page

When a user is not logged in, the register nav item appears in the Nav bar. A user will be able to register, via the register form on the register page. If a user with an account, finds themselves on this page by mistake, they are guided to click "HERE" to direct them to the login page. Within the register form, are fields for email address, Username, Password and Password Confirmation. You can also login with google.

#### The Login Page

The login page features a standard login form asking for username and password. It does have the option to reset your password, if you have forgotten it. By clicking on the "I forgot my password" button, the user will be directed to another page where they must input their email address. The user will be emailed a set of instructions of how to reset their password. There is also an option for users that find themselves on this page, that don't have an account. If they click HERE, they get redirected to the register page. You can also login with google

#### The Cart Page

The Shopping cart page features a summary of all the items the user has added to their cart. Each Product has a thumbnail picture, to remind the user of their purchase. There is a price value for each product that has been added to the cart. There is also a quantity value, and an option to amend that quantity value. There is a size value and the option to change it too. If the user decides they want to remove that product, there is a remove button. The total at the bottom give the total amount that all the items come to. Below this value, is the button to "Secure checkout".

#### Checkout

The checkout section is quite similar to the cart section, with the main exception that the user is not able to alter their products picked for purchase and there's a payment form on the left.
To the left of the Order summary, there is the payment section, where the users card details and billing address can be entered to purchase the products. Once Submit payment is clicked, the user is directed to the home page, and a message should be displayed to advise the user if their payment was accepted or not. 

### Features Left to Implement
* Product Review Page, where previous customers and existing and previous users of the web store can give feedback on items purchased.

* A wishlist, where the user can pick products and "favorite" them, before deciding to add them to the cart or not. The user can click on the wishlist link and review the products they have favored. This saves time and gives the user a better user experience overall.

* A section on the homepage showing the most popular purchased products at that current time.

* Toast notification with cart summary inside it.

## Main Technologies Used

### Languages used

* This project uses **HTML**, **CSS**, **JavaScript**, and **Python** programming languages.

### Tools used

* **Balsamiq** to create the wireframes for this project.
* **Visual Studio Code by Microsoft** - This was used as the IDE for building the application. This was my second time using a local IDE for a Milestone Project. 
* **Django** as python web framework rapid development and clean, pragmatic design.
* **Git** to handle version control.
* **GitHub** to store the project code remotely.
* **PIP** for installation of tools needed in this project.
* **Stripe** as payment platform to validate and accept credit card payments securely.
* **Heroku** for deployment
* **AWS S3 Bucket** to store static files in the cloud.
* **Django Crispy Forms** to style django forms.

### Libraries utilised

* **Google Fonts** to style the website fonts.
* **Bootstrap 5 and Icons** to simplify the structure of the website and make the website responsive easily, also provides sleek and simple icons.
* **jQuery**

## Databases

### Databases used

Django normally works with SQL databases and comes prepacked with sqlite3. During development on my local machine I worked with the standard sqlite3 database installed with Django. On deployment, the SQL database provided by Heroku is a PostgreSQL database.

### User Testing

#### Manual User testing:
This was the primary method of testing the application. People were asked to visit the website on a variety of devices, to setup accounts within the web store and to purchase items in the store. This feedback was very useful to determine any bugs that may have been present. I also tested the app manually myself on a varietly of browsers.


### Below are the list of Internet Browsers that were used to test the display of the website:

1. Google Chrome (Version 77.0)
2. Mozilla Firefox
3. Microsoft Edge

Manual testing was carried out using the above browsers. No bugs or desplay issues could be identified. 

### Below are the list of websites I used to test the HTML, CSS and JS code:

1. [W3C HTML Validator](https://validator.w3.org/) This is a HTML online validitor.
2. [W3C CSS Validator](https://jigsaw.w3.org/css-validator/) This is a CSS online validitor.
3. [CSS Lint](http://csslint.net/) CSS Lint is an open source CSS code quality tool I used.

#### Meeting the needs of the user stories (as described in the UX section of this README file)

#### As a new User to the web application, I want to be able to view the range of products for sale in this store, online.

If the User navigates their way to the "All Products" Nav-Item, in the NavBar, they will be directed to the products page, where all items are displayed.

#### As a new User to the web application, I want to be able to purchase these products, and pay for them online.

When the user adds items to the cart, and proceeds to payment at the bottom of the cart page, they will be directed to the checkout page where they will be shown a summary of their products and payment details are taken below via the Stripe form.

#### As a new User to the web application, I want to be able to easily navigate around the website.

The webstore has been setup so that there is no confusion when a user visits the site. The Nav bar is of a neutral color, the Nav items are clear text.

#### As a new User to the web application, I want to be able to add a product to a cart, but have the option to continue to look in the shop section, before I decide to pay.

In the cart section of the webstore, there is an option for the user to "amend" their quantity of their pre-purchased products. This can only be done from the cart section. 

#### As a new User to the web application, I want to be able to search through the many items in the online store, to narrow down the items that are of interest to me.

In the NAVBAR, the user can use the search bar, to narrow down the items, according the the keyword entered. If no keyword is entered, all products will be displayed. 

## Known Issue

#### Google needs a privay policy to expand past a test account which I don't have, so I will have to add google emails as test emails for them to work

## Deployment

### Local Deployment

This project was developed using the Visual Studio Code IDE, committed to git and pushed to GitHub using the built in function within Visual Studio Code.

The GitHub Repository is here:https://github.com/gamefootage/django-project/
The application is live here: https://jersey-rewind.herokuapp.com/

To deploy this project locally, on your own IDE, folow the steps below:

 Firstly, ensure of the following:
    - You have an IDE, such as VS Code.
    - The following must be installed locally on your computer:
        1.  git
        2.  PIP
        3.  Python 3
            
    - You will need to have accounts (free if possible) setup on the following:
        1.  Stripe
        2.  AWS(For S3 Bucket Services)
        3.  EmailJS
        4. Google API

Instructions for Installation:

1. Make your own folder and navigate to it on the terminal. Then enter the following in the terminal:

```
$ git clone https://github.com/gamefootage/django-project/

```
2. Open your locally installed IDE, unzip the downloaded file and open the terminal window.

3. Create a virtual environment
```
$ python -m venv env

```
4. Now activate that environment

```
$ env\scripts\activate
```
5. Install all required modules onto a .txt file with the command:
```
$ pip3 freeze --local > requirements.txt
```
6. Add a .env file with the following parameters
```
HOSTNAME = "127.0.0.1"
PORT = "8080"
DB_USER = "jr_admin"
DB_PASSWORD = "z1nf4nd3lll"
DATABASE_URL = "postgres://ajdpqlxbnczcbw:02aa441b4edeb2a22e853fc3ac586f0e09db3ba5e8b6d6b8882f64bf7e26da0c@ec2-18-232-216-229.compute-1.amazonaws.com:5432/d1akbvif72qjgp"
SECRET_KEY = "fy%3_&qpvt5uaat#f$%znpnw(@q-u*eczs=&^+va2s$w87dv*e"
DEVELOPMENT = True
AWS_ACCESS_KEY_ID = "AKIAVDF2BIVYPNVZ3AXC"
AWS_SECRET_ACCESS_KEY = "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"
STRIPE_API_KEY = "sk_test_51JsRklHhxonCNb5yv2OE5bxQlHk1pgkGJL1a8hCVK6OZPGzmj4dc4m7IBBwq040CPHX2VgiZwy5JFTRfkx0sQnrH003MiHrvNb"
STRIPE_PUBLIC_KEY = "pk_test_51JsRklHhxonCNb5yuxsy8wgL1LCYRVSfZfOguqma5VIBxePaQ16FNoYDJ4CXQEDDSISwAI0oxq7RoZHJkH8EsqNQ00T6OiKnFO"
STRIPE_WH_SECRET = "whsec_1DsxJcupfC6u6E4y26kmIwXr6eZA6toL"
```
* Special Note: "DEVELOPMENT" environment variable is set only within the development environment, it does not exist in the deployed version, making it possible to have different settings for the two environments. For example setting DEBUG to True only when working in development and not on the deployed site.

6. You can now run the program locally with the following command:
```
$ python manage.py runserver
```
### Heroku Deployment

To deploy this web store to Heroku, take the following steps:

1. Create a `requirements.txt` file using the terminal command `pip freeze > requirements.txt`.

2. Create a `Procfile` with the terminal command `echo web: gunicorn jersey_rewind.wsgi:application > Procfile`.

3. `git add` and `git commit` the new requirements and Procfile and then `git push` the project to GitHub.

3. Create a new app on the [Heroku website](https://dashboard.heroku.com/apps) by clicking the "New" button in your dashboard. Give it a name and set the region to whichever is applicable for your location.

4. From the heroku dashboard of your newly created application, click on "Deploy" > "Deployment method" and select GitHub.

5. Confirm the linking of the heroku app to the correct GitHub repository.

6. In the heroku dashboard for the application, click on "Settings" > "Reveal Config Vars".

7. Set the following config vars:

`"DEVELOPMENT": "1",`
`"SECRET_KEY": "enter your own value here",`
`"DB_USER": "enter your own value here",`
`"DB_PASSWORD": "enter your own value here",`
`"STRIPE_WH_SECRET": "enter your own value here",`
`"DATABASE_URL": "enter your own value here",`
`"STRIPE_PUBLIC_KEY": "enter your own value here",`
`"STRIPE_API_KEY": "enter your own value here",`
`"AWS_ACCESS_KEY_ID": "enter your own value here",`
`"AWS_SECRET_ACCESS_KEY": "enter your own value here"`

8. In your heroku dashboard, click "Deploy". Scroll down to "Manual Deploy", select the master branch then click "Deploy Branch"
9. Once the build is complete, click on the "View app" button.

The app should open in a new tab.

## Credits

### Content
All text in this project was written by the developer.

####Credits:
##### Code
1.       Crispy forms
2.       https://favicon.io/favicon-generator/
3.       https://simpleisbetterthancomplex.com/tips/2016/09/06/django-tip-14-messages-framework.html
4.       https://www.w3schools.com/ (product card template)
5.       https://bootstrapious.com/ (shopping cart template)



### Media
- The background and product images were sourced from various locations on Google Images 


### The content of this website is for educational purposes only. 
### Thank you.