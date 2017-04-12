from .models import Group

def parse_item_orders(items):
    """
    parse_item_orders takes a string of tokens representing ordered item IDs
    and parses it into a list of ordered item IDs.

    @param: items A string of tokens representing ordered item IDs.
    @return: An ordered list of item IDs.
    """
    stripped_str = items.replace('item[]=', '')
    ids = stripped_str.split('&')
    return map(int, ids)
