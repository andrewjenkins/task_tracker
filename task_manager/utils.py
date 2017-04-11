def parse_item_orders(items):
    """
    parse_item_orders takes a string of tokens representing item orders s and parses it into
    a list of orders.

    @param: items A string of tokens representing item orders.
    @return: An enumerable of item orders.
    """
    stripped_str = items.replace('item[]=', '')
    ids = stripped_str.split('&')
    return map(int, ids)
