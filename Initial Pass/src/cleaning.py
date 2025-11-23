"""
Data cleaning functions for SCE data
"""

import pandas as pd
import numpy as np
from typing import List, Optional


def standardize_column_names(df: pd.DataFrame) -> pd.DataFrame:
    """
    Standardize column names (lowercase, replace spaces with underscores).
    
    Parameters
    ----------
    df : pd.DataFrame
        Input dataframe
        
    Returns
    -------
    pd.DataFrame
        Dataframe with standardized column names
    """
    df_clean = df.copy()
    df_clean.columns = (df_clean.columns
                        .str.strip()
                        .str.lower()
                        .str.replace(' ', '_')
                        .str.replace('[^a-z0-9_]', '', regex=True))
    return df_clean


def convert_percentage_columns(df: pd.DataFrame, percent_cols: Optional[List[str]] = None) -> pd.DataFrame:
    """
    Convert percentage columns to numeric format.
    
    Parameters
    ----------
    df : pd.DataFrame
        Input dataframe
    percent_cols : Optional[List[str]]
        List of percentage columns. If None, auto-detect.
        
    Returns
    -------
    pd.DataFrame
        Dataframe with converted percentage columns
    """
    df_clean = df.copy()
    
    if percent_cols is None:
        # Auto-detect columns that might be percentages
        percent_cols = [col for col in df.columns if 
                       any(x in col.lower() for x in ['percent', 'pct', 'rate', 'prob'])]
    
    for col in percent_cols:
        if col in df_clean.columns:
            # Remove % sign if present and convert to float
            if df_clean[col].dtype == 'object':
                df_clean[col] = (df_clean[col]
                                .str.replace('%', '')
                                .str.replace(',', '')
                                .astype(float))
    
    return df_clean


def handle_special_values(df: pd.DataFrame, 
                          na_values: Optional[List] = None) -> pd.DataFrame:
    """
    Replace special values with NaN.
    
    Parameters
    ----------
    df : pd.DataFrame
        Input dataframe
    na_values : Optional[List]
        List of values to treat as NaN
        
    Returns
    -------
    pd.DataFrame
        Dataframe with special values replaced
    """
    df_clean = df.copy()
    
    if na_values is None:
        na_values = [-999, -99, -9, 'N/A', 'NA', 'n/a', '', ' ']
    
    df_clean = df_clean.replace(na_values, np.nan)
    
    return df_clean


def validate_density_bins(df: pd.DataFrame, 
                         bin_cols: List[str], 
                         tolerance: float = 1.0) -> pd.DataFrame:
    """
    Validate that density forecast bins sum to 100%.
    
    Parameters
    ----------
    df : pd.DataFrame
        Input dataframe
    bin_cols : List[str]
        List of density bin columns
    tolerance : float
        Acceptable deviation from 100
        
    Returns
    -------
    pd.DataFrame
        Validation results
    """
    bin_sums = df[bin_cols].sum(axis=1)
    
    validation = pd.DataFrame({
        'row_index': df.index,
        'bin_sum': bin_sums,
        'deviation': np.abs(bin_sums - 100),
        'valid': np.abs(bin_sums - 100) <= tolerance
    })
    
    return validation


def remove_duplicates(df: pd.DataFrame, 
                     subset: Optional[List[str]] = None,
                     keep: str = 'first') -> pd.DataFrame:
    """
    Remove duplicate rows.
    
    Parameters
    ----------
    df : pd.DataFrame
        Input dataframe
    subset : Optional[List[str]]
        Columns to check for duplicates
    keep : str
        Which duplicates to keep ('first', 'last', False)
        
    Returns
    -------
    pd.DataFrame
        Dataframe with duplicates removed
    """
    df_clean = df.drop_duplicates(subset=subset, keep=keep)
    
    n_removed = len(df) - len(df_clean)
    if n_removed > 0:
        print(f"Removed {n_removed} duplicate rows")
    
    return df_clean


def clip_outliers(series: pd.Series, 
                 lower_percentile: float = 1, 
                 upper_percentile: float = 99) -> pd.Series:
    """
    Clip outliers to specified percentiles.
    
    Parameters
    ----------
    series : pd.Series
        Input series
    lower_percentile : float
        Lower percentile bound (0-100)
    upper_percentile : float
        Upper percentile bound (0-100)
        
    Returns
    -------
    pd.Series
        Series with clipped values
    """
    lower_bound = series.quantile(lower_percentile / 100)
    upper_bound = series.quantile(upper_percentile / 100)
    
    return series.clip(lower=lower_bound, upper=upper_bound)

