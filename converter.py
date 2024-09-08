#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Copyright © 2024 Joey Tatú & TattedFaceJoey.ie
All rights reserved.

This script formats MediaWiki code by applying the following transformations:
1. Deletes the output file if it exists and waits for 1 second to ensure it is deleted.
2. Replaces pipes `|` within double curly braces with a placeholder.
3. Inserts new lines before double pipes.
4. Restores the original pipes within double curly braces.
5. Replaces all instances of double pipes with a single pipe.
6. Ensures that `|-` is always preceded by two new lines.
7. Removes any blank lines.
8. Writes the formatted wiki code to the output file output_wiki_code.txt.

Usage:
    python format_wiki_code.py
"""

import re
import os
import time

def format_wiki_code(input_file, output_file):
    # Delete the output file if it exists
    if os.path.exists(output_file):
        os.remove(output_file)
        # Wait for 1 second to ensure the file is deleted
        time.sleep(1)

    # Read the input file
    with open(input_file, 'r') as file:
        wiki_code = file.read()

    # Replace pipes within double curly braces with a placeholder
    line_with_placeholder = re.sub(r'{{[^{}]*}}', lambda m: m.group(0).replace('|', '%%%PIPE%%%'), wiki_code)

    # Function to insert a newline before each double pipe
    def insert_newline_before_double_pipes(match):
        return '\n\n' + match.group(0)

    # Insert new lines before every occurrence of double pipes, including those directly followed by other characters
    formatted_code = re.sub(r'\|\|(?=\S)', insert_newline_before_double_pipes, line_with_placeholder)

    # Restore pipes within double curly braces
    formatted_code = formatted_code.replace('%%%PIPE%%%', '|')

    # Replace all instances of || with | (after ensuring new lines are correctly inserted)
    formatted_code = re.sub(r'\|\|+', '|', formatted_code)

    # Ensure that |- is always preceded by two line breaks
    formatted_code = re.sub(r'(?<!\n\n)\n*\|\-', '\n\n|-', formatted_code)

    # Remove any blank lines
    formatted_code = re.sub(r'\n\s*\n', '\n', formatted_code)

    # Write to the output file
    with open(output_file, 'w') as file:
        file.write(formatted_code)

    print(f"Formatted wiki code has been written to {output_file}")

# File paths
input_file = 'input_wiki_code.txt'  # Input file with wiki code
output_file = 'output_wiki_code.txt'  # Output file for formatted wiki code

format_wiki_code(input_file, output_file)
