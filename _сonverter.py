def get_day_word(days):
    if 11 <= days % 100 <= 14:
        return "днів"
    last_digit = days % 10
    if last_digit == 1:
        return "день"
    elif 2 <= last_digit <= 4:
        return "дні"
    else:
        return "днів"


def convert_seconds(seconds):

    days, remainder = divmod(seconds, 86400)
    hours, remainder = divmod(remainder, 3600)
    minutes, seconds = divmod(remainder, 60)

    time_str = f"{str(hours).zfill(2)}:{str(minutes).zfill(2)}:{str(seconds).zfill(2)}"

    day_word = get_day_word(days)

    return f"{days} {day_word}, {time_str}"


while True:
    try:
        user_input = int(input("Enter the number of seconds (0–8640000): "))
        if 0 <= user_input < 8640000:
            print(convert_seconds(user_input))
            break
        else:
            print("The number must be between 0 and 8640000. Please try again.")
    except ValueError:
        print("Enter only a whole number!")
