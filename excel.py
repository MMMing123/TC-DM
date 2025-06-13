from openpyxl import load_workbook
import pandas as pd


# Data is passed in as a row
def update_Excel(data):
    # 1. Load existing Excel file
    file_path = "Resources/dms.xlsx"
    wb = load_workbook(file_path)
    ws = wb.active  # Select active worksheet (or by name: ws = wb["Sheet1"])

    # 2. Find next row after last row and append data
    ws.append(data)

    # 3. Save file (overwrite original file)
    wb.save(file_path)


def read_Excel():
    file_path = "Resources/dms.xlsx"  # Replace with your Excel file path
    df = pd.read_excel(file_path, engine='openpyxl')  # For .xlsx files

    # Sort by time in third column (column index 2) descending
    # First ensure time column is datetime type (optional based on data)
    df[df.columns[2]] = pd.to_datetime(df[df.columns[2]])
    # Sort by time descending and update DataFrame
    df.sort_values(by=df.columns[2], ascending=False, inplace=True)
    return df