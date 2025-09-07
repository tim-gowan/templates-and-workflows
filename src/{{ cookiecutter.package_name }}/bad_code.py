# src/bad_code.py

def process_data(data, user_type, region, is_admin, has_promo, order_total):
    """
    This function is a mess. It has high cyclomatic complexity due to
    deeply nested conditionals and multiple responsibilities, making it
    brittle and hard to test.
    """
    # This entire block will be flagged by radon for high complexity.
    if data:
        if user_type == "premium":
            if region == "US":
                if order_total > 100 or has_promo:
                    # Apply a special discount
                    return {"status": "success", "discount": 0.20}
                else:
                    return {"status": "success", "discount": 0.10}
            elif region == "EU":
                if order_total > 120:
                    # Another nested conditional
                    if has_promo:
                        return {"status": "success", "discount": 0.30}
                    return {"status": "success", "discount": 0.25}
                else:
                    return {"status": "success", "discount": 0.15}
        elif user_type == "guest":
            if has_promo and order_total > 50:
                return {"status": "success", "discount": 0.05}
    elif is_admin:
        # Admin bypass path adds another branch
        return {"status": "admin_bypass"}

    # Default case with no clear path
    return {"status": "no_action"}
