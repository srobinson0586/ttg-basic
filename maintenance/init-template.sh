#!/bin/bash

if [ -z $2 ]
then
    echo Usage: $0 "<traino ip> <git remote ssh url>"
    exit 1
fi

port=4567
ip_addr=$1
template_dir=basic-jqr
tar_filename=$template_dir.tar.gz
git_remote_url=$2

# Receive the tar.gz from the server.
# We don't need an idle timeout because the Python socket will close once
# it's sent the whole file. Then ncat will finish (using --recv-only).
echo "[+]" Receiving $tar_filename from $ip_addr:$port . . .
ncat -v --recv-only  -w 1s $ip_addr $port > $tar_filename
if [ $? = 0 ]
then
   echo -e "[+] Done\n"
else
    echo $tar_filename transfer failed. Exiting.
    exit 1
fi

# Extract the tar.gz file.
echo "[+]" Extracting $tar_filename . . .
tar -xvf $tar_filename
if [ $? -ne 0 ]
then
    echo "[-]" $tar_filename appears corrupted. Exiting.
    rm $tar_filename
    exit 1
fi
echo -e "[+] Done\n"

# Initialize git repo.
echo [+] Moving into $template_dir and initializing local git repo . . .
cd $template_dir
git init --initial-branch=main
echo -e "[+] Done\n"

# Set the remote repo URL.
echo [+] Setting the git remote to $git_remote_url . . .
git remote add origin $git_remote_url
echo -e "[+] Done\n"

# Add all files to the local repo.
echo [+] Adding all files to the local repo . . .
git add .
echo -e "[+] Done\n"

# Make the initial commit for the local repo.
echo [+] Making the initial commit for the local repo . . .
git commit -m "Initial commit"
echo -e "[+] Done\n"

# Push to the remote.
echo [+] Pushing to the remote . . .
git push --set-upstream origin main
echo -e "[+] Done"
