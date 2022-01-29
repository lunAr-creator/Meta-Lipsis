def get_input(string: str, valid_options: list) -> str:
    """
    Deals with error checking for inputs
    """
    while True:
        user_input = input(string)
        if user_input in valid_options:
            return user_input
        print(f"^^^ Please select from: {' or '.join(valid_options)} ^^^ ")