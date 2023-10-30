# CAPM-
In this project we create a web application using streamlit to perform CAPM calculation for different stocks. We use Yahoo finance to gather data related to different stocks. 
There are two fiels, CAPM.py consists of the main code for fetching the data for the selected stocks, creating the web application using streamlit, calculating CAPM values for different stocks.  

capm_functions consists of some functions that we use to calculate some coefficients like Beta, normlaising the data and plotting it. 

CAPM or capital asset pricing model is basically used to calculate expected returns given the cost of capital and risk of assets. 

CAPM indicates that the expected return on a security is equal to the risk free return plus a risk premium.

ri = rf + Bi(rm - rf)

ri = Expected return on a security ( we'll be calculating this)
rf = Risk free rate of return 
Bi = Beta between the stock and the market 
rm = Expected return of the market 


