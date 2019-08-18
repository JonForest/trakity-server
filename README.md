# Trakity Server
This is the Django API server, able to support multiple types of client (e.g. ember, command-line etc)

## Build Locally

## How to run tests

## Deploy to server

# TODO items
* uwsgi set-up? Maybe a docker container with it all in that I can then deploy to docker? That seems best
* Think about the command line interface structure and dates. Namely, do we want date objects and time separately?
  Or do we want some kind of timezone aware datetime? Or two fields? date for when only date selected, datetime for when time also selected?
  Gut feel is that timezone is important once the app goes beyond three people in new zealand.
* Double check what we want to do with tasks that have a targetDate in the past. Do we want to roll them forward to tomorrow again?
* Get tasks with hard coded user working
* Why does 127.0.0.1:8000/tasks work but localhost:8000/tasks does not?
* How do we turn the API web interface off?

## Done
* Read in more detail about JWT
  * Why access and refresh tokens separately
  * Can be used to extract user object out of the application so it can work across many applications
* Make decision on JWT or Expiring Tokens
* Test the blacklisting of refresh tokens works automatically
* Import JWT https://github.com/davesque/django-rest-framework-simplejwt
  * Request token is read-once
* Set it up such auth/refresh and tasks part of the app are independent. (i.e. separate Django apps)
* Fix failing tests as 'RefreshToken' doesn't appear t be using my custom functions
* Include userid (guid), role (basic_tasks), email  
* Implement permissions to ensure that a user can only get their own tasks (CURRENTLY FAILING TESTS)
  * Check non-db backed user object is on the request
    
