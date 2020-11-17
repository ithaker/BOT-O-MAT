# BOT-O-MAT for Alexa

## Table of contents
* [General Info](#general-info)
* [Issues](#issues)
* [Technologies](#technologies)
* [Installation](#installation)
* [Deployment](#deployment)
* [Project Details](#project-details)

## General info
This project was coded in Python3 using Linux on a Raspberry Pi 4. The program aims to present the basic functionality of the Bot-o-Mat using Amazon Alexa. Ngrok allows the localhost server to be tunneled out and used as an endpoint by Amazon Alexa Skills. 

## Issues
The code runs within the localhost server and tunnels successfully to the alexa skills build; however, once called, ngrok displays a "500 internal server eroror."

To-Do:
- Add responsive tasks for the robots to do
- Read out updated task list as tasks are completed

## Technologies
Project is created with:
* Flask
* Flask-ask
* Ngrok

## Setup w/ Flask-Ask
### Pre-requisites
- Python or Python3
- Register for an [AWS Account](https://aws.amazon.com/)
- Register for an [Amazon Developer Account](https://developer.amazon.com/)

## Installation
1. Clone the repository
`$ git clone https://github.com/ithaker/BOT-O-MAT/`

2. Install Flask
`pip install flask`

3. Install Flask-Ask
`pip install flask-ask`

4. Install [Ngrok](https://ngrok.com/) and follow the installation guide, extracting the zip file into the project folder

## Deployment
1. Within the alexa developer console, Create a Skill

2. Title the skill as you would like

3. Set up a Skill Invocation Name (the phrase that will start the project)

4. Adding Intents: 
The project is dependent on specific intents in order to operate. Thankfully, the alexa developer console has premade intents. Click "Add Intent" and activate the following:
    - AMAZON.YesIntent
    - AMAZON.NoIntent
    - Custom "NameIntent"
    - Within the Slot Type select "AMAZON.US_FIRST_NAME"
  
5. Tunneling
    - run the program
    - run ngrok `./ngrok http 5000`
    - Under "Endpoint," paste the https Forwarding URL
    - Add "/" to the end of the url depending on the extension specified in line 6
    
6. "Build" the skill and put the skill testing in "Development" mode

7. Test the application within the developer console or on your Amazon Echo

## Project Details

### Robot
Robot completes tasks and removes them from the list when they are done (i.e. enough time has passed since starting the task).

### Tasks
Tasks have a description and an estimated time to complete.

```
[
  {
    description: 'do the dishes',
    eta: 1000,
  },{
    description: 'sweep the house',
    eta: 3000,
  },{
    description: 'do the laundry',
    eta: 10000,
  },{
    description: 'take out the recycling',
    eta: 4000,
  },{
    description: 'make a sammich',
    eta: 7000,
  },{
    description: 'mow the lawn',
    eta: 20000,
  },{
    description: 'rake the leaves',
    eta: 18000,
  },{
    description: 'give the dog a bath',
    eta: 14500,
  },{
    description: 'bake some cookies',
    eta: 8000,
  },{
    description: 'wash the car',
    eta: 20000,
  },
]
```

### Types
```
{ 
  UNIPEDAL: 'Unipedal',
  BIPEDAL: 'Bipedal',
  QUADRUPEDAL: 'Quadrupedal',
  ARACHNID: 'Arachnid',
  RADIAL: 'Radial',
  AERONAUTICAL: 'Aeronautical'
}
```


## Authors
- Scott Hoffman <https://github.com/scottshane>
- Olivia Osby <https://github.com/oosby>
- Ishan Thaker <https://github.com/ithaker>
