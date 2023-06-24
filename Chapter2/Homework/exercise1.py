name = 'Amazon'
stock_code = '007623'
stock_price = 19.99
stock_price_daily_growth_factor = 1.2
growth_days = 7
total =  stock_price * (stock_price_daily_growth_factor ** growth_days)

print("Entreprise: %s code de stock %s  cour actuel de l'action %s facteur de quotidient : %s après %d jours de "
"croissance,le prix de l'action a atteint %.2f " % (name,stock_code,stock_price,stock_price_daily_growth_factor,growth_days,total ))
