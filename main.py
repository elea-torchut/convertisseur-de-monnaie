from forex_python.converter import CurrencyRates
import json
import os

def convert_currency(amount, from_currency, to_currency):
    c = CurrencyRates()
    
    try:
        exchange_rate = c.get_rate(from_currency, to_currency)
        converted_amount = amount * exchange_rate
        return converted_amount, exchange_rate
    except:
        return None, None

def save_conversion_history(history):
    with open("conversion_history.json", "w") as file:
        json.dump(history, file)

def load_conversion_history():
    if os.path.exists("conversion_history.json"):
        with open("conversion_history.json", "r") as file:
            return json.load(file)
    else:
        return []

def main():
    conversion_history = load_conversion_history()

    amount = float(input("Entrez le montant à convertir : "))
    from_currency = input("Entrez la devise d'origine (par exemple, USD) : ").upper()
    to_currency = input("Entrez la devise de destination (par exemple, EUR) : ").upper()

    converted_amount, exchange_rate = convert_currency(amount, from_currency, to_currency)

    if converted_amount is not None:
        print(f"{amount} {from_currency} équivaut à {converted_amount:.2f} {to_currency} (Taux de change : {exchange_rate:.4f})")
        
        # Enregistrement de l'historique de conversion
        conversion_history.append({
            "from_currency": from_currency,
            "to_currency": to_currency,
            "amount": amount,
            "converted_amount": converted_amount,
            "exchange_rate": exchange_rate
        })
        save_conversion_history(conversion_history)
    else:
        print(f"La conversion de {from_currency} vers {to_currency} n'est pas possible.")

if __name__ == "__main__":
    main()
