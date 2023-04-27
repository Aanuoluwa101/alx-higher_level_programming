#!/bin/bash
# a script that makes a request to 0.0.0.0:5000/catch_me
curl -isX PUT -d "You got me!" -d "user_id=98" -d "School" 0.0.0.0:5000/catch_me
