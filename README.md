# Mediquick
by Ryan, Greta, Elwin

Advancing health care into the future generation

# Description
The B word. We've all said it.

Busy.

But even in this modern age of always being on the go, you should never be too busy to look after your own health.

At MediQuick, we can provide you with easy access to expert medical advice in just a matter of minutes.

No more queuing on the phone to book a GP appointment. Just register online and speak to one of our expert resident doctors immediately!



## Requirements, installation & usage
For our app to run on your local machine you will have to follow these steps: 
Requirements
First of all, you will need to ensure the following are installed on your local machine:

Pyenv
Pipenv
Python
(below are some links to download python)
https://www.python.org/downloads/
https://realpython.com/intro-to-pyenv/

### Installation
Fork and clone this repo, then navigate to the root directory of this repo in your local machine's shell/terminal e.g. Git Bash.

Then run the following commands:

pipenv shell
pipenv install
Usage
If all is successful, you should be able to perform the following tasks by running the specified commands:

Run dev environment: pipenv run dev (view on http://localhost:8000)
Run the full test suite: pipenv run test
Initiate a coverage report: pipenv run initcov
View the coverage report: pipenv run viewcov




## Technologies

For this project, we used a lot of new technologies that we were exposed to during our final LAP at futureproof. It was decided as a group to use these technologies as they provided us with the necessary requirements to fulfill the project MVP, whilst also exposing us to new ways of working on an application, therefore advancing our learning!

Here is a list of the main technologies used along with a short description as to why.

Dependencies:
Api: 

Python - used for the backend of the app, as this was a great opportunity for us to use a different language to what we were used to and practise the language!

Django web development framework - this decision was made due to Django's extensive in-built features, which it easier to build the app rather than work from scratch using a technology such as python flask.

Django channels & mail - communication is a key cornerstone of our app, it is designed to be easy and flexible for patients and doctors to connect, therefore the in-built django libraries for channels (web sockets) and mail (two factor authentication/support) was chosen.

SQLlite3 - inbuilt django database used for the ease of integration into our app and the need for relational data 

Client: 

Bootstrap4 - used to make slick and nice looking designs on the client




## Planning and development of app
DevOps process

The initial idea creation phase was as follows: 

Figma design - Once the idea was clearly defined, we created figma designs to visualise the app before creating it

Database design - This was then proceeded by designing the database so we could understand the flow of data through our ap

User Story - The next main step within planning was to fully flesh out the user journey so we could begin development

GitHub actions board - During development we worked on separate feature branches and were highly communicative within the team about which tasks needed to be completed. Each member was assigned tasks on the project board and consequently worked on these tasks. 

Bugs

A bug in our app is the error handling elements that weren't fully implemented although the html templates where designed appropriately. However, there were issues integrating into our app and due to time limitations this was not seen as a priority at this moment. 

 
## Wins & Challenges

### Wins
- Managed to create a product that we are very proud of in a short time scale with a small team
- Created a website design that looks very similar to the initial figma designs that we set out to achieve
- Implemented a lot of GDPR considerations for our app as we realise due to the nature of the data we have, security is of the utmost priority
- Was able to be extremely flexible and adaptable as a team, in terms of learning new technologies (like django encryption and django channels) as well as adapting our requirements to the timeframe
- In general, the git flow within the team was highly commendable, there was not any huge conflicts and we were highly communicative with each other in terms of which feature branches we were working on at all times.
- Achieved 80%+ test coverage within the app!
- created a great patient dashboard and eye-appealing user interface that can only be improved upon as time goes on!

### Challenges
- Deployment was a key issue for our app during this process. Due to inexperience with deploying django apps, we had a few issues with the configurations but managed to deploy most of the functionality. 
- The usage of pipenv virtual environments proved to be a challenge as some teammates had problems importing the channels module
- Originally we had planned to have more features in the app, e.g. scheduling feature and doctor view. However, due to time limitations we had to consider refining our MVP. 
- Team management and work flow proved to be a big challenge, due to the size of the team being fairly small for a larger project, the productivity in the early stages was slower. However, this exercise proves the flexibility and adaptability within the team to be able to find solutions to different scenarios!



## Significant Code
(Place image of code snippets here)
{"A?":"B","a":5,"d":"B","h":"www.canva.com","c":"DAEe8NAZUR4","i":"Us-WzufjzcWzLvncnqZyEA","b":1621578007312,"A":[{"A?":"I","A":352.9843634473119,"B":682.4428091684845,"D":1223.0138271617052,"C":470.33269831304614,"a":{"B":{"A":{"A":"MAEfBh0qRUw","B":1},"B":{"A":-91.26499506115684,"B":-86.70174530809902,"D":1432.8947894328885,"C":652.8626884353599}}}}],"B":1920,"C":1080}

{"A?":"B","a":5,"d":"B","h":"www.canva.com","c":"DAEe8NAZUR4","i":"Us-WzufjzcWzLvncnqZyEA","b":1621578007312,"A":[{"A?":"I","A":340.4606819194761,"B":779.463698691221,"D":1032.536301308779,"C":435.1402984086997,"a":{"B":{"A":{"A":"MAEfBVSl4SE","B":1},"B":{"A":-2.842170943040401e-14,"B":-1.1368683772161603e-13,"D":1032.5363013087792,"C":435.1402984086998}}}}],"B":1920,"C":1080}



## Future Features

Machine Learning Model - a plan to implement a predictive ML model, where patients would be able to enter their symptoms and get a prediction for their disease at which point they would be recommended a more specialised doctor was made. 

Video Calls - implement video call technology for patients who prefer this type of communication

Scheduling system - implement an appointment scheduling system for the patients to organise with the doctors in a slick and easy way

## GDPR Considerations

Due to the nature of the app, in terms of the handling of sensitive health data, GDPR policies must be followed. Some of the key factors to consider and how we dealt with this is placed below. 

Transparency - we have a policy page, which clearly states the use of data for patients to read as well as a support page to contact us

Data minimisation - mediquick only asks for basic information, such as name and email address to function properly. However, this may be expanded upon in future versions

Storage - all data that is stored is encrypted using django cryptography

Slide Deck

https://www.canva.com/design/DAEe8NAZUR4/Us-WzufjzcWzLvncnqZyEA/edit
