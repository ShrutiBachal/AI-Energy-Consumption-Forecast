from src.data_preprocessing import load_data, preprocess_data, save_processed_data

def main():
    
    # Step 1: Load data
    df = load_data("data/raw/energy_data.csv")
    
    # Step 2: Preprocess
    df = preprocess_data(df)
    save_processed_data(df, "data/processed/processed_energy_data.csv")

if __name__ == "__main__":
    main()