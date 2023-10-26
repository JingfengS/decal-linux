#!/usr/bin/bash

# Find the mac address of the eth0 network interface

ip addr show eth0 | grep link/ether | cut -c 16-
