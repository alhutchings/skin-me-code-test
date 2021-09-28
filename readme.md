
## Spec

Please clone this repository, and create a PR to demonstrate the following using the provided flask/sqlalchemy application:

Create a set of endpoints to allow a browser to present a survey to a user and collect their answers, for the purpose of collecting patient medical information.  

Try and implement some of the following:
* Multiple steps/pages, each with multiple questions.
* Ability to support multiple question types, e.g. Single choice, Multi choice, Free text, Address.
* Ability to have questions be asked dependent on previous answer, e.g. If we ask if they are taking any medication, we might want to then ask what medications they are taking.
* State can be stored, so that user can continue at a later date or on another device
* Support A/B testing of new questions that we might want to introduce

Of course this is a large, and wide ranging scope - so I would bias towards sharing something early with explanation about decisions you took and what you would do with more time, ultimately this is about building confidence in ability to carry out the role vs actually delivering a complete solution.  

## Prerequisites
* python 3
* bash
* make
* optionally - docker


## Development

Use either of the following local or docker instructions

### Local
#### Setup
* `python3 -m venv .venv`
* `source .venv/bin/activate`
* `pip install -r requirements.txt`
* `make local-reset-db`
#### Run
* `make local-start`
#### Test
* `make local-test`

### Docker
#### Setup
* `make docker-init`
#### Run
* `make docker-start`
#### Test
* `make docker-test`


This is to help you get up and running quickly.
Feel free to restructure the app code as you see fit.
Feel free to add any packages/dependencies as you see fit.
What would you do further to this spec?