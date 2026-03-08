import yfinance as yf
import plotly.graph_objects as go

def show_graph(symbol: str):
    data = yf.download(symbol)

    
