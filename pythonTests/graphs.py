import requests
import matplotlib.pyplot as plt

url = "https://api.nbp.pl/api/exchangerates/rates/a/eur/2024-10-01/2024-12-12"
response = requests.get(url) #wysłanie zapytania get do api

if response.status_code == 200: #200 oznacza sukces w zapytaniu
    data = response.json() #zwrócenie danych w formacie JSON
    pass
else:
    print(f"Błąd: {response.status_code}")
    pass

rates = data['rates']
date = [rate['effectiveDate'] for rate in rates]
value = [rate['mid'] for rate in rates]

plt.figure(figsize=(12, 4))
plt.plot(date,value,marker="o",label="Kurs Euro")
plt.title("Kurs Euro")
plt.xlabel("Data")
plt.ylabel("Kurs EUR")
plt.grid(True)
plt.legend()
plt.xticks(rotation=90)  # Obrót etykiet osi X
plt.tight_layout()  # Dopasowanie elementów wykresu
plt.show()
