import pandas as pd

def save_to_csv(data, filename="lyrics_data.csv"):
    try:
        df = pd.DataFrame(data)
        df.to_csv(filename, index=False)
        print(f"Data saved to {filename}")
    except Exception as e:
        print(f"Error saving to CSV: {e}")
