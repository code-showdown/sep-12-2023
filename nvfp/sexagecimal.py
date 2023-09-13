


def get_sexagecimal(secs: float, /, include_ms: bool = False) -> str:
    """
    Converts seconds to sexagesimal format.

    ## Demo
    >>> get_sexagecimal(3661.345)
    '01:01:01'

    """
    sign = '-' if secs < 0 else ''
    secs_abs = abs(secs)
    hours, remainder = divmod(secs_abs, 3600)
    minutes, seconds = divmod(remainder, 60)

    h = str(int(hours)).zfill(2)
    m = str(int(minutes)).zfill(2)

    if include_ms:
        s = f'{seconds:.3f}'.zfill(6)
    else:
        s = str(round(seconds)).zfill(2)

    return sign + ':'.join([h, m, s])


def sexagecimal_to_secs(sexagecimal: str, /) -> float:
    """
    ## Exceptions
    - `ValueError` if `sexagecimal` is invalid

    ## Demo
    - `sexagecimal_to_secs('1.25')` -> `1.25`
    - `sexagecimal_to_secs('01:01.25')` -> `61.25`
    - `sexagecimal_to_secs('1:1:5.25')` -> `3665.25`
    """
    _s = sexagecimal.strip(' ')

    res = _re.match(r'^(?P<sign>\+|-)?(?:(?:(?P<h>\d+):)?(?:(?P<m>[0-5]?\d):))?(?P<s>[0-5]?\d(?:\.\d*)?)$', _s)
    if res is None:
        raise ValueError(f'Invalid sexagecimal: {repr(sexagecimal)}')

    sign = res.group('sign')
    if sign in (None, '+'):
        sign = 1
    else:
        sign = -1

    h = res.group('h')
    if h is None:
        h = 0

    m = res.group('m')
    if m is None:
        m = 0

    s = res.group('s')

    return sign * (int(h)*3600 + int(m)*60 + float(s))
