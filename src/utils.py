"""
Utility functions for SCE data analysis
"""

import pandas as pd
import numpy as np
from typing import List, Dict, Tuple


def identify_column_types(df: pd.DataFrame) -> Dict[str, List[str]]:
    """
    Categorize columns by their type and content.
    
    Parameters
    ----------
    df : pd.DataFrame
        Input dataframe
        
    Returns
    -------
    Dict[str, List[str]]
        Dictionary with column categories
    """
    column_types = {
        'numeric': df.select_dtypes(include=[np.number]).columns.tolist(),
        'categorical': df.select_dtypes(include=['object', 'category']).columns.tolist(),
        'datetime': df.select_dtypes(include=['datetime64']).columns.tolist(),
        'boolean': df.select_dtypes(include=['bool']).columns.tolist()
    }
    
    return column_types


def missing_data_summary(df: pd.DataFrame, threshold: float = 0.0) -> pd.DataFrame:
    """
    Generate summary of missing data.
    
    Parameters
    ----------
    df : pd.DataFrame
        Input dataframe
    threshold : float
        Minimum percentage of missing data to include (0-100)
        
    Returns
    -------
    pd.DataFrame
        Summary dataframe with missing counts and percentages
    """
    missing = df.isnull().sum()
    missing_pct = (missing / len(df)) * 100
    
    summary = pd.DataFrame({
        'Missing_Count': missing,
        'Missing_Percentage': missing_pct,
        'Data_Type': df.dtypes
    }).sort_values('Missing_Percentage', ascending=False)
    
    return summary[summary['Missing_Percentage'] >= threshold]


def detect_outliers_iqr(series: pd.Series, multiplier: float = 1.5) -> Tuple[pd.Series, Dict]:
    """
    Detect outliers using IQR method.
    
    Parameters
    ----------
    series : pd.Series
        Input numeric series
    multiplier : float
        IQR multiplier for outlier bounds
        
    Returns
    -------
    Tuple[pd.Series, Dict]
        Boolean series indicating outliers and dictionary with bounds
    """
    Q1 = series.quantile(0.25)
    Q3 = series.quantile(0.75)
    IQR = Q3 - Q1
    
    lower_bound = Q1 - multiplier * IQR
    upper_bound = Q3 + multiplier * IQR
    
    outliers = (series < lower_bound) | (series > upper_bound)
    
    bounds = {
        'Q1': Q1,
        'Q3': Q3,
        'IQR': IQR,
        'lower_bound': lower_bound,
        'upper_bound': upper_bound,
        'n_outliers': outliers.sum()
    }
    
    return outliers, bounds


def summarize_categorical(df: pd.DataFrame, col: str, top_n: int = 10) -> pd.DataFrame:
    """
    Summarize categorical variable with counts and percentages.
    
    Parameters
    ----------
    df : pd.DataFrame
        Input dataframe
    col : str
        Column name
    top_n : int
        Number of top categories to show
        
    Returns
    -------
    pd.DataFrame
        Summary with counts and percentages
    """
    value_counts = df[col].value_counts()
    percentages = (value_counts / len(df)) * 100
    
    summary = pd.DataFrame({
        'Count': value_counts,
        'Percentage': percentages,
        'Cumulative_Percentage': percentages.cumsum()
    }).head(top_n)
    
    return summary


def calculate_weighted_stats(df: pd.DataFrame, value_col: str, weight_col: str) -> Dict:
    """
    Calculate weighted statistics for a variable.
    
    Parameters
    ----------
    df : pd.DataFrame
        Input dataframe
    value_col : str
        Column with values
    weight_col : str
        Column with weights
        
    Returns
    -------
    Dict
        Dictionary with weighted statistics
    """
    data = df[[value_col, weight_col]].dropna()
    
    weighted_mean = np.average(data[value_col], weights=data[weight_col])
    weighted_median = weighted_quantile(data[value_col], data[weight_col], 0.5)
    
    stats = {
        'weighted_mean': weighted_mean,
        'weighted_median': weighted_median,
        'unweighted_mean': data[value_col].mean(),
        'unweighted_median': data[value_col].median(),
        'n_obs': len(data)
    }
    
    return stats


def weighted_quantile(values: pd.Series, weights: pd.Series, quantile: float) -> float:
    """
    Calculate weighted quantile.
    
    Parameters
    ----------
    values : pd.Series
        Values
    weights : pd.Series
        Weights
    quantile : float
        Quantile to calculate (0-1)
        
    Returns
    -------
    float
        Weighted quantile value
    """
    sorted_idx = np.argsort(values)
    sorted_values = values.iloc[sorted_idx]
    sorted_weights = weights.iloc[sorted_idx]
    
    cum_weights = sorted_weights.cumsum()
    cutoff = quantile * cum_weights.iloc[-1]
    
    return sorted_values.iloc[np.searchsorted(cum_weights, cutoff)]

