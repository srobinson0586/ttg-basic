#!/bin/bash

#trainee_setup.sh is to be run as the first action after cloning your student repository. 


if ! command -v git &> /dev/null
then
    echo "git could not be found"
    echo "Attempting to install git:"
    sudo apt install git -y
fi

if ! command -v gh &> /dev/null
then
    echo "GitHub CLI could not be found"
    echo "Attempting to install gh:"
    ## Install GitHub CLI - Debian/Ubuntu
     type -p curl >/dev/null || (sudo apt update && sudo apt install curl -y)
     curl -fsSL https://cli.github.com/packages/githubcli-archive-keyring.gpg | sudo dd of=/usr/share/keyrings/githubcli-archive-keyring.gpg \
     && sudo chmod go+r /usr/share/keyrings/githubcli-archive-keyring.gpg \
     && echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/githubcli-archive-keyring.gpg] https://cli.github.com/packages stable main" | sudo tee /etc/apt/sources.list.d/github-cli.list > /dev/null \
     && sudo apt update \
     && sudo apt install gh -y
fi
gh auth login

git remote add upstream https://github.com/Developer-Pipeline/ttg-basic.git

git pull upstream main --allow-unrelated-histories --no-edit --rebase -f

git push origin HEAD:main --force-with-lease
git checkout main
git config pull.rebase true
rm -fr ".git/rebase-merge"
git pull
