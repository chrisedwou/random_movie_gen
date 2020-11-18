RANDOM MOVIE GENERATOR
----------------------
Author: Chris Edwards

-----Description-----
Random Movie Generator is a console based dynmaic webscraping program using the Selenium webdriver and ran_mov_scrape.py to collect titles, and othe useful information for movies from the Amazon Prime Video website and place them into a csv file. ran_mov_gen.py selects a random title based on genere.

-------How to--------
With python installed run:
$ python ran_mov_scrape.py

This will create the csv files.

Next run:
$ python ran_mov_gen gen [sci : hor : act : all]

gen followed by a second argument (either "sci" for science fiction, "hor" for horror, "act" for action, or "all" for any catagrory) will select a random movie based on genre.