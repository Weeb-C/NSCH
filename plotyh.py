import pandas as pd 
import yfinance as yf
import plotly.graph_objects as go
df = pd.read_csv(r"C:\Users\spurw\Downloads\Bitstamp_AAVEBTC_d.csv")
df = df.iloc[::-1]
df['date'] = pd.to_datetime(df['date'])
df['20wma'] = df['close'].rolling(window=140).mean()
fig = go.Figure(data = [go.Candlestick(x= df['date'],
                                             open=df['open'],high=df['high'],
                                             low=df['low'], close=df['close'])])
fig.add_trace(
    go.Scatter(
        x=df['date'],
        y=df['20wma'],
        line=dict(color = "#FFFFFF"),
        name="20 Week MA"
    )
)
fig.update_layout(xaxis_rangeslider_visible=False, template="plotly_dark")
fig.update_layout(yaxis_title="Bitcoin Price USD")
fig.update_layout(xaxis_title="Data")

fig.update_yaxes(type="log")
fig.show()