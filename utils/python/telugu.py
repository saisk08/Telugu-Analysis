from itertools import combinations

chars = [
    'అ',
    'న',
    'వ',
    'మ',
    'య',
    'ల',
    'ర',
    'ఒ',
    'జ',
    'ఠ',
    'ఆ',
    'ఉ',
    'ఊ',
    'ఎ',
    'ఏ',
    'ప',
    'ఫ',
    'ద',
    'డ',
    'బ',
    'త',
    'క',
    'హ',
    'ణ',
    'ఘ',
]

chars_pairs = [x + '-' + y for x, y in list(combinations(chars, 2))]
