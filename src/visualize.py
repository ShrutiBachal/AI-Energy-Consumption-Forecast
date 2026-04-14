import matplotlib.pyplot as plt

def plot_results(y_test, y_pred, last_n=500):
    """Plot actual vs predicted values with a focus on recent samples"""
    
    plt.figure(figsize=(12, 6))
    
    # Plotting only the last_n samples for better interpretability
    plt.plot(y_test.values[-last_n:], label='Actual', alpha=0.7, linewidth=2)
    plt.plot(y_pred[-last_n:], label='Predicted', linestyle='--', linewidth=2)
    
    plt.title(f"Energy Consumption Forecast (Last {last_n} Hours)")
    plt.xlabel("Time (Hourly)")
    plt.ylabel("Consumption (MW)")
    
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.legend()
    plt.savefig("images/actual_vs_predicted.png")
    plt.show()

def plot_forecast(future_predictions):
    """Plot future predicted values"""
    
    plt.figure(figsize=(10, 5))
    plt.plot(future_predictions, marker='o', color='green', label='Future Forecast')
    
    plt.title("Next 24 Hours Energy Consumption Forecast")
    plt.xlabel("Steps (Hours)")
    plt.ylabel("Consumption (MW)")
    
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.legend()
    plt.savefig("images/future_forecast.png")
    plt.show()