import pandas as pd

def excel_to_dict(filename: str):
    # Read Excel with two header rows
    df = pd.read_excel(filename, header=[0, 1], index_col=0)

    # Normalize "Unnamed: ..." to ""
    clean_columns = []
    for top, sub in df.columns:
        if isinstance(sub, str) and sub.startswith("Unnamed"):
            sub = ""  # replace with empty for single columns
        clean_columns.append((top, sub))

    df.columns = pd.MultiIndex.from_tuples(clean_columns)

    # Step 1: Rebuild headers
    headers = {}
    for top, sub in df.columns:
        if sub == "" or pd.isna(sub):  # simple column
            headers[top] = None
        else:  # grouped column
            headers.setdefault(top, [])
            if sub not in headers[top]:
                headers[top].append(sub)

    # Step 2: Rebuild rows
    rows = []
    for _, row in df.iterrows():
        row_dict = {}
        for top, sub in df.columns:
            if headers[top] is None:  # simple
                row_dict[top] = row[(top, sub)]
            else:  # grouped
                row_dict.setdefault(top, {})
                row_dict[top][sub] = row[(top, sub)]
        rows.append(row_dict)

    return headers, rows


# -----------------------
# ✅ Example usage
# -----------------------
if __name__ == "__main__":
    headers, rows = excel_to_dict("structured_output.xlsx")

    print("\nRecovered headers:")
    print(headers)

    print("\nRecovered rows:")
    for r in rows:
        print(r)
