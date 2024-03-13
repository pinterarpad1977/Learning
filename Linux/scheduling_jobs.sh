#!/bin/bash

# 1. scheduling with the command at
# install the at command if it is not installed

logfile=job_results.log
/usr/bin/echo "The script ran at: $(/usr/bin/date)" > $logfile

# at 19:19 -f ./scheduling_jobs.sh 
# at usage:
	# -f run a file
	# atq shows the jobs on queue
	# atrm removes the job from the queue
	# at 18:00 300324 -f ./sript.sh (use the full path)

# 2. scheduling with the command cron
	# in scripts use fully qualified commands
	# the reason is because cron might run in a different shell environment
	# also to avoid the case when a user creates a same name script as a command and puts it somewhere in the path
	# to add a cronjob: crontab -e and see the instructions


