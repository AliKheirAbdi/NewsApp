# Project
the TRIBUNE

## By:
Ali Kheir

## Email: 
akheirali(at)gmail.com

# Project Description
A Flask application that help one list and preview news articles from various sources. 
This is achieved by using the [News Api](https://newsapi.org/)

# Set up instructions
1. You need to have python3.7 installed, venv and pip
2. Set up the virtual environment and activate it.

    
    $ python3.6 -m venv virtual


    $ source virtual/bin/activate


3. Install all modules required

    $ pip install flask


    $ pip install flask-bootstrap


    $ pip install flask-script



4. Get an Api key from the [News Api](https://newsapi.org/)
5. Create an instance folder ```mkdir instance``` in the root directory and navigate to it ```cd instance```
6. Create a config.py file in the instance folder ```touch config.py```
7. Open your editor and add ```NEWS_HIGHLIGHT_API_KEY = <your apikey>``` to the config.py file
8. To run your application, in the terminal run ```$ chmod a+x start.sh``` command
9. Followed by ```$ ./start.sh``` command
10.Launch in the server to view the application

# Development
Want to contribute? Great!
* Fork the repo
* Clone the repo in your machine but ensure you have all the necessary modules.(You can find them in the set up instructions above)
```https://github.com/AliKheirAbdi/NewsApp.git```
* Create a new branch ```git branch contributions```
* Edit your changes in your branch
* Run the application

### Known bugs
As the yet the app has no known bugs.
If you find a bug please contact me at akheirali(at)gmail.com

## Technologies used
Python3.7

## BDD
| Input        | Output           | Behavior  |
| ------------- |:-------------:| -----:|
| Search the app      | News-highlight application appears | A list of news articles is generated |
| Click on read more      | Directs user to the news source    | Application generates detailed article |
| Search through the nav bar | Multiple news categories are displayed  | results displayed as per search |


# License
MIT license
