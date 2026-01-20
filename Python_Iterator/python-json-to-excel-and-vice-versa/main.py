import pandas as pd

def build_dataframe(headers: dict, rows: list) -> pd.DataFrame:
    """
    Build a pandas DataFrame with hierarchical headers.
    """
    column_tuples = []
    for dict_key, dict_value in headers.items():
        if dict_value is None:  # Simple column
            column_tuples.append((dict_key, ""))
        else:  # Group with subcolumns
            for sub in dict_value:
                column_tuples.append((dict_key, sub))

    flat_rows = []
    for row in rows:
        flat_row = []
        for dict_key, dict_value in headers.items():
            if dict_value is None:  # single column
                flat_row.append(row.get(dict_key, ""))
            else:
                for sub in dict_value:
                    flat_row.append(row.get(dict_key, {}).get(sub, ""))

        flat_rows.append(flat_row)

    df = pd.DataFrame(flat_rows, columns=pd.MultiIndex.from_tuples(column_tuples))
    return df


def dict_to_excel(headers: dict, rows: list, filename: str):
    df = build_dataframe(headers, rows)
    df.to_excel(filename, index=True)   # ✅ must keep index for MultiIndex columns
    print(f"Excel file '{filename}' created successfully!")


# -----------------------
# ✅ Example Usage
# -----------------------
if __name__ == "__main__":
    
    headers = {
        "Name": None,
        "Age": None,
        "People Details": ["Person 1", "Person 2", "Person 3"],
        "Contact Details": ["Email", "Phone"]
    }

    rows = [
        {
            "Name": "connor",
            "Age": 24,
            "People Details": {"Person 1": "Jack", "Person 2": "Sam", "Person 3": "Peter"},
            "Contact Details": {"Email": "connor@example.com", "Phone": "111-222"}
        },
        {
            "Name": "patrik",
            "Age": 28,
            "Contact Details": {"Email": "patrik@example.com", "Phone": "333-444"},
            "People Details": {"Person 1": "Alex", "Person 2": "John", "Person 3": "Ravi"},
        }
    ]

    dict_to_excel(headers, rows, "structured_output.xlsx")
