import pandas as pd
import os

# Putanje fajlova
input_path = "data/raw/GeneratedLabelledFlows/TrafficLabelling/Monday-WorkingHours.pcap_ISCX.csv"
output_path = "data/processed/Monday-WorkingHours-cleaned.csv"

# Učitavanje CSV fajla
print("Učitavanje CSV fajla...")
data = pd.read_csv(input_path)

# Uklanjanje razmaka iz naziva kolona
data.columns = data.columns.str.strip()

# Kolone za uklanjanje
columns_to_drop = ['Source IP', 'Destination IP', 'Flow ID']
data = data.drop(columns=columns_to_drop, errors='ignore')  # Nepotrebno uklanjamo
print(f"Kolone nakon uklanjanja: {data.columns}")

# Provera nedostajućih vrednosti
missing_values = data.isnull().sum()
print("\nBroj nedostajućih vrednosti po kolonama:")
print(missing_values[missing_values > 0])  # Prikazuje samo kolone sa NaN vrednostima

# Popunjavanje nedostajućih vrednosti sa 0
data = data.fillna(0)
print("\nNedostajuće vrednosti su popunjene sa 0.")

# Prikaz prvih nekoliko redova nakon obrade
print("\nPreostalih nekoliko redova (provera nakon obrade):")
print(data.head())

# Čuvanje prerađenog fajla
os.makedirs("data/processed", exist_ok=True)
data.to_csv(output_path, index=False)
print(f"Prerađeni i očišćeni podaci sačuvani u {output_path}.")