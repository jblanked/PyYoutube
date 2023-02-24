def ordered(prices):
    sorted_prices = []
    for item in prices:
        if not sorted_prices:
            sorted_prices.append(item)
        else:
            # iterates over the elements of sorted_prices and
            # keeps track of both the index and value of each element in the list.
            for i, sorted_item in enumerate(sorted_prices):
                if item < sorted_item:
                    sorted_prices.insert(i, item)
                    break
            else:
                sorted_prices.append(item)
    return sorted_prices

# i, sorted_item: These are variables that are assigned the index and value of each element
# in the sequence being iterated over (in this case, sorted_prices).
# The i variable keeps track of the index of each element and the
# sorted_item variable keeps track of the value of each element.

# in enumerate(sorted_prices): This part specifies the sequence being iterated over and
# also uses the enumerate function to get both the index and value of each element in the sequence.
# The enumerate function takes a sequence (in this case, sorted_prices) as an argument and
#  returns an enumerate object that produces pairs of index and value.
