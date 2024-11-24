import pandas as pd

def load_csv(file_path):
    """
    Loads a CSV file into a pandas DataFrame.
    
    Args:
        file_path (str): Path to the CSV file.
        
    Returns:
        pd.DataFrame: Loaded DataFrame.
    """
    try:
        data = pd.read_csv(file_path)
        print("\nData loaded successfully!\n")
        print(data.head())
        return data
    except Exception as e:
        print(f"Error loading file: {e}")
        return None

def handle_missing_values(data):
    """
    Handles missing values in the DataFrame.
    
    Args:
        data (pd.DataFrame): Input DataFrame.
        
    Returns:
        pd.DataFrame: Cleaned DataFrame.
    """
    print("\nHandling missing values...")
    print("Options:")
    print("1. Drop rows with missing values")
    print("2. Fill missing values with a constant")
    print("3. Fill missing values with column mean/median/mode")
    choice = input("Choose an option (1/2/3): ").strip()
    
    if choice == "1":
        data = data.dropna()
        print("\nRows with missing values dropped.")
    elif choice == "2":
        fill_value = input("Enter a value to fill missing entries: ")
        data = data.fillna(fill_value)
        print("\nMissing values filled with constant value.")
    elif choice == "3":
        print("\nOptions:")
        print("a. Fill with mean")
        print("b. Fill with median")
        print("c. Fill with mode")
        stat_choice = input("Choose an option (a/b/c): ").strip()
        if stat_choice == "a":
            data = data.fillna(data.mean(numeric_only=True))
            print("\nMissing values filled with mean.")
        elif stat_choice == "b":
            data = data.fillna(data.median(numeric_only=True))
            print("\nMissing values filled with median.")
        elif stat_choice == "c":
            for column in data.columns:
                mode = data[column].mode()
                if not mode.empty:
                    data[column].fillna(mode[0], inplace=True)
            print("\nMissing values filled with mode.")
    else:
        print("\nInvalid choice. No changes made.")
    return data

def remove_duplicates(data):
    """
    Removes duplicate rows from the DataFrame.
    
    Args:
        data (pd.DataFrame): Input DataFrame.
        
    Returns:
        pd.DataFrame: Cleaned DataFrame.
    """
    before = len(data)
    data = data.drop_duplicates()
    after = len(data)
    print(f"\nRemoved {before - after} duplicate rows.")
    return data

def save_csv(data, output_path):
    """
    Saves the cleaned DataFrame to a new CSV file.
    
    Args:
        data (pd.DataFrame): Cleaned DataFrame.
        output_path (str): Path to save the CSV file.
    """
    try:
        data.to_csv(output_path, index=False)
        print(f"\nCleaned data saved to {output_path}")
    except Exception as e:
        print(f"Error saving file: {e}")

def main():
    print("Welcome to the Data Cleaning Tool!")
    file_path = input("Enter the path to your CSV file: ").strip()
    data = load_csv(file_path)
    
    if data is not None:
        while True:
            print("\nWhat would you like to do?")
            print("1. Handle missing values")
            print("2. Remove duplicates")
            print("3. Save cleaned data")
            print("4. Exit")
            choice = input("Choose an option (1/2/3/4): ").strip()
            
            if choice == "1":
                data = handle_missing_values(data)
            elif choice == "2":
                data = remove_duplicates(data)
            elif choice == "3":
                output_path = input("Enter the path to save the cleaned CSV file: ").strip()
                save_csv(data, output_path)
            elif choice == "4":
                print("Exiting the tool. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
