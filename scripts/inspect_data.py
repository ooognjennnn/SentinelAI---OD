import pandas as pd

# Putanja do odabranog fajla (Monday-WorkingHours.csv)
file_path = "data/raw/unsw-nb15/UNSW-NB15 dataset/CSV Files/Training and Testing Sets/UNSW_NB15_training-set.csv"

# Učitavanje podataka iz fajla
print("Učitavanje podataka...")
data = pd.read_csv(file_path)

# Štampamo osnovne informacije
print("\nKolone (Columns):")
print(data.columns)  # Lista kolona

print("\nPrvih 5 redova (First 5 rows):")
print(data.head())   # Prvih 5 redova

# Dimenzije (rows x columns)
print(f"\nDimenzije skupa podataka: {data.shape}")