sp_test
==============

Interview Test

----------------------------------------------------------------------------------
USAGE
----------------------------------------------------------------------------------

These testcases were written using Python 2.7.4 on Ubuntu Linux. The git log shows that it was worked on over the course of 3 days, from Wednesday to Friday.

To run all testcases

(When in the parent folder of the folder with the testcases)
python -m unittest discover <folder-name-with-testcases> *.py

To run an individual test suite

(When in the folder with the testcases)
python <test-suite>.py

----------------------------------------------------------------------------------
TESTCASES
----------------------------------------------------------------------------------

There are 31 testcases in the sanity test plan.

They are the following:
* Add a comment when not logged in
* Add a comment when logged in
* Delete a commment
* Send a comment with a @reply
* Use the reply button to add a comment
* Flag a comment

* Contact the designer when not logged in
* Contact the designer when logged in

* Change country
* Change country to a non-existent country

* Favorite when not logged in
* Favorite when logged in
* Unfavorite when logged in

* Verify that the page loads

* Change material
* Close change material dialog box

* Verify permalink

* Change preview by selecting picture in list
* Change preview by selecting next button
* Change preview by selecting back button
* Change preview to interactable 3D model
* Change preview to youtube video

* Verify that the See More Link has a valid tag in it
* Verify related tag shares the same tag

* Verify tags list is accurate
* Verify product in tags listing

* Add to wishlist when not logged in
* Add to wishlist when logged in
* Remove from wishlist when logged in

----------------------------------------------------------------------------------
BUGS
----------------------------------------------------------------------------------

Two low severity issues were found on the page. They're summaries are below

When one attempts to go to the Contact designer page when not logged in, it takes you to the log in page, but doing anything else when not logged in takes you to the sign up page. they should be consistent. either they should all be sign up or all be login
ratings.py
When one has an item in the wishlist, and you click the added to wishlist link, it doesn't show up in the wishlist list, and you have to click the wishlist link again for it to show up

----------------------------------------------------------------------------------
CHALLENGES
----------------------------------------------------------------------------------

Most of the challenges were in addressed page elements that didn't have unique identier attributes. Most of the new XPath features that I learnt pertained to addressing items like this.

This is how I ended up with clever and/or unpleasant looking XPaths like these:
//strong[text() = 'chrisyeem_test']/../../../../div[@class='comment-body']/div[@class='comment-text']
//div[@id='favoriters']/following-sibling::div[1]/div[@class='grid-view']/div/div

Also was there a slight redesign of the product page while I was working on the testcases? The ratings feature disappeared while I was working on the testcases.

----------------------------------------------------------------------------------
FLAWS AND FUTURE CHANGES
----------------------------------------------------------------------------------

It's clear that a class needed to be written to encapsulate the operations of interacting with this web page for the sake of the code being DRY and abstracting away repeated code. I forsook that so I could get all the test coverage done by the end of the week. I will be creating that class over the weekend. I'll most likely resubmit an updated version with that encapsulation present

Same thing goes for data. The data like login information and tags are hard-coded into the testcases
