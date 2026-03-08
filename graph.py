import yfinance as yf
import plotly.graph_objects as go

def show_graph(symbol: str):
    data = yf.download(symbol)

    figure= go.Figure()

    #Graph
    figure.add_trace(
        go.Scatter(
            x=data.index,
            y=data["Close"],
            mode="lines",
            name=symbol
        )
    )

    #Style
    figure.update_layout(
        title= f"{symbol} Stock Price",
        xaxis_title= "Date",
        yaxis_title= "Price",
        template= "plotly_dark"
    )

    figure.show()