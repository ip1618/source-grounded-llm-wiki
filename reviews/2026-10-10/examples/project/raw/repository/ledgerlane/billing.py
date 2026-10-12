"""Pure invoice arithmetic for the prototype. Amounts are integer cents."""


def calculate_invoice(lines, tax_basis_points):
    subtotal_cents = sum(line["unit_price_cents"] * line["quantity"] for line in lines)
    tax_cents = (subtotal_cents * tax_basis_points + 5000) // 10000
    return {
        "subtotal_cents": subtotal_cents,
        "tax_cents": tax_cents,
        "total_cents": subtotal_cents + tax_cents,
    }
