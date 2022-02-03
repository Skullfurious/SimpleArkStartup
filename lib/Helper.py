class Helper:
    def __init__(self):
        pass

    def to_bool(s: str):
        """evaluates if lowered input is equivalent to true, 1, t, y, and yes."""
        if len(s) > 0:
            return s.lower() in ['true', '1', 't', 'y', 'yes', 'tr', 'tru']
        else:
            return False

    def clamp(n, minn, maxn):
        return max(min(maxn, n), minn)