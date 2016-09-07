#!/usr/bin/bash

cd $HOME/source
git pull
lektor build --output-path $HOME/output
rm -f $HOME/output/index.html
rsync -avz $HOME/output/* kushaldas@dgplug.org:./dgplug.org/
