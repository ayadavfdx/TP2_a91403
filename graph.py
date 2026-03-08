import yfinance as yf
import plotly.graph_objects as go

def show_graph(symbol: str):
    data = yf.download(symbol)

    figure= go.Figure()

    figure.add_trace(
        go.Scatter(
            x=data.index,
            y=data["Close"],
            mode="lines",
            name=symbol
        )
    )
