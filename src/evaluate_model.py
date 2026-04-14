from sklearn.metrics import mean_squared_error, r2_score
import numpy as np

def evaluate_model(y_test, y_pred):
    """Evaluate model performance"""

    print("Evaluating model performance")
    
    mse = mean_squared_error(y_test, y_pred)
    rmse = np.sqrt(mse)
    r2 = r2_score(y_test, y_pred)
    
    print(f"RMSE: {rmse}")
    print(f"R2 Score: {r2}")
    
    return rmse, r2