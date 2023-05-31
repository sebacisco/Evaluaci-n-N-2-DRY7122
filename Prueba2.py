import requests
import json
ciudad_origen = input("Ingrese la ciudad de origen: ")
ciudad_destino = input("Ingrese la ciudad de destino: ")
url = f"https://www.mapquestapi.com/directions/v2/route?key=FX7ovwFThdMnD2jLURQM43dLRGGSmVp5&from={ciudad_origen}&to={ciudad_destino}"
response = requests.get(url)
data = json.loads(response.text)
distancia = data["route"]["distance"]
duracion = data["route"]["formattedTime"]
rendimiento = float(input("Ingrese el rendimiento del vehículo (litros por kilómetro): "))
combustible = distancia * rendimiento
print(f"\nNarrativa del viaje:\nDe {ciudad_origen} a {ciudad_destino}\n")

print(f"Distancia: {distancia:.2f} km")
print(f"Duración: {duracion}")
print(f"Combustible requerido: {combustible:.2f} litros")
opcion = input("\nPresione 'q' para salir: ")
if opcion.lower() == "q":
    exit()
