# Paper Weight

![Responsive screenshot showing site on different screens](media/readme-images/paper-weight.png)

[Link to deployed site](https://paper-weight.herokuapp.com/)

## Introduction

Paper Weight is a full-stack Django website built using Python, Javascript, HTML and CSS. This web application is a full B2C e-commerce website for a fictional online stationery store. 

The site provides role based permissions for users to interact with a central dataset. It includes user authentication, email validation, full CRUD functionality for both users and admin users.

The users of the site can browse all products at once, filter specfic categories and search for a specific item. The search bar uses keyword searches so it will show the user a product if the desicription contains the word they were searching.

When a user finds a product that they want, they are able to click on the product image which will direct them to a page on the site which gives them more detail about the specific problem. They can decide to add it into their bag, with the ability of picking the quantity of the item or simply return to all the products. If the user decides later on that they want to change the quantity of the product they have selected they can either change it on the product detail page of from their shopping bag. 

At the checkout, the user will be prompted with a form in order to complete their transaction. If they are an authenticated user then they have an option to save their delivery info for more efficient future checkouts. The user can access any information they have submitted by going to their profile and from their they can update any incorrect information. When the purchase has successfully gone through, the user will recieve a email confirming their purchase, they will also recieve confirmation on the website and are able to see an order history on the profile page.

The payment system uses Stripe. (Please note this website is for eductional purposes only and the credit card payment functionality is not set up to take real payments.) When testing interactively, using the numbers 4242... for everyting will allow the payment to go through as it is a practice card.

