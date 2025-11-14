"""
Weighting pipeline for SCE data
"""

import pandas as pd
import numpy as np
from typing import List, Dict, Optional


def validate_weights(df: pd.DataFrame, weight_col: str) -> Dict:
    """
    Validate survey weights.
    
    Parameters
    ----------
    df : pd.DataFrame
        Input dataframe
    weight_col : str
        Name of weight column
        
    Returns
    -------
    Dict
        Validation statistics
    """
    weights = df[weight_col].dropna()
    
    validation = {
        'min': weights.min(),
        'max': weights.max(),
        'mean': weights.mean(),
        'median': weights.median(),
        'sum': weights.sum(),
        'n_missing': df[weight_col].isnull().sum(),
        'n_negative': (weights < 0).sum(),
        'n_zero': (weights == 0).sum()
    }
    
    return validation


def trim_extreme_weights(df: pd.DataFrame, 
                        weight_col: str,
                        lower_percentile: float = 1,
                        upper_percentile: float = 99) -> pd.DataFrame:
    """
    Trim extreme weights to reduce variance.
    
    Parameters
    ----------
    df : pd.DataFrame
        Input dataframe
    weight_col : str
        Name of weight column
    lower_percentile : float
        Lower percentile for trimming
    upper_percentile : float
        Upper percentile for trimming
        
    Returns
    -------
    pd.DataFrame
        Dataframe with trimmed weights
    """
    df_trim = df.copy()
    
    lower_bound = df[weight_col].quantile(lower_percentile / 100)
    upper_bound = df[weight_col].quantile(upper_percentile / 100)
    
    df_trim[f'{weight_col}_trimmed'] = df[weight_col].clip(
        lower=lower_bound, 
        upper=upper_bound
    )
    
    return df_trim


def normalize_weights(df: pd.DataFrame, 
                     weight_col: str,
                     target_sum: Optional[float] = None) -> pd.DataFrame:
    """
    Normalize weights to sum to a target value.
    
    Parameters
    ----------
    df : pd.DataFrame
        Input dataframe
    weight_col : str
        Name of weight column
    target_sum : Optional[float]
        Target sum for weights. If None, normalizes to sample size.
        
    Returns
    -------
    pd.DataFrame
        Dataframe with normalized weights
    """
    df_norm = df.copy()
    
    if target_sum is None:
        target_sum = len(df)
    
    current_sum = df[weight_col].sum()
    df_norm[f'{weight_col}_normalized'] = df[weight_col] * (target_sum / current_sum)
    
    return df_norm


def create_post_stratification_weights(df: pd.DataFrame,
                                       strata_cols: List[str],
                                       population_margins: Dict[str, Dict],
                                       base_weight_col: Optional[str] = None) -> pd.DataFrame:
    """
    Create post-stratification weights to match population margins.
    
    Parameters
    ----------
    df : pd.DataFrame
        Input dataframe
    strata_cols : List[str]
        Columns defining strata
    population_margins : Dict[str, Dict]
        Population margins for each stratum variable
    base_weight_col : Optional[str]
        Base weight column. If None, uses equal weights.
        
    Returns
    -------
    pd.DataFrame
        Dataframe with post-stratification weights
    """
    df_weighted = df.copy()
    
    # Start with base weights
    if base_weight_col is None:
        df_weighted['base_weight'] = 1.0
    else:
        df_weighted['base_weight'] = df[base_weight_col]
    
    # Calculate adjustment factors for each stratum
    df_weighted['ps_weight'] = df_weighted['base_weight']
    
    for col in strata_cols:
        if col in population_margins:
            # Calculate sample proportions
            sample_dist = df_weighted.groupby(col)['base_weight'].sum()
            sample_dist = sample_dist / sample_dist.sum()
            
            # Create adjustment factors
            pop_margins = pd.Series(population_margins[col])
            adjustment = pop_margins / sample_dist
            
            # Apply adjustment
            df_weighted['ps_weight'] *= df_weighted[col].map(adjustment)
    
    return df_weighted


def calculate_effective_sample_size(weights: pd.Series) -> float:
    """
    Calculate effective sample size from weights.
    
    Parameters
    ----------
    weights : pd.Series
        Survey weights
        
    Returns
    -------
    float
        Effective sample size
    """
    return (weights.sum() ** 2) / (weights ** 2).sum()


def compute_weighted_distribution(df: pd.DataFrame,
                                 var_col: str,
                                 weight_col: str,
                                 bins: Optional[int] = None) -> pd.DataFrame:
    """
    Compute weighted distribution of a variable.
    
    Parameters
    ----------
    df : pd.DataFrame
        Input dataframe
    var_col : str
        Variable column
    weight_col : str
        Weight column
    bins : Optional[int]
        Number of bins for continuous variables
        
    Returns
    -------
    pd.DataFrame
        Weighted distribution
    """
    data = df[[var_col, weight_col]].dropna()
    
    if bins is not None:
        # For continuous variables, create bins
        data['bin'] = pd.cut(data[var_col], bins=bins)
        grouped = data.groupby('bin')[weight_col].sum()
    else:
        # For categorical variables
        grouped = data.groupby(var_col)[weight_col].sum()
    
    distribution = pd.DataFrame({
        'weighted_count': grouped,
        'weighted_percentage': (grouped / grouped.sum()) * 100
    })
    
    return distribution

