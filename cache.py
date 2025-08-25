import hashlib

_cache = {}
_user_scores = {}

def get_cache_key(name: str, birth_date: str, date_today: str) -> str:
    key_raw = f"{name}:{birth_date}:{date_today}"
    return hashlib.md5(key_raw.encode()).hexdigest()

def get_cached_response(key: str):
    return _cache.get(key)

def set_cached_response(key: str, response: dict):
    _cache[key] = response

def get_user_score(name: str, birth_date: str, birth_time: str) -> int:
    """
    Calculate or retrieve a score for the user.
    Score ranges 0-10, deterministic based on user info hash.
    """
    if name not in _user_scores:
        key = f"{name}{birth_date}{birth_time}"
        val = int(hashlib.md5(key.encode()).hexdigest(), 16)
        _user_scores[name] = val % 11
    return _user_scores[name]
