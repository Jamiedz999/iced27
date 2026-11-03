"""Fuzzy passage search — the moving-window matcher extracted from uCeltic."""

from .common import calculate_dissimilarity_score, tokenize_query
from .optimized import moving_window_similarity1, run_search

__all__ = [
    "run_search",
    "tokenize_query",
    "moving_window_similarity1",
    "calculate_dissimilarity_score",
]
