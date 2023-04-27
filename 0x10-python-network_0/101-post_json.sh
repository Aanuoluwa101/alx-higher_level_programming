#!/bin/bash
# a script that sends a JSON POST request to a URL and displays the body of the response
curl -sX POST -H "Content-Type: application/json" --data-binary @$2 $1
