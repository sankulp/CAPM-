import plotly.express as px
import  numpy as np 

# funtion to plot interactive plotly charts 

def interactive_plot(df):
    fig=px.line()
    for i in df.columns[1:]:
        fig.add_scatter(x = df['Date'], y = df[i] ,name = i)# column_name) 

    fig.update_layout(width = 450, margin = dict(l = 20, r= 20, t = 20, b=20),legend = dict(orientation = 'h', yanchor = 'bottom',
                    y = 1.02, xanchor='right', x =1)           ) 
    
    return fig

# funciton ot normalise the prices based on the initial prices 

def normalise(df_2):
    df = df_2.copy()
    for i in df.columns[1:]:
        df[i] = df[i] / df[i][0]
        # we divide to check how many times the prices increased or decreased
    return df  


# funciton to calculate daily returns 

def daily_return(df):
    df_daily_return = df.copy()
    for i in df.columns[1:] :
        for j in range(1,len(df)):
            df_daily_return[i][j] = ((df[i][j] - df[i][j-1]) / df[i][j-1]) * 100 
            # (current price - prev close price )/ prev close price

        df_daily_return[i][0] = 0 # first row to be 0 
    return df_daily_return

# to calculate beta 
def calculate_beta(stocks_daily_return, stock):
    rm = stocks_daily_return['sp500'].mean() * 252
    b,a = np.polyfit(stocks_daily_return['sp500'], stocks_daily_return[stock],1)

    return b,a 

    