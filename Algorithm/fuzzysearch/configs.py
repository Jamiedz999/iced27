"""The configurations compared in the ablation: name -> stage options.

Each value is passed as-is to `pipeline.moving_window`. Only stage choices
belong here; experimental conditions (window ratio, threshold, step, query
length) are set by the caller and shared by every configuration.

Adding an optimisation: implement it as an option of its stage in
`pipeline.py`, then add the configurations that use it below.
`tests/test_configs.py` checks every entry against the naive scan and
`bench/bench_search.py` times every entry.
"""

CONFIGS = {
    "baseline":        {"distance": "compute", "pruning": "none"},
    "prefilter":       {"distance": "compute", "pruning": "lower_bound"},
    "table":           {"distance": "table",   "pruning": "none"},
    "table+prefilter": {"distance": "table",   "pruning": "lower_bound"},
}
