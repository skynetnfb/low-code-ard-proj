from asyncore import write
from cgitb import html
import requests
import bs4


def detail_scraper(address,name,element):
    url = address+name
    res =  requests.get(url)
    try:
        
        res.raise_for_status()
        html_page = bs4.BeautifulSoup(res.text, 'html.parser')
        elem_html = element
        sel_elem = html_page.select(elem_html)
        contents = sel_elem[0]

        with open('library_test.txt','a') as data:
            data.write('{'+'\n')
            data.write('"name":'+name+','+'\n')
            #print(contents)

            category = contents.find_all("p", {"class": "categories"})
            if category:
                data.write('"category":'+str(category[0].get_text(strip=True).replace("\n",""))+','+'\n')
            else:
                data.write('"category": "null",'+'\n')
            
            description = contents.find_all("p", {"class": "description"})
            if description:
                data.write('"description":'+str(description[0].get_text(strip=True).encode("utf-8"))+','+'\n')
            else:
                data.write('"description":"null",'+'\n')
            author = contents.find_all("p", {"class": "author"})
            if author:
                data.write('"author":'+str(author[0].get_text(strip=True).replace("\n","").encode("utf-8"))+','+'\n')
            else:
                data.write('"author":"null",'+'\n')
            maintainer = contents.find_all("p", {"class": "maintainer"})
            if maintainer:
                data.write('"maintainer":'+str(maintainer[0].get_text(strip=True).replace("\n","").encode("utf-8"))+','+'\n')
            else:
                data.write('"maintainer": "null",'+'\n')
            compatibility = contents.find_all("p", {"class": "compatibility"})
            if compatibility:
                data.write('"compatibility":'+str(compatibility[0].get_text(strip=True).replace("\n",""))+','+'\n')
            else:
                data.write('"compatibility":"null",'+'\n')
            
            ul = contents.find_all("ul")
            ul= ul[0:2]
            for u in ul:

                if not u.get_text(strip=True)[0].isdigit() and u.get_text(strip=True)[0]!="":
                    compatible_boards_list='['

                    for li in u:
                        if li.get_text(strip=True)!='':
                            #print(li.get_text(strip=True)[0].isdigit())
                            compatible_boards_list = compatible_boards_list + '"'+str(li.get_text(strip=True))+'",'
                    #print(compatible_boards_list)

                    compatible_boards_list= compatible_boards_list[:-1]
                    data.write('"boards":'+compatible_boards_list+']\n') 
                #else:
                #    data.write('"boards":[],'+'\n')
                if u.get_text(strip=True)[0].isdigit() and u.get_text(strip=True)[0]!="":
                    release_list='['
                    for li in u:
                        if li.get_text(strip=True)!='':
                            release_list = release_list + '"'+str(li.get_text(strip=True))+'",'
                    release_list = release_list[:-1]
                    #print(release_list)
                    release_list= release_list + ']'
                    data.write('"relaeases":'+release_list+'\n') 
                #else:
                #    data.write('"releases":[]'+'\n')
            data.write('}'+'\n')

    except Exception as exc:
        print('Exception raised'+str(name))
        print ('------------------------------------'+url)



def category_scraper(url = 'https://www.arduino.cc/reference/en/libraries/category/communication/'):
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
    with open('library_test.txt','a') as data1:
        data1.write('['+'\n')
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
                with open('library_test.txt','a') as data1:
                    detail_scraper(address='https://www.arduino.cc/reference/en/libraries/',name=parsed_name.replace(' ','-').lower(),element='div.single-page')
                    data1.write(','+'\n')
    with open('library_test.txt','a') as data1:
                data1.write(']'+'\n')
    print('file data updated')

category_scraper ( url='https://www.arduino.cc/reference/en/libraries/category/communication/')