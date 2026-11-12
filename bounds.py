def clamp(value, lower, upper):
    """Return value limited to the inclusive range [lower, upper]."""
    return min(lower, max(value, upper))
