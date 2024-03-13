#!/bin/bash

# check to make sure user has entered exactly 2 arguments
if  [ $# -ne 2 ]
then
    echo "Usage: backup_script.sh <source_dir> <target_dir>"
    echo "Please try again."
    exit 1
fi

# check to see if rsync is installed
if ! command -v rsync > /dev/null 2>&1  # send all output to /dev/null
then
    echo "This script requires rsync to be installed."
    echo "Pleas euse your distro's package manager to install it"
    exit 2
fi

# Capture the current date and store it to YYYY-MM-DD format
current_date=$(date +%Y-%m-%d)

# -a archive mode, -v verbose, -b -backup-dir:
# $2/$current_date creates a subdir with the actual date so files don't get overwritten
# --delete makes sure that the target directory is an exact clone of source
# --dry-run a test run which simulates the real thing
# remove the --dry-run option is everything is OK
rsync_options="-avb --backup-dir $2/$current_date --delete --dry-run"

# which returns the fully verified command
# adding options
# source and target+subfolder
# the verbose option result will be sent to a log file
$(which rsync) $rsync_options $1 $2/current >> backup_$current_date.log

