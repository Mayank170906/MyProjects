from bs4 import BeautifulSoup
import requests

class data_extractor:
    def give_data():
        url="https://appbrewery.github.io/Zillow-Clone/"
    
        data={'price':[],'adress':[],'link':[]}
    
        response=requests.get(url=url)
        html_response=response.text
    
        soup=BeautifulSoup(html_response,'html.parser')
    
    
        result_count=int(soup.find('span',class_='result-count').text.split()[0])
        print(result_count)
    
        price_span = soup.find_all('span', {'data-test': 'property-card-price'})
        for price in price_span:
            price=price.text.split('+')[0]
            price=price.split('/')[0]
            price=price.split()[0]
            price=price.replace(',','')
            data['price'].append(price)
    
        
        adress_span=soup.find_all('address', {'data-test':'property-card-addr'})
        for adress in adress_span:
            adress=adress.text.strip()
            data['adress'].append(adress)
    
        link_span=soup.find_all('a',class_="property-card-link")
        for link in link_span:
            link=link['href']
            data['link'].append(link)
        
        return data



# /html/body/div/div[2]/div/div/div[1]/div[1]/div/ul/li[1]/div/div/article/div/div[1]/div[2]/div/span

# /html/body/div/div[2]/div/div/div[1]/div[1]/div/ul/li[2]/div/div/article/div/div[1]/div[2]/div/span