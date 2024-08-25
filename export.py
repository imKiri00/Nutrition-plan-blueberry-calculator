"""
This module handles the export and printing functionality for the Borovnica Prehrana application.
It formats the calculated data for printing.
"""

def format_for_printing(preparati_values, parcele_values, results, num_runs):
    """
    Format the calculated data for printing.
    Returns a formatted string containing all the data.
    """
    output = "Borovnica Prehrana - Izvještaj\n\n"

    output += "Unesene vrijednosti:\n"
    output += "Preparati:\n"
    for preparat, value in preparati_values.items():
        output += f"{preparat}: {value:.2f} g/sadnica\n"
    
    output += "\nParcele:\n"
    for parcela, value in parcele_values.items():
        output += f"{parcela}: {value} sadnica\n"

    output += f"\nIzračunate količine preparata po parceli (Broj nanošenja: {num_runs}):\n"
    for parcela, preparat_values in results.items():
        output += f"Parcela {parcela}:\n"
        for preparat, value in preparat_values.items():
            total_amount = value
            split_amount = total_amount / num_runs
            output += f"  {preparat}: {total_amount:.2f} g | {split_amount:.2f} g x {num_runs}\n"
        output += "\n"
    
    return output

def export_to_file(content, filename="izvjestaj.txt"):
    """
    Write the formatted content to a file.
    """
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    return filename