import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd

def digitSymbol():
    print("-----------------------------------------------------------")
    symbol = input("Ingresa el símbolo de la acción (NVDA, VOO, PLTR): ").upper()
    print("-----------------------------------------------------------")
    return symbol

def chargeStocks(symbol):
    stock = yf.Ticker(symbol)
    hist = stock.history(period="12mo")  # Últimos 12 meses

    if hist.empty:
        print(f"No se encontraron datos para el símbolo: {symbol}")
    else:
        # Graficar los precios de cierre

        df = pd.DataFrame(hist)

        # Save the dataframe to a CSV file
        df.to_csv('Stocks'+"_"+symbol+".csv", index=False)
        plt.figure(figsize=(10, 6))
        plt.plot(hist.index, hist['Close'], label='Precio de Cierre', color='blue')
        plt.title(f'Precios de {symbol} - Últimos 12 Meses')
        plt.xlabel('Fecha')
        plt.ylabel('Precio (USD)')
        plt.grid(True)
        plt.legend()
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

chargeStocks(digitSymbol())