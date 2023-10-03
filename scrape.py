import requests 
import pandas as pd
from bs4 import BeautifulSoup 
url="https://www.moneycontrol.com/india/stockpricequote/diversified/itc/ITC"
page=requests.get(url)
print(page)
df=pd.read_csv("./stocks1.csv")
print(df)
soup=BeautifulSoup(page.content,'html.parser')
price = soup.find('div', class_ ='inprice1 nsecp').text
print(price)
df1=pd.DataFrame()
df1['companies']=df['companies']
df1['prices']=''
print(df1)
for i, company_url in enumerate(df['url']):
    page = requests.get(company_url)
    soup = BeautifulSoup(page.content, 'html.parser')
    price = soup.find('div', class_='inprice1 nsecp').text
    df1.at[i, 'prices'] = price  # Add the price to the corresponding row
print(df1)
