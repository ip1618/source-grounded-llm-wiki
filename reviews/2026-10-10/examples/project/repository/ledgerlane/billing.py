"""Pure invoice arithmetic for the prototype. Amounts are integer cents."""


def calculate_invoice(lines, tax_basis_points, discount_cents=0):
    subtotal_cents = sum(line["unit_price_cents"] * line["quantity"] for line in lines)
    if discount_cents < 0 or discount_cents > subtotal_cents:
        raise ValueError("discount must be between zero and the subtotal")
    taxable_cents = subtotal_cents - discount_cents
    tax_cents = (taxable_cents * tax_basis_points + 5000) // 10000
    return {
        "subtotal_cents": subtotal_cents,
        "discount_cents": discount_cents,
        "taxable_cents": taxable_cents,
        "tax_cents": tax_cents,
        "total_cents": taxable_cents + tax_cents,
    }
