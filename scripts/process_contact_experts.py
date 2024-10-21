import csv

# Define the logic for the "Relation" column
def generate_relation(accepte_value):
    accepte_value = accepte_value.strip().lower()
    if accepte_value == '':
        return 'Inexistante'
    elif accepte_value == 'oui':
        return 'Excellente'
    elif accepte_value == 'non':
        return 'Moyenne'
    else:
        return 'Bonne'

# Define the logic for mapping "Aligné" to "Alignement"
def map_aligne_to_alignement(aligne_value):
    aligne_value = aligne_value.strip().lower()
    
    if "oui" in aligne_value:
        return "Total"
    elif "plus ou moins" in aligne_value:
        return "Partiel"
    elif "peut etre" in aligne_value:
        return "Moyen"
    elif "non" in aligne_value:
        return "Opposé"
    elif "pas vraiment" in aligne_value or "not really" in aligne_value:
        return "Faible"
    elif "unknown" in aligne_value or "inconnu" in aligne_value or "unkown" in aligne_value:
        return "Inconnu"
    else:
        return "Inconnu"  # Default to "Inconnu" if no match

# Function to transform the CSV
def transform_csv(input_file, output_file):
    with open(input_file, mode='r', encoding='utf-8-sig') as infile, open(output_file, mode='w', newline='', encoding='utf-8') as outfile:
        reader = csv.DictReader(infile)
        fieldnames = ['full_name', 'email', 'notes', 'linkedin', 'relation', 'contact_types', 'alignement']
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)

        # Write the header to the output CSV
        writer.writeheader()

        # Process each row from the input CSV
        for row in reader:
            full_name = row['Nom'].strip()
            email = row['Email'].strip()
            notes = row['Notes'].strip()
            linkedin = row['Linkedin'].strip()
            accepte = row['Accepte'].strip()
            aligne = row['Aligné'].strip()

            # Apply the logic to generate the "Relation" field
            relation = generate_relation(accepte)

            # Apply the logic to map "Aligné" to "Alignement"
            alignement = map_aligne_to_alignement(aligne)

            # Constant value for "Contact Types"
            contact_types = 'Expert;'

            # Create a new row with the transformed data
            transformed_row = {
                'full_name': full_name,
                'email': email,
                'notes': notes,
                'linkedin': linkedin,
                'relation': relation,
                'contact_types': contact_types,
                'alignement': alignement
            }

            # Write the transformed row to the output CSV
            writer.writerow(transformed_row)

# Example usage:
input_csv_file = 'Contacts - Experts.csv'  # Replace with your actual input file path
output_csv_file = 'contacts_experts.csv'  # Replace with your actual output file path
transform_csv(input_csv_file, output_csv_file)
