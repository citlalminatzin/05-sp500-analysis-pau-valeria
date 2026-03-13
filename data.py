#!/usr/bin/env python

from yfinance import Ticker
import pandas as pd
import matplotlib.pyplot as plt 

def get_stock_data(ticker:str = "^GSPC", years: int = 5, path:str = "data/sp500.csv"):
    """Gets historic data for a ticker from yfinance API"""
    t = str(years) + "y"
    stock = Ticker(ticker).history(period = t)
    stock.to_csv(path, encoding = 'utf-8')

def read_data(path="data/sp500.csv"):
    """Lee los datos de un csv y te los devuelve"""
    df = pd.read_csv(path)
    df["Date"] = pd.to_datetime(df["Date"]) #me convierte las fechas a formato Date
    return df
def stock_plot(df):
    """Grafica el precio de cierre"""
    df = df.sort_values("Date")

    plt.figure(figsize=(10,5))
    plt.plot(df["Date"], df["Close"])
    plt.title("Precio del S&P 500 (últimos 5 años)")
    plt.xlabel("Fecha")
    plt.ylabel("Precio de cierre")
    plt.grid(True)
    plt.show()

def rends(df):
    """Calcula los rendimientos diarios con pandas"""
    df = df.sort_values("Date")
    df["Return"] = df["Close"].pct_change()
    return df

def rends_plot(df):
    """Grafica de rendimientos diarios"""
    plt.figure(figsize=(10,5))
    plt.plot(df["Date"], df["Return"])
    plt.title("Rendimientos diarios del S&P500")
    plt.xlabel("Fecha")
    plt.ylabel("Rendimiento")
    plt.grid(True)
    plt.show()

def main():
    get_stock_data()
    df = read_data()
    rendimientos = rends(df)
    rends_plot(rendimientos)
    stock_plot(df)

if __name__ == "__main__":
    
    main()
