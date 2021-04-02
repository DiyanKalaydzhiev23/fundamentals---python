tickets = input().split(",")


for ticket in tickets:
    result = ""
    ticket = ticket.strip()
    symbol = None
    current_count = 0
    if len(ticket) == 20:
        first_half = ticket[:int(len(ticket)/2)]
        second_half = ticket[int(len(ticket)/2):]
        monkey_a = first_half.count("@")
        hashtag = first_half.count("#")
        dollar = first_half.count("$")
        house = first_half.count("^")
        if monkey_a >= 6:
            symbol = "@"
            current_count = monkey_a
        elif hashtag >= 6:
            symbol = "#"
            current_count = hashtag
        elif dollar >= 6:
            symbol = "$"
            current_count = dollar
        elif house >= 6:
            symbol = "^"
            current_count = house
        if symbol:
            count_symbol = second_half.count(symbol)
            if current_count + count_symbol == 20:
                result = f'ticket "{ticket}" - 10{symbol} Jackpot!'
            elif count_symbol >= current_count:
                result = f'ticket "{ticket}" - {current_count}{symbol}'
            elif current_count > count_symbol:
                result = f'ticket "{ticket}" - {count_symbol}{symbol}'
            elif count_symbol < 6 or current_count < 6:
                result = f'ticket "{ticket}" - no match'
        else:
            result = f'ticket "{ticket}" - no match'
    else:
        result = "invalid ticket"
    print(result)
