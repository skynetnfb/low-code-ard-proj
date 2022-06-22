from asyncore import write
from cgitb import html
import requests
import bs4

def detail_scraper(address,name,element,childs):
    url = address+name
    res =  requests.get(url)
    try:
        res.raise_for_status()
        html_page = bs4.BeautifulSoup(res.text, 'html.parser')

        elem_html = element
        sel_elem = html_page.select(elem_html)

        text_elem = sel_elem[0].getText()
        container = html_page.find_all(childs)

        with open('libraries.txt','a') as data:
            data.write('*********************************'+name+'*********************************'+'\n')
            for li in html_page.find_all("li"):

                parsed_name = str(li.get_text(strip=True).encode("utf-8")).split(":", 1)[0]
                
                if(parsed_name[1] == '"'):
                    parsed_name = parsed_name.split('b"', 1)[1]

                else:
                    parsed_name = parsed_name.split("b'", 1)[1]

                parsed_name = parsed_name.split("'", 1)[0]
                
                if(str(parsed_name) != 'Languagefunctionsvariablesstructure' 
                and str(parsed_name) != 'functions'  
                and str(parsed_name) != 'variables' 
                and str(parsed_name) != 'structure'
                and str(parsed_name) != 'Libraries'
                and str(parsed_name) != 'IoT Cloud API'
                and str(parsed_name) != 'Glossary'):
                    data.write(parsed_name+','+'\n')
    except Exception as exc:
        print('Exception raised')
        print ('------------------------------------'+url)
        pass




url = 'https://www.arduino.cc/reference/en/libraries/category/communication/'
res =  requests.get(url)
try:
    res.raise_for_status()
except Exception as exc:
    print('Exception raised')

html_page = bs4.BeautifulSoup(res.text, 'html.parser')

elem_html = 'div.single-page'
sel_elem = html_page.select(elem_html)

text_elem = sel_elem[0].getText()
container = html_page.find_all("li")
print(len(container))

with open('data.txt','w') as data:
    for li in html_page.find_all("li"):
        #print(li.get_text(strip=True).encode("utf-8"))
        parsed_name = str(li.get_text(strip=True).encode("utf-8")).split(":", 1)[0]
        
        if(parsed_name[1] == '"'):
            parsed_name = parsed_name.split('b"', 1)[1]
            #print(parsed_name)
            #data.write(parsed_name+','+'\n')
        else:
            parsed_name = parsed_name.split("b'", 1)[1]
            #print(parsed_name)
            #data.write(parsed_name+','+'\n')
        parsed_name = parsed_name.split("'", 1)[0]
        
        if(str(parsed_name) != 'Languagefunctionsvariablesstructure' 
        and str(parsed_name) != 'functions'  
        and str(parsed_name) != 'variables' 
        and str(parsed_name) != 'structure'
        and str(parsed_name) != 'Libraries'
        and str(parsed_name) != 'IoT Cloud API'
        and str(parsed_name) != 'Glossary'):
            data.write(parsed_name+','+'\n')
            detail_scraper(address='https://www.arduino.cc/reference/en/libraries/',name=parsed_name.replace(' ','-').lower(),element='div.single-page',childs='li')


print('file data updated')