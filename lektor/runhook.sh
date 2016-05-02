#!/usr/bin/bash

cd /source
git pull
lektor build --output-path /output
rm -f /output/index.html
rsync -avz /output/* kushaldas@dgplug.org:./dgplug.org/
