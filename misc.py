def get_help(given_list):
    print(" Help: \n -----------------------")
    
    for i in range(len(given_list)):
        output2 = []

        for j in range(len(given_list[i])):
            output = f"{given_list[i][j]}"
            output2.append(output)

        print(f" {': '.join(output2)}")

    print(" -----------------------")

def get_input(string: str, valid_options: list) -> str:
    while True:
        user_input = input(string)
        hmm = user_input[0].upper() + user_input[1:len(user_input)]

        if user_input in valid_options or hmm in valid_options:
            return hmm

        print(f" -Please select from: {' or '.join(valid_options)}-")
