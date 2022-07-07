from asyncore import write
from cgitb import html
from msilib.schema import Component
import requests
import bs4

def category_scraper(url = "",pages=31):
    res =  requests.get(url)
    
    try:
        res.raise_for_status()
        html_page = bs4.BeautifulSoup(res.text, 'html.parser')
        elem_html = "div"
        sel_elem = html_page.select(elem_html)
        contents = sel_elem[0]
        with open('project_links.txt','a') as data:
            data.write('['+'\n')
        for i in range(1,pages+1):
            url="https://create.arduino.cc/projecthub?category=sensors-environment&page={}&sort=trending".format(str(i))
            #print(url)    
            #print(contents)

                #print(contents)

            project_links = contents.find_all("a", {"class": "project-link-with-ref"}, href=True)
            with open('project_links.txt','a') as data:
                if project_links:
                    print(len(project_links))
                    
                    for link in project_links:
                        if(link.get_text()!=""):
                            data.write('{'+'\n')
                            data.write('"project_name":'+'"'+str(link.get_text(strip=True).replace("\n",""))+'",'+'\n')
                            data.write('"project_link":'+'"'+"https://create.arduino.cc"+str(link['href'])+'"'+'\n')
                            if(i<=31 and link != project_links[-1]):
                                data.write('},'+'\n')
                            else:
                                data.write('}'+'\n')
                        #scrape_project_detail(url="https://create.arduino.cc"+str(link['href']))
                else:
                    print(project_links)
                #data.write('"category": "null",'+'\n')
        with open('project_links.txt','a') as data:
            data.write(']'+'\n')        
    except Exception as exc:
        print('-------------------Exception raised')



def scrape_project_detail(url=""):
    print ("SCRAPE PROJECT: "+str(url))
    res =  requests.get(url)
    
    try:
        res.raise_for_status()
        html_page = bs4.BeautifulSoup(res.text, 'html.parser')
        elem_html = "div"
        sel_elem = html_page.select(elem_html)
        contents = sel_elem[0]
        project_title = contents.find_all("h1", {"class": "project-title"})
        print('"title": '+str(project_title[0].get_text()))
        project_description = contents.find_all("p", {"class": "project-one-liner"})
        print('"decription": '+str(project_description[0].get_text()))
        print("\n")

        section_components = contents.find_all("section", {"id": "components"})
        parser_components = bs4.BeautifulSoup(str(section_components[0].get_text), 'html.parser')
        components = parser_components.find_all("tr", {"class": "part-name"})
        for c in components:
            print(c.get_text()+",")
        print("\n")

        section_tools = contents.find_all("section", {"id": "tools"})
        parser_tools = bs4.BeautifulSoup(str(section_tools[0].get_text), 'html.parser')
        tools = parser_tools.find_all("tr", {"class": "part-name"})
        for t in tools:
            print(t.get_text()+",")
        print("\n")



        section_app = contents.find_all("section", {"id": "apps"})
        parser_app = bs4.BeautifulSoup(str(section_app[0].get_text), 'html.parser')
        apps = parser_app.find_all("tr", {"class": "part-name"})
        for a in apps:
            print(a.get_text()+",")
        print("\n")
        

        with open('projects.txt','a') as data:
            if components:
                print(len(components))
                for link in components:
                    a= contents.find_all("a", {"class": "project-one-liner"}, href=True)
                    if(link.get_text()!=""):
                        data.write('{'+'\n')
                        #data.write('"project_name":'+'"'+str(link.get_text(strip=True).replace("\n",""))+'",'+'\n')
                        #data.write('"project_link":'+'"'+"https://create.arduino.cc"+str(link['href'])+'"'+'\n')
            else:
                print(components)
            #data.write('"category": "null",'+'\n')
      
    except Exception as exc:
        print('-------------------Exception raised')





#scrape_project_detail(url="https://create.arduino.cc/projecthub/LithiumION/mpu6050-gyroscope-with-arduino-64b931")
category_scraper(url = "https://create.arduino.cc/projecthub?category=sensors-environment&page=1&sort=trending")