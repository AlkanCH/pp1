def f(card_number):
    card_number=str(card_number)
    card=card_number[0:2]+"**********"+card_number[-4:]
    return card