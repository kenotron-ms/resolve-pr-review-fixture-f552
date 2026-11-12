def clamp(value, lower, upper):
    """Return value limited to the inclusive range [lower, upper]."""
    return max(lower, min(value, upper))
