def forecast_future(model, X_test, steps=24):  
    """Predicts next n values (24 hours)"""

    print("Forecasting future values")
    
    future_predictions = model.predict(X_test.tail(steps))
    
    return future_predictions