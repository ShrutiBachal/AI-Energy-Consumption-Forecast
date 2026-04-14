import pandas as pd

def load_data(file_path):
    """Load dataset"""
    df = pd.read_csv(file_path)
    print("Dataset loaded successfully\n",df.head)
    return df

def preprocess_data(df):
    """Clean and prepare data"""

    df.rename(columns={
    'Datetime': 'datetime',
    'AEP_MW': 'consumption'
    }, inplace=True)
    
    # Convert datetime column
    df['datetime'] = pd.to_datetime(df['datetime'])
    
    # Sort data
    df = df.sort_values(by='datetime')
    
    # Drop missing values
    if(df.isnull().values.any()):
        print("Total null values : ",df.isnull().sum())
        df = df.dropna()
    else:
        print("No null values found")
    return df

def save_processed_data(df, output_path):
    df.to_csv(output_path, index=False)
    print(f"Processed data saved at {output_path}")
    return df