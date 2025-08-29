import re
from dataclasses import dataclass
from typing import List, Sequence

RE_INT = re.compile(r"^[+-]?\d+$")          # pure integer string (optional sign)
RE_ALPHA = re.compile(r"^[A-Za-z]+$")       # only letters
RE_SPECIAL = re.compile(r"^[^A-Za-z0-9]+$") # only non-alphanumeric

@dataclass
class Processed:
    odd_numbers: List[str]
    even_numbers: List[str]
    alphabets: List[str]
    special_characters: List[str]
    sum_numbers: int
    concat_string: str

def _is_int_str(s: str) -> bool:
    return bool(RE_INT.match(s))

def _is_alpha_str(s: str) -> bool:
    return bool(RE_ALPHA.match(s))

def _is_special_only(s: str) -> bool:
    return bool(RE_SPECIAL.match(s))

def _alt_caps_reverse(all_letters: Sequence[str]) -> str:
    # Reverse and apply alternating caps: Upper, lower, Upper, ...
    rev = list(reversed(all_letters))
    return "".join(ch.upper() if i % 2 == 0 else ch.lower() for i, ch in enumerate(rev))

def process_payload(raw_items: Sequence[object]) -> Processed:
    # Normalize everything to strings
    items = [str(x) for x in raw_items]

    odd_numbers: List[str] = []
    even_numbers: List[str] = []
    alphabets: List[str] = []
    special_characters: List[str] = []
    total = 0
    letters_stream: List[str] = []

    for token in items:
        # Collect letters from anywhere (for concat_string)
        for ch in token:
            if ch.isalpha():
                letters_stream.append(ch)

        # Classify full tokens
        if _is_int_str(token):
            n = int(token)
            total += n
            if abs(n) % 2 == 0:
                even_numbers.append(token)      # must stay as strings
            else:
                odd_numbers.append(token)
        elif _is_alpha_str(token):
            alphabets.append(token.upper())     # uppercased tokens
        elif _is_special_only(token):
            special_characters.append(token)
        else:
            # Mixed tokens like "a1", "x-y", "3.14" -> treat as special
            special_characters.append(token)

    return Processed(
        odd_numbers=odd_numbers,
        even_numbers=even_numbers,
        alphabets=alphabets,
        special_characters=special_characters,
        sum_numbers=total,
        concat_string=_alt_caps_reverse(letters_stream),
    )
