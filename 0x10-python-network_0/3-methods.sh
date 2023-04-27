#!/bin/bash
# a script that takes in a URL and displays all HTTP methods the server will accept.
curl -isX OPTIONS $1 | awk -F ': ' '/^Allow/{print $2}'
