import requests


def convert_currency(from_currency, to_currency, amount):
    url = f"https://open.er-api.com/v6/latest/{from_currency}"

    try:
        response = requests.get(url)
        response.raise_for_status()

        data = response.json()

        if "rates" not in data:
            print("Error: Could not retrieve exchange rates.")
            return None

        if to_currency not in data["rates"]:
            print(f"Error: Currency '{to_currency}' not found.")
            return None

        rate = data["rates"][to_currency]
        converted_amount = amount * rate

        return converted_amount

    except requests.exceptions.RequestException as e:
        print("Network error:", e)
        return None


def main():
    print("=" * 40)
    print("      Currency Converter")
    print("=" * 40)

    while True:
        from_currency = input("From currency (e.g. USD): ").upper()
        to_currency = input("To currency (e.g. EUR): ").upper()

        try:
            amount = float(input("Amount: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        result = convert_currency(
            from_currency,
            to_currency,
            amount
        )

        if result is not None:
            print("\n--- Result ---")
            print(
                f"{amount:.2f} {from_currency} = "
                f"{result:.2f} {to_currency}"
            )

        again = input(
            "\nDo you want another conversion? (y/n): "
        ).lower()

        if again != "y":
            print("Goodbye!")
            break


if __name__ == "__main__":
    main()