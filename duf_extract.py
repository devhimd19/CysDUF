# CysDUF (Database for DUF proteins to elucidate the functions of Cys PTMs) Python script to extract the data, where the input can be a DUF ID, PFAM ID or a PDB ID and the output gives FPFAM ID, DUF ID, DUF Name, SCOPe Family, SCOPe SuperFamiy, Organisms, Pathway, PDB ID, Chain ID, MENV Computations and Cys Post-Translational Modifications Results.
# Import Libraries required for running of the program.
import csv
import json
import pandas as pd
# Function to read the CSV file.
def find_and_print_rows(file_path, search_id, output_format):
    # Read the CSV file with proper encoding
    data = []
    try:
        with open(file_path, 'r', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                data.append(row)
    except UnicodeDecodeError:
        # Fallback to a different encoding if utf-8 fails
        with open(file_path, 'r', encoding='ISO-8859-1') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                data.append(row)
    
    # Search for all matching rows
    found_rows = []
    for row in data:
        if search_id in row.values():
            found_rows.append(row)
# Save the output in different formats namely CSV, TXT, JSON and Excel.    
    if found_rows:
        if output_format == 'csv':
            with open('output.csv', 'w', newline='') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=found_rows[0].keys())
                writer.writeheader()
                writer.writerows(found_rows)
            print(f"{len(found_rows)} rows written to output.csv")
        
        elif output_format == 'txt':
            with open('output.txt', 'w') as txtfile:
                for row in found_rows:
                    for key, value in row.items():
                        txtfile.write(f"{key}: {value}\n")
                    txtfile.write("\n")  # Separate rows by a newline
            print(f"{len(found_rows)} rows written to output.txt")
        
        elif output_format == 'json':
            with open('output.json', 'w') as jsonfile:
                json.dump(found_rows, jsonfile, indent=4)
            print(f"{len(found_rows)} rows written to output.json")
        
        elif output_format == 'excel':
            df = pd.DataFrame(found_rows)
            df.to_excel('output.xlsx', index=False)
            print(f"{len(found_rows)} rows written to output.xlsx")
        
        else:
            print("Unsupported output format")
    else:
        print("No matching rows found in the database")
# Input Details
# CSV File path
# Input parameters : search_id, output_format
# Example usage
file_path = 'Final_DUF_Data.csv'
search_id = input("Enter the ID to search for: ").strip()
output_format = input("Enter the output format (csv, txt, json, excel): ").strip().lower()
find_and_print_rows(file_path, search_id, output_format)

