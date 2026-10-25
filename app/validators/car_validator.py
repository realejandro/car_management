def validate_car_data(data):
    errors = []

    # required fields
    required_fields = ["brand", "model", "year", "price", "vin", "mileage"]

    for field in required_fields:
        if field not in data:
            errors.append(f"{field} is required")

    # type + logic validation
    if "price" in data:
        try:
            price = float(data["price"])
            if price <= 0:
                errors.append("price must be greater than 0")
        except:
            errors.append("price must be a number")

    if "year" in data:
        try:
            year = int(data["year"])
            if year < 1980 or year > 2030:
                errors.append("year is out of valid range")
        except:
            errors.append("year must be an integer")

    if "mileage" in data:
        try:
            mileage = int(data["mileage"])
            if mileage < 0:
                errors.append("mileage cannot be negative")
        except:
            errors.append("mileage must be an integer")

    if "vin" in data and len(data["vin"]) < 5:
        errors.append("vin is too short")

    return errors