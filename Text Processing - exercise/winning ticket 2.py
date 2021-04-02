tickets = input().split(",")
winner_elements = ["@", "#", "$", "^"]

for ticket in tickets:
    result = ""
    ticket = ticket.strip()
    symbol = None
    current_count = 0
    if len(ticket) == 20:
        first_half = ticket[:int(len(ticket)/2)]
        second_half = ticket[int(len(ticket)/2):]
        winning_part = []
        max_num_1 = 0
        for i in range(len(first_half)):
            el = first_half[i]
            symbol = el
            while el in winner_elements and el == symbol:
                winning_part.append(el)
                i += 1
                if i < len(first_half):
                    el = first_half[i]
                else:
                    break
            if len(winning_part) >= 6:
                break
            else:
                winning_part = []
        winning_symbol_1 = ""
        if len(winning_part) >= 6:
            max_num_1 = len(winning_part)
            if "@" in winning_part:
                winning_symbol_1 = "@"
            elif "#" in winning_part:
                winning_symbol_1 = "#"
            elif "$" in winning_part:
                winning_symbol_1 = "$"
            elif "^" in winning_part:
                winning_symbol_1 = "^"
        winning_part = []
        max_num_2 = 0
        for i in range(len(second_half)):
            el = second_half[i]
            symbol = el
            while el in winner_elements and el == symbol:
                winning_part.append(el)
                i += 1
                if i < len(second_half):
                    el = second_half[i]
                else:
                    break
            if len(winning_part) >= 6:
                break
            else:
                winning_part = []
        winning_symbol_2 = ""
        if len(winning_part) >= 6:
            max_num_2 = len(winning_part)
            if "@" in winning_part:
                winning_symbol_2 = "@"
            elif "#" in winning_part:
                winning_symbol_2 = "#"
            elif "$" in winning_part:
                winning_symbol_2 = "$"
            elif "^" in winning_part:
                winning_symbol_2 = "^"
        if max_num_1 and max_num_2 and winning_symbol_1 == winning_symbol_2:
            if max_num_1 + max_num_2 == 20:
                result = f'ticket "{ticket}" - 10{winning_symbol_1} Jackpot!'
            else:
                if max_num_1 >= max_num_2:
                    result = f'ticket "{ticket}" - {max_num_2}{winning_symbol_2}'
                else:
                    result = f'ticket "{ticket}" - {max_num_1}{winning_symbol_1}'
        else:
            result = f'ticket "{ticket}" - no match'
    else:
        result = f'invalid ticket'
    print(result)
