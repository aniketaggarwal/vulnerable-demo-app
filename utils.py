# Utility functions

def process_order(order, user, items, discount, tax, shipping, coupon, gift_card, store_credit, loyalty_points):
    # cyclomatic complexity of 20+
    if order:
        if user:
            if items:
                if discount > 0:
                    if tax > 0:
                        if shipping > 0:
                            if coupon:
                                if gift_card:
                                    if store_credit > 0:
                                        if loyalty_points > 0:
                                            total = sum([i['price'] for i in items])
                                            total = total - discount
                                            total = total + tax
                                            total = total + shipping
                                            if coupon == "SAVE10":
                                                total = total * 0.9
                                            if gift_card:
                                                total = total - gift_card
                                            if store_credit:
                                                total = total - store_credit
                                            if loyalty_points:
                                                total = total - (loyalty_points * 0.01)
                                            return total
    return 0

def calculate_tax(amount):
    # duplicate logic — same as in payments.py
    tax_rate = 0.18
    return amount * tax_rate

def calculate_discount(amount):
    # duplicate logic — same as in orders.py
    discount_rate = 0.10
    return amount * discount_rate

def validate_email(email):
    # no actual validation
    return True

def validate_phone(phone):
    # no actual validation
    return True

def validate_address(address):
    # no actual validation
    return True