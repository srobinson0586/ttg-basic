#!/bin/bash
#
# trainee_update.sh 
# This script will make a backup of the current branch, then switch to the "main" branch and pull the upstream.

DATE=$(date +%s)
echo "##Backing up current main as branch: backup_$(date -d"@$DATE" '+%Y-%m-%d-%H-%M')"
git branch "backup_$(date -d"@$DATE" '+%Y-%m-%d-%H-%M')";

echo "##Switching to main branch"
git checkout main

echo "##Pulling update from upstream main:"
git pull upstream main --rebase

echo "##Syncing changes:"
git pull --rebase

echo "##Pushing updated repo to remote:"
git push
