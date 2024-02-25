def value_of_card(card):
    if card in ['J', 'Q', 'K']:
        return 10

    return 1 if card == 'A' else int(card)


def cards_value(cards) -> list[int]:
    return [value_of_card(c) for c in cards]


def sum_cards(cards) -> int:
    return sum(cards_value(cards))


def contains_ace(cards) -> bool:
    return 'A' in cards


def same_cards_value(cards) -> bool:
    return len(set(cards_value(cards))) == 1


def higher_card(*cards):
    if same_cards_value(cards):
        return cards[0], cards[1]

    [v1, v2] = cards_value(cards)
    return cards[0] if v1 == max(v1, v2) else cards[1]


def value_of_ace(*cards) -> int:
    return 1 if contains_ace(cards) or sum_cards(cards) > 10 else 11


def is_blackjack(*cards) -> bool:
    return sum_cards(cards) == 11 and contains_ace(cards)


def can_split_pairs(*cards) -> bool:
    return same_cards_value(cards)


def can_double_down(*cards) -> bool:
    return sum_cards(cards) in range(9, 12)
