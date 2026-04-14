from src.data_preprocessing import load_data, preprocess_data, save_processed_data
from src.feature_engineering import create_features
from src.train_model import train_model
from src.evaluate_model import evaluate_model
from src.forecast import forecast_future

def main():
    
    # Step 1: Load data
    df = load_data("data/raw/energy_data.csv")
    
    # Step 2: Preprocess
    df = preprocess_data(df)
    save_processed_data(df, "data/processed/processed_energy_data.csv")

    # Step 3: Feature Engineering
    df = create_features(df)
    
    # Step 4: Train model
    model, X_test, y_test = train_model(df)

    # Step 5: Predictions
    y_pred = model.predict(X_test)
    pred_df = pd.DataFrame({
        "Actual": y_test.values,
        "Predicted": y_pred
    })
    pred_df.to_csv("outputs/predictions/predictions.csv", index=False)

    # Step 6: Evaluate model
    evaluate_model(y_test, y_pred)

    # Step 7: Forecast future values
    future_predictions = forecast_future(model, X_test)
    print(future_predictions)

if __name__ == "__main__":
    main()