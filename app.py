import streamlit as st
from export import format_for_printing, export_to_file
from export_excel import export_to_excel
import os

def read_file(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file if line.strip()]

def read_parcele(file_path):
    parcele = {}
    with open(file_path, 'r') as file:
        for line in file:
            key, value = line.strip().split(',')
            parcele[key] = int(value)
    return parcele

def calculate_preparat_per_parcela(preparati_values, parcele_values):
    results = {}
    for parcela, parcela_value in parcele_values.items():
        results[parcela] = {}
        for preparat, preparat_value in preparati_values.items():
            results[parcela][preparat] = preparat_value * parcela_value
    return results

def main():
    st.title("Borovnica Prehrana - Unos Preparata i Parcela")

    if 'results' not in st.session_state:
        st.session_state.results = None

    preparati = read_file("preparati.txt")
    parcele = read_parcele("parcele.txt")
    
    st.write("Unesite količine za sljedeće preparate i parcele:")
    
    col1, col2, col3 = st.columns(3)
    
    preparati_values = {}
    parcele_values = {}
    
    with col1:
        st.subheader("Preparati")
        for preparat in preparati:
            preparati_values[preparat] = st.number_input(f"{preparat} (g/sadnica)", min_value=0.0, format="%.2f", key=f"prep_{preparat}")
    
    with col2:
        st.subheader("Parcele")
        for parcela, default_value in parcele.items():
            parcele_values[parcela] = st.number_input(f"{parcela} (broj sadnica)", value=int(default_value), min_value=0, step=1, key=f"parc_{parcela}")
    
    with col3:
        st.subheader("Broj nanošenja")
        num_runs = st.number_input("Broj nanošenja", min_value=1, value=1, step=1)
    
    if st.button("Izračunaj potrebne količine"):
        st.write("Unesene vrijednosti:")
        col1, col2 = st.columns(2)
        with col1:
            st.subheader("Preparati")
            for preparat, value in preparati_values.items():
                st.write(f"{preparat}: {value} g/sadnica")
        with col2:
            st.subheader("Parcele")
            for parcela, value in parcele_values.items():
                st.write(f"{parcela}: {value} sadnica")
        
        st.subheader(f"Izračunate količine preparata po parceli (Broj nanošenja: {num_runs}):")
        results = calculate_preparat_per_parcela(preparati_values, parcele_values)
        for parcela, preparat_values in results.items():
            st.write(f"Parcela {parcela}:")
            for preparat, value in preparat_values.items():
                total_amount = value
                split_amount = total_amount / num_runs
                st.write(f"  {preparat}: {total_amount:.2f} g | {split_amount:.2f} g x {num_runs}")
            st.write("")
        
        st.session_state.results = results

    col1, col2 = st.columns(2)

    with col1:
        if st.button("Izvoz rezultata (TXT)"):
            if st.session_state.results is not None:
                formatted_content = format_for_printing(preparati_values, parcele_values, st.session_state.results, num_runs)
                filename = export_to_file(formatted_content)
                st.success(f"Izvještaj je uspješno izvezen u datoteku: {filename}")
                with open(filename, "r", encoding="utf-8") as file:
                    st.download_button(
                        label="Preuzmi TXT izvještaj",
                        data=file.read(),
                        file_name=filename,
                        mime="text/plain"
                    )
            else:
                st.warning("Molimo prvo izračunajte potrebne količine prije izvoza rezultata.")

    with col2:
        if st.button("Izvoz rezultata (Excel)"):
            if st.session_state.results is not None:
                excel_filename = export_to_excel(preparati_values, parcele_values, st.session_state.results, num_runs)
                st.success(f"Excel izvještaj je uspješno izvezen u datoteku: {excel_filename}")
                with open(excel_filename, "rb") as file:
                    st.download_button(
                        label="Preuzmi Excel izvještaj",
                        data=file.read(),
                        file_name=excel_filename,
                        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                    )
            else:
                st.warning("Molimo prvo izračunajte potrebne količine prije izvoza rezultata.")

if __name__ == "__main__":
    main()