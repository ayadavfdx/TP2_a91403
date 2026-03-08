import yfinance as yf
import plotly.graph_objects as go

def show_graph(symbol: str):
    ticker= yf.Ticker(symbol) 
    data = ticker.history(period="3mo")

    figure= go.Figure()

    #Graph
    figure.add_trace(
        go.Scatter(
            x=data.index,
            y=data["Close"],
            mode="lines",
            name=symbol,
            line=dict(color="green",width=4)
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