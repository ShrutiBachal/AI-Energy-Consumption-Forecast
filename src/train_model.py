from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
import joblib

def train_model(df):
    """Train ML model"""
    
    # Features & target
    X = df.drop(['consumption', 'datetime'], axis=1)
    y = df['consumption']
    
    # Train-test split (IMPORTANT: no shuffle)
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, shuffle=False
    )
    
    # Model
    model = RandomForestRegressor(n_estimators=100)
    model.fit(X_train, y_train)
    
    # Save model
    joblib.dump(model, "models/model.pkl")

    print("Model trained successfully")
    
    return model, X_test, y_test