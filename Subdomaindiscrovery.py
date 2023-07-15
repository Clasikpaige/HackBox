#!/bin/bash

# Prompt the user for the target
read -p "Enter the target domain: " target_domain

# Set the output file name
output_file="subdomains.txt"

# Run subfinder and save the output to the file
subfinder -d $target_domain | tee $output_file
