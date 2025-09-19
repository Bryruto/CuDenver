import sys
import requests

url = "https://rest.coincap.io/v3/assets/bitcoin?apiKey=726ae563f4078f1e2922ef9c0722cb831a0c6ac14c797613b5148ccc2706086f"

if len(sys.argv) != 2:
    sys.exit("Missing command-line argument")

try:
    bitcoin = float(sys.argv[1])
except ValueError:
    sys.exit("Command-line argument is not a number")

CoinCap = requests.get(url)
try:
    CoinCap.json()
except requests.RequestException:
    sys.exit("Requests Failed")

price = CoinCap.json()['data']['priceUsd']

price = float(price) * float(sys.argv[1])

print(f"${price:,.4f}")


