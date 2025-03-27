import os
import pandas as pd

def preprocess_csv(input_path, output_path):
    print(f"Processing {input_path}...")
    data = pd.read_csv(input_path)
    data.columns = data.columns.str.strip()  # Ukloniti razmake iz naziva kolona
    # Uklanjanje nepotrebnih kolona
    columns_to_drop = ['Source IP', 'Destination IP', 'Flow ID']
    data = data.drop(columns=columns_to_drop, errors='ignore')
    # Popunjavanje nedostajućih vrednosti
    data = data.fillna(0)
    # Čuvanje prerađenog fajla
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    data.to_csv(output_path, index=False)
    print(f"Processed file saved to {output_path}")

input_folder = "data/raw/cic-ids-2017/MachineLearningCVE"
output_folder = "data/processed"

# Iterativno procesuiranje CSV fajlova u folderu
for filename in os.listdir(input_folder):
    if filename.endswith(".csv"):
        input_file = os.path.join(input_folder, filename)
        output_file = os.path.join(output_folder, f"processed_{filename}")
        preprocess_csv(input_file, output_file)