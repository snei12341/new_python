# total wholesale cost for 60 copies

# wholesale_book_cost.py
# Calculates the wholesale cost for multiple copies of a book with discount and shipping

def calculate_wholesale_price(cover_price, discount):
    """
    Returns the discounted price of the book.
    """
    return cover_price * (1 - discount)


def calculate_total_cost(discounted_price, shipping_first, shipping_additional, num_copies):
    """
    Calculates the total wholesale cost for a given number of copies.

    :param discounted_price: price after bookstore discount
    :param shipping_first: shipping cost for the first copy
    :param shipping_additional: shipping cost per additional copy
    :param num_copies: total number of books
    :return: total wholesale cost
    """
    total_book_cost = discounted_price * num_copies
    total_shipping_cost = shipping_first + shipping_additional * (num_copies - 1)
    return total_book_cost + total_shipping_cost


def main():
    cover_price = 24.95
    discount = 0.40
    shipping_first_copy = 3.00
    shipping_per_additional = 0.75
    number_of_copies = 60

    discounted_price = calculate_wholesale_price(cover_price, discount)
    total_cost = calculate_total_cost(discounted_price, shipping_first_copy, shipping_per_additional, number_of_copies)

    print(f"Total wholesale cost for {number_of_copies} copies: R$ {total_cost:.2f}")


if __name__ == "__main__":
    main()
