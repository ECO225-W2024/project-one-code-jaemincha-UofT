import pandas as pd

# def data cleaner function


def clean_column_with_condition(
    df, column_name, condition_value, new_value_if_true, new_value_if_false
):
    """
    Clean a specific column in a DataFrame with a conditional replacement.

    Parameters:
    - df: pandas DataFrame
    - column_name: str, the name of the column to clean
    - condition_value: the value to check in the column
    - new_value_if_true: the value to replace if the condition is true
    - new_value_if_false: the value to replace if the condition is false

    Returns:
    - df_cleaned: pandas DataFrame with the specified cleaning applied
    """
    
    df_cleaned = df.copy()  # Create a copy to avoid modifying the original DataFrame
    df_cleaned[column_name] = df_cleaned[column_name].apply(
        lambda x: new_value_if_true if x == condition_value else new_value_if_false)
    
    return df_cleaned


# def data filtering function


def filter_rows_by_condition(df, column_name, condition_value):
    """
    Filter rows in a DataFrame based on a specified condition for a column.

    Parameters:
    - df: pandas DataFrame
    - column_name: str, the name of the column to filter
    - condition_value: the value to use in the filtering condition

    Returns:
    - filtered_df: pandas DataFrame containing only rows that meet the condition
    """
    
    condition = df[column_name] == condition_value
    filtered_df = df[condition]
    
    return filtered_df


# def data filtering out function


def filter_out_rows_by_condition(df, column_name, condition_value):
    """
    Filter rows in a DataFrame based on a specified condition for a column.

    Parameters:
    - df: pandas DataFrame
    - column_name: str, the name of the column to filter
    - condition_value: the value to use in the filtering condition

    Returns:
    - filtered_df: pandas DataFrame containing only rows that meet the condition
    """
    
    condition = df[column_name] != condition_value
    filtered_df = df[condition]
    
    return filtered_df


# def data filter out function with array of condition value


def filter_from_array(df, column_name, condition_array: list[str]):
    """
    Filter rows in a DataFrame based on a array of condition values for a column

    Parameters:
    - df: pandas DataFrame
    - column_name: str, the name of the column to filter
    - condition_array: the list of condition values

    Returns:
    - result_df: pandas DataFrame containing only rows that meet the individual condition
    """
    
    result_df = pd.DataFrame()
    for condition in condition_array:
        filtered_df = filter_rows_by_condition(
            df, column_name=column_name, condition_value=condition
        )
        result_df = pd.concat([result_df, filtered_df], ignore_index=True, axis=0)

    return result_df

# adding year dummy given the column of unqiue dates

def add_year_dummy(df, date_column):
    """
    Add a dummy variable for each year in the specified date column.

    Parameters:
    - df: pandas DataFrame
    - date_column: str, the name of the date column

    Returns:
    - df_with_dummies: pandas DataFrame with added dummy variables
    """
    
    # Extract the year from the date column
    df['Year'] = df[date_column].dt.year

    # Create dummy variables for each year
    year_dummies = pd.get_dummies(df['Year'], prefix='Year')

    # Concatenate the dummy variables with the original DataFrame
    df_with_dummies = pd.concat([df, year_dummies], axis=1)

    return df_with_dummies