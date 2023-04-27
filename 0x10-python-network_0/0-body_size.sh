#!/bin/bash
# a script that sends a request to a given URL and prints the size of the body of the response
curl -sw "%{size_download}\n" -o /dev/null $1
