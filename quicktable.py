#!/usr/bin/python3
import argparse

def format_table(table_str):
    # Split the table string into rows
    rows = table_str.strip().split('\n')
    
    # Split the first row into column headers
    headers = [header.strip() for header in rows[0].split('\t')]
    
    # Create the table header
    header = '| ' + ' | '.join(headers) + ' |'
    
    # Create the table separator
    separator = '| ' + ' | '.join(['---' for _ in headers]) + ' |'
    
    # Create the table body
    body = []
    for row in rows[1:]:
        cells = [cell.strip() for cell in row.split('\t')]
        body.append('| ' + ' | '.join(cells) + ' |')
    
    # Combine the header, separator, and body into the final table
    table = [header, separator] + body
    
    # Join the table into a single string and return it
    return '\n'.join(table)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Format a tab-delimited table into a Markdown table.')
    parser.add_argument('input', help='File path or text input to format')
    args = parser.parse_args()
    
    # Check if input is a file path or text
    try:
        with open(args.input, 'r') as f:
            table_str = f.read()
    except FileNotFoundError:
        table_str = args.input
    
    # Format the table and print it
    formatted_table = format_table(table_str)
    print(formatted_table)


