def create_features(df):
    """Create time-based and lag features"""

    # Time features
    df['hour'] = df['datetime'].dt.hour
    df['day'] = df['datetime'].dt.day
    df['month'] = df['datetime'].dt.month
    df['day_of_week'] = df['datetime'].dt.dayofweek
    
    # Lag feature (previous hour consumption)
    df['lag_1'] = df['consumption'].shift(1)
    
    # Drop NaN values after lag
    df = df.dropna()

    print("Features created successfully\n",df.head())
    
    return df