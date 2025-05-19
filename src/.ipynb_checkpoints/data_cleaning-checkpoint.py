import ast

def process_column(df, column_name, key_name=None):
    """
    Cleans columns with stringified lists of dictionaries.
    Extracts the desired key from each dictionary.

    Arguments:
        df : The DataFrame to process.
        column_name : Name of the column to transform.
        key_name: Key to extract from the dictionaries.

    Returns:
        pd.DataFrame: Modified DataFrame with transformed column.
    """
    def extract_value(x):
        if isinstance(x, str):
            try:
                data = ast.literal_eval(x)
                if isinstance(data, list):
                    if key_name:
                        return [item[key_name] for item in data if key_name in item]
                    else:
                        return data
                else:
                    return data
            except:
                return None
        return None

    df[column_name] = df[column_name].apply(extract_value)
    return df

