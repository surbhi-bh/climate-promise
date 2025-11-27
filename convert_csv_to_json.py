#!/usr/bin/env python3
"""
Convert CSV files to JSON format for web visualization
"""
import csv
import json

def convert_csv_to_json(csv_file, json_file):
    """Convert CSV file to JSON format"""
    data = []

    with open(csv_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            data.append(row)

    with open(json_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print(f"Successfully converted {len(data)} records from {csv_file} to {json_file}")

def convert_climate_promise():
    """Convert climate promise database"""
    convert_csv_to_json('climate-promise-db.csv', 'climate-promise-db.json')

def convert_emissions():
    """Convert emissions database"""
    convert_csv_to_json('merged_emissions.csv', 'merged_emissions.json')

if __name__ == '__main__':
    # Convert both files
    convert_climate_promise()
    convert_emissions()
