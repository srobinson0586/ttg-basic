#!/bin/bash

sudo apt update && sudo apt upgrade

# Install vim (assume "y" when prompted if you want to install).
sudo apt install --assume-yes vim

# Install gcc and make (`-y` is the same as `--assume-yes`).
sudo apt install -y build-essential

# Install the man pages.
sudo apt install -y man-db

# Install file.
sudo apt install -y file

# Install unzip.
sudo apt install -y unzip

# Install gcc-multilib.
sudo apt install -y gcc-multilib

# Install python3.
sudo apt install -y python3
sudo apt install -y python3-pip

# Install gdb and gef.
sudo apt install -y gdb
bash -c "$(curl -fsSL https://gef.blah.cat/sh)"

# Install valgrind
sudo apt install -y valgrind
# Ensure 32-bit libc debug lib is installed.
sudo apt install -y libc6-dbg:i386

# Install git.
sudo apt install -y git

# Install nasm.
sudo apt install -y nasm

# Install net-tools.
sudo apt install -y net-tools

# Install wireshark.
sudo apt install -y wireshark
# yes - should superusers be able to capture packets
sudo dpkg-reconfigure wireshark-common
sudo usermod -a -G wireshark $USER
# You'll need to restart to enable non-super user packet capture.

# Install ncat.
sudo apt install -y ncat

# Install ltrace.
sudo apt install -y ltrace

# Install strace.
sudo apt install -y strace

# Install ghidra.
wget https://ghidra-sre.org/ghidra_9.2.1_PUBLIC_20201215.zip \
    && unzip ghidra_9.1.2_PUBLIC_20200212.zip \
    && rm ghidra_9.1.2_PUBLIC_20200212.zip
sudo apt install -y openjdk-11-jdk
sudo apt install -y openjdk-11-jre-headless
sudo mv ghidra_9.1.2_PUBLIC ~/ghidra
sudo ln -s ~/ghidra/ghidraRun /bin/ghidra
# Now typing `ghidra` from the terminal will start ghidra.

# Install checksec.
cd /bin/
sudo wget http://www.trapkit.de/tools/checksec.sh
sudo mv checksec.sh checksec
sudo chmod +x checksec
