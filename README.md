# Trakity Server
This is the Django API server, able to support multiple types of client (e.g. ember, command-line etc)

## Build Locally

## How to run tests

## Deploy to server

# TODO items
* Test the blacklisting of refresh tokens works automatically
* Import JWT https://github.com/davesque/django-rest-framework-simplejwt
  * Request token is read-once
  * Include userid (guid), role (basic_tasks), email
  * See if the non-db backed user object works here
  
* Set it up such auth/refresh and tasks part of the app are independent. (i.e. separate Django apps)
* Add lots of unit tests around login in, access expiration, and refreshing the token
* Tests around a user with a valid token fetching their tasks

* Set up so user can only fetch their own tasks
* Copy over pieces of trakity code from the original
* Get tasks with hard coded user working
* Why does 127.0.0.1:8000/tasks work but localhost:8000/tasks does not?
* How do we turn the API web interface off?

## Done
* Read in more detail about JWT
  * Why access and refresh tokens separately
  * Can be used to extract user object out of the application so it can work across many applications
* Make decision on JWT or Expiring Tokens

