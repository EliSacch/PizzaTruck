def validate_action(value, choices):
    """
    Inside the try, converts all string values into integers.
    Raises ValueError if strings cannot be converted into int,
    or if it is outside of the range of choices.
    """
    try:
        if value.isnumeric() is False:
            raise ValueError('Please, enter a whole number')
        action = int(value)-1
        is_valid_choice = action >= 0 and action < len(choices)
        if is_valid_choice is False:
            raise IndexError("No option corresponding to this number")
    except (ValueError, IndexError) as e:
        print(f"\nInvalid data: {e}. Please try again.")
        return False

    return True
