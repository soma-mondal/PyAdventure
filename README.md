PyAdventure is an adventure booking system based on Python 3.6 for the back-end and MySQL as a database. 

It is CLI based with all the functionalities of a modern app. It features a 3 way access as an admin, a registered user or as a guest, that can be accomplished via registration and login system with standard features like email and password verification, forgot password options and security questions. It also boasts a captcha system that prevents foreign scripts to scrap data from the database. 

This is divided into two phases: 1.For the End-User and 2.For the Admins

User's Perspective:

It features a list of adventures, from which you can browse, book or save for later. 

Browsing showcases the list of adventures, the needful details and prerequisites which will direct the user into choosing a suitable adventure.

On a booking, the adventure details are provided from the database and the process is initiated with acceptance of user details and booking credentials. Then a made up payment procedure is also setup which holds the feature such saving a debit/credit card as favorites native to the user only for future reference.

The saved for later literally saves your choice to view/book later in the database. It is unique for each user and all the other functionalities can also be initiated from the saved list.

The entire information can also be accessed in a "guest mode", so logging in isn't necessary but to continue with the booking or saving a particular adventure, requires a verified user login.

Admin's Perspective:

Apart from all the standard privileges of a standard registered user, the admin also enjoys a couple of more options. 

Admins can create/modify/delete adventures. Creation constitutes of a add-from-scratch approach where admins can add the adventure, its location(s), pricing, etc. In the modify part, admins are able to modify the small details of an already added adventure like location(s), pricing to editing an entire adventure. The deletion part is fairly simple, where the admins have the authority to delete an existing adventure.
