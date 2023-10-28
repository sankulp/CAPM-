import streamlit as st
import pandas as pd
import yfinance as yf
import datetime 
import pandas_datareader.data as web 
import capm_functions 

st.set_page_config(page_title= 'CMAP', page_icon='chart_with_upward_trend', layout='wide')

st.title('Capital Asset Pricing Model' )

# now we need the stock names and time period from the user
col1,col2 = st.columns([1,1])
with col1:
    #stocks_list = st.multiselect('Choose 4 stocks ',('TSLA','AAPL','NFLX','MSFT','MGM','AMZN'),['TSLA','AAPL','MSFT','AMZN'] )# dropdown list
    stocks_list = st.multiselect('Choose 4 stocks ',('AWL','HINDCOPPER','SUBEXLTD','SEQUENT','IEX','IRCTC'),['IEX'] )
with col2:
    year = st.number_input('Number of years',1,10)

# downloading data for SP500 
end = datetime.date.today()
start = datetime.date(datetime.date.today().year-year, datetime.date.today().month, datetime.date.today().day)

SP500 = web.DataReader(['sp500'],'fred',start,end)
#print(SP500.head())

stocks_df = pd.DataFrame()

for stock in stocks_list:
    data = yf.download(stock, period= f'{year}y')
    stocks_df[f'{stock}'] =  data['Close']

    #print(stocks_df.head())

stocks_df.reset_index(inplace=True)
SP500.reset_index(inplace=True)
SP500.columns = ['Date','sp500']
# changing the formatting for merge

stocks_df['Date'] = stocks_df['Date'].astype('datetime64[ns]')
stocks_df['Date'] = stocks_df['Date'].apply(lambda x:str(x)[:10]) # taking nly the date values
stocks_df['Date'] = pd.to_datetime(stocks_df['Date'])
stocks_df = pd.merge(stocks_df,SP500, on='Date', how= 'inner')

#print(stocks_df)

# displaying starting 5 and ending 5 rows 

col1,col2 = st.columns([1,1])
with col1:
    st.markdown('### Dataframe head')
    st.dataframe(stocks_df.head(), use_container_width= True)

with col2:
    st.markdown('### Dataframe tail')
    st.dataframe(stocks_df.tail(),use_container_width=True)

col1,col2 = st.columns([1,1])
with col1:
    st.markdown('### Price of all the stocks ')
    st.plotly_chart(capm_functions.interactive_plot(stocks_df))
with col2:
    #print(capm_functions.normalise(stocks_df))
    st.markdown('### Price of all the stocks (After normalising) ')
    st.plotly_chart(capm_functions.interactive_plot(capm_functions.normalise(stocks_df)))


stocks_daily_return = capm_functions.daily_return(stocks_df)
#print(stocks_daily_return.head())


beta = {}
alpha = {}

for i in stocks_daily_return.columns:
    if i != 'Date' and i != 'SP500' :
        b,a = capm_functions.calculate_beta(stocks_daily_return , i)

        beta[i] = b
        alpha[i] = a 

#print(beta,alpha) 

beta_df = pd.DataFrame(columns= ['Stock', 'Beta Value'])
beta['Stock'] = beta.keys()
beta_df['Beta values'] = str(round(i,2) for i in beta.values()) # (i,2 ) because rounding off till 2 decimal places 

with col1:
    st.markdown('### Calculated Beta value')
    st.dataframe(beta_df, use_container_width= True)

# calculating return 

rf = 0 # risk free asset                                                                     
rm = stocks_daily_return['sp500'].mean()* 252  # market portfolio return 

return_df = pd.DataFrame()
return_value = [] # for storing calculated return value 

#print('beta keys are :',beta.values())
#print(beta.values())

#for x,y in beta.items():
#print(x,'\t', y)
for value in beta.values():
    print((value))
    return_value.append(str(round(rf + (int(value) * (rm-rf)),2)))

# return_df['Stock']  = stocks_list # new column for the stock list
# return_df['Return value'] = return_value # new column for the list 

# with col2:
#     st.markdown('### Calculated return with CAPM')

#     st.dataframe(return_df, use_container_width= True )