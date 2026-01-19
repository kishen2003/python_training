users = {}
_current_id = 1

def get_next_id() -> int:
    global _current_id
    value = _current_id
    _current_id += 1
    return value