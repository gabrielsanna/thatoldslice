# Project 3: Web Programming with Python and JavaScript

My Project 3 is **That Old Slice**, a site for a pizzeria! Users can view the menu and place orders, view their past orders, and add and remove things from the cart. Admins can view all past orders, and see if there are any pending orders.

## Database Schema

Setting up the database was a challenge. There are a lot of out-of-model edge cases that need to be accounted for. In my `migrations` folder, you'll find 24 iterations of the database; this is actually not accurate, as a few times I got migration errors and had to delete a couple migrations back.

My models for the `orders` app are as follows:

* **Entree** - All types of meals on the menu are stored as an `Entree`. It includes fields for the name, category, size, and price of the entree. Some of these fields are dropdowns with limited options.
* **PizzaTopping** - The toppings available to put on pizzas. The only field is the topping's name.
* **SteakCheeseTopping** - The toppings available to put on a Ssteak and Cheese sub, the only sub that gets toppings. These toppings relate to pizza toppings to share names, but they have an additional field for price (since adding them costs money).
* **CustomerOrder** - This model store each individual order submitted by a user. The contents of the user's cart constitute an "unsubmitted" order. The model contains datetime fields for when the order is created, submitted, and updated, booleans for whether it is submitted and ready for delivery, and relationships for the user submitting it and the meals included in the order.
* **MealsInOrder** - This model is a customized ManyToMany relationship between `CustomerOrders` and `Entrees`. This allowed me to add additional fields to each meal included in an order. The additional fields are themselves ManyToMany relationships with `PizzaTopping` and `SteakCheeseTopping` to determine the toppings on each instance on a meal in an order.

## Python Files

Back-end functionality is provided by the following `.py` files in the `orders` app.

* **\_\_init.py\_\_** - This is a blank file that indicates to Python that this directory can be used to `import` .py files.
* **admin.py** - Registers certain models for viewability on the `/admin` site.
* **apps.py** - List of registered Django apps. I did not modify this.
* **models.py** - Contains the full spec of all the models used for the database schema. See above for a full description.
* **tests.py** - File for automated testing. This was beyond the scope of the assignment and I didn't have time to implement any.
* **urls.py** - Contains the paths registered and their corresponding view functions.

## HTML Templates

There are several HTML templates included in the project, found in the `templates/orders` directory.

* **access-denied.html** - An alert page for when users try to directly access resources they're not allowed in. Includes a link to go back.
* **all-order.html** - A page to show all submitted orders, viewable only by superusers. Also used to mark orders as complete when they're "done cooking".
* **cart.html** - Shows the contents of the logged-in user's cart.
* **index.html** - The homepage of the site. Includes a hero image and a list of the logged-in user's pending and past orders.
* **master.html** - This is the master layout template, extended by all the other templates. It includes links to external resources including Bootstrap 4.
* **menu.html** - The menu with buttons to add items to cart. If a logged-out user tries to click these, they are redirected to the login page.
* **orders.html** - This page shows all the past orders for the logged-in user.
* **register.html** - A custom template for Django's registration form, allowing me to style it with Bootstrap.
* **single-order.html** - A page to show the details (all items and prices) for a single order. Redirects to the access-denied page if the user is not authenticated or doesn't have access.
* ** submitted.html** - A success page to tell a user that their order has been submitted.

## Static Resources

There are several resources in the `static` directory.

* **img/** contains several icons, from https://glyphicons.com. Also contains the homepage's hero image and the navbar brand.
* **styles.css** contains any hand-written CSS styles.
* **access-denied.js** - A script for the back button on the `/access-denied` page.
* **menu.js** - A somewhat lengthy script for setting up all the listeners on the `/menu` page. Much of the logic is devoted to handling meals with toppings, which would have been difficult to organize with normal HTML forms.

## Personal Touch

The personal touch for the project involves the ability for admins to easily see new orders and mark them as complete once preparation is finished.

* When a new order is submitted by any user, a red notification appears on the upper right corner for logged-in admins.
* Clicking on the notification leads to a page with the full list of past orders. Incomplete orders are clearly marked and can be marked as complete when they're done.
* Logged in users who have submitted orders see them listed as "Pending" on the homepage. Once an admin marks the order as complete (it's on it's way!) it will drop down into "Completed" orders.

## Access Information

I've set up an admin account you can use to get the full experience (and create other accounts if needed). Credentials are as follows.

* Username: cs33a
* Password: Veritiserum1