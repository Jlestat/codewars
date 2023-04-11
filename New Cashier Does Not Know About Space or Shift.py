def get_order(order: str) -> str:
    return f"{'Burger ' * order.count('burger')}" \
        f"{'Fries ' * order.count('fries')}" \
        f"{'Chicken ' * order.count('chicken')}" \
        f"{'Pizza ' * order.count('pizza')}" \
        f"{'Sandwich ' * order.count('sandwich')}" \
        f"{'Onionrings ' * order.count('onionrings')}" \
        f"{'Milkshake ' * order.count('milkshake')}" \
        f"{'Coke ' * order.count('coke')}".rstrip()


print(get_order("milkshakepizzachickenfriescokeburgerpizzasandwichmilkshakepizza"))