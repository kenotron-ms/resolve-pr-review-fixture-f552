def clamp(value, lower, upper):
    """Return value limited to the inclusive range [lower, upper].

    Values below lower return lower. Values above upper return upper.
    Values already inside the range are returned unchanged.
    """
    return max(lower, min(value, upper))
