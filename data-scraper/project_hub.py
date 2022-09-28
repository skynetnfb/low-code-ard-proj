from asyncore import write
from cgitb import html
from msilib.schema import Component
from matplotlib.pyplot import title
import requests
import bs4
import csv
import time
from utils import *
import code_snippet_scraper
import uuid


def project_links_scraper_cycle (pages=276,file_name='links.txt',project_detail_file='all_project_links_final.txt'):
        with open(file_name,'a') as data:
                data.write('['+'\n')
        with open(project_detail_file,'a') as detail_data:
                detail_data.write('['+'\n')
        for i in range(1,pages+1):
            url="https://create.arduino.cc/projecthub?&page={}&sort=recent".format(str(i))
            project_links_scraper(url = url,file_name=file_name,project_detail_file = project_detail_file)
            print(url)
            with open(file_name,'a') as data:
                data.write(']'+'\n')
        with open(project_detail_file,'a') as detail_data:
                detail_data.write(']'+'\n')

def project_links_scraper(url = "",file_name='',project_detail_file='all_project_detail_final_test.txt'):
    res =  requests.get(url)
    
    try:
        res.raise_for_status()
        html_page = bs4.BeautifulSoup(res.text, 'html.parser')
        elem_html = "div"
        sel_elem = html_page.select(elem_html)
        contents = sel_elem[0]

        project_links = contents.find_all("a", {"class": "project-link-with-ref"}, href=True)
        with open(file_name,'a') as data:
            if project_links:                
                for link in project_links:
                    if(link.get_text()!=""):                      
                        data.write('{'+'\n')
                        data.write('"project_name":'+'"'+str(link.get_text().encode("utf-8"))+'",'+'\n')
                        data.write('"project_link":'+'"'+"https://create.arduino.cc"+str(link['href'])+'"'+'\n')
                        scrape_project_detail_new(url="https://create.arduino.cc"+str(link['href']),file_name=project_detail_file)
                        if(link != project_links[-1]):
                            data.write('},'+'\n')
                        else:
                            data.write('}'+'\n')
            else:
                print(project_links)
       
    except Exception as exc:
        log_str = ''
        msg=''
        print('-------------------Exception raised LINK SCRAPER ', exc.__class__)
        if hasattr(exc, 'message'):
                msg = exc.message
        else:
            msg = exc
        with open('err_log_link.txt','a') as data_loger:
            log_str = str(time.time())+' : '+ str(msg) + "URL: " + url
            data_loger.write(log_str)



def scrape_project_detail_new(url="",file_name=''):
    #print ("SCRAPE PROJECT: "+str(url))
    res =  requests.get(url)
    
    try:
        prj_info = ''
        res.raise_for_status()
        html_page = bs4.BeautifulSoup(res.text, 'html.parser')
        elem_html = "div"
        sel_elem = html_page.select(elem_html)
        contents = sel_elem[0]
        project_title = contents.find_all("h1", {"class": "project-title"})
        #print('"title": '+str(project_title[0].get_text()))
        project_description = contents.find_all("p", {"class": "project-one-liner"})

        #print('"decription": '+str(project_description[0].get_text()))
        #print("\n")

        section_components = contents.find_all("section", {"id": "components"})
        if(section_components):
            parser_components = bs4.BeautifulSoup(str(section_components[0].get_text), 'html.parser')
            components = parser_components.find_all("tr", {"class": "part-name"})
        else:components=[]
        #for c in components:
        #    print(c.get_text()+",")
        #print("\n")
        section_tools = contents.find_all("section", {"id": "tools"})
        if(section_tools):
            parser_tools = bs4.BeautifulSoup(str(section_tools[0].get_text), 'html.parser')
            tools = parser_tools.find_all("tr", {"class": "part-name"})
        else:tools=[]    
        #for t in tools:
        #    print(t.get_text()+",")
        #print("\n")
        section_app = contents.find_all("section", {"id": "apps"})
        if(section_app):
            parser_app = bs4.BeautifulSoup(str(section_app[0].get_text), 'html.parser')
            apps = parser_app.find_all("tr", {"class": "part-name"})
        else:apps=[]

        
        # I dati minati di views respect e comments non corrispondono a quelli ispezionati!!
        # non credo sia risolvibile
        
        #project_views = contents.find_all("li", {"class": "impression-stats"})
        #if(project_views):
        #    print(project_views)
        #    parser_views = bs4.BeautifulSoup(str(project_views[0].get_text), 'html.parser')
        #    views = parser_views.find_all("span", {"class": "stat-figure"})
        #    print ("Views"+str(views))
        #else:views="0"

        #project_comments = contents.find_all("li", {"class": "comment-stats"})
        #if(project_comments):
        #    parser_comments = bs4.BeautifulSoup(str(project_comments[0].get_text()), 'html.parser')
        #    comments = parser_comments.find_all("span", {"class": "stat-figure"})
        #    print ("Comments"+str(comments.get_text()))
        #else:comments="0"

        #project_respect = contents.find_all("li", {"class": "respect-stats"})
        #if(project_respect):
        #    parser_respect = bs4.BeautifulSoup(str(project_respect[0].get_text()), 'html.parser')
        #    print(parser_respect)
        #    respects = parser_respect.find_all("span", {"class": "stat-figure"})
        #    print ("Respect"+str(respects[0].get_text))
        #else:respects="0"

        #for a in apps:
        #    print(a.get_text()+",")
        #print("\n")
        project_id=str(uuid.uuid4())
        code_snippet_scraper.scrape_code_snippet(url=url,project_id=project_id)
        
        with open(file_name,'a') as data:
            prj_info = '{'+'\n' + '"project_link"'+":"+'"'+url+'"'+","+'\n' +'"project_title"'+":"+'"'+clean_string(str(project_title[0].get_text().encode("utf-8")))+'"'+","+'\n'+'"project_description"'+":"+'"'+clean_string(str(project_description[0].get_text().encode("utf-8")))+'"'+","+'\n'
            prj_info = prj_info+ '"project_id"'+":"+'"'+project_id+'"'+","+'\n'
            if components:
                prj_info = prj_info + '"components":' + '' + '['
                for c in components:
                    if(c.get_text()!=""):
                        if(c!=components[len(components)-1]):
                            prj_info = prj_info + '"'+clean_string(c.get_text().replace(",", ""))+'"'+","
                            write_column_name(file_name="components.txt", component_name=clean_string(c.get_text().replace(",", ""))) 
                        else:
                            prj_info = prj_info + '"'+clean_string(c.get_text().replace(",", ""))+'"'
                            write_column_name(file_name="components.txt", component_name=clean_string(c.get_text().replace(",", ""))) 
                            
                prj_info = prj_info + '],'+'\n'
            else:
                prj_info = prj_info + '"tools":'+'[],'
            if tools:
                prj_info = prj_info + '"tools":'+'' + '['
                for t in tools:

                    #a= contents.find_all("a", {"class": "project-one-liner"}, href=True)
                    if(t.get_text()!=""):
                        if(t!=tools[len(tools)-1]):

                            prj_info = prj_info + '"'+clean_string(t.get_text().replace(",", ""))+'"'+","
                            write_column_name(file_name="tools.txt", component_name=clean_string(t.get_text().replace(",", "")))
                        else:
                            prj_info = prj_info + '"'+clean_string(t.get_text().replace(",", ""))+'"'
                            write_column_name(file_name="tools.txt", component_name=clean_string(t.get_text().replace(",", "")))         
                prj_info = prj_info + ']'+'\n'
            else:

                prj_info = prj_info + '"tools":'+'[]'
            #data.write('"category": "null",'+'\n')
            prj_info = prj_info + '}'','+'\n'
            #print(str(prj_info))
            data.write(prj_info)
    except Exception as exc:
        msg=str(time.time())+ url +'\n'
        print('-------------------Exception raised PRJ DETAIL', exc.__class__)
        if hasattr(exc, 'message'):
            msg = exc.message
        else:
            msg = exc
        with open('err_log.txt','a') as data_log:
            log_str = str(time.time())+' : '+ str(msg) + "URL: " + url +'\n'
            data_log.write(log_str)
                

def write_column_name(file_name="components.txt", component_name=""):
    with open(file_name,'a') as data:
        data.write(component_name+',')

def read_columns(file_name = "test.txt"):
    with open (file_name,'r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        for row in csv_reader:
            print (len(row))
            row_set = set(row)
            print(len(row_set))
            for c in row_set:
                print(c)

def clean_string(temp_string):
    if(temp_string == ""):
        return " "
    if(temp_string[1] == '"'):
            
            temp_string = temp_string.split('b"', 1)[1]
    elif(temp_string[1] == "'"):
            
            temp_string = temp_string.split("b'", 1)[1]
                #print(parsed_name)
                #data.write(parsed_name+','+'\n')
    temp_string = temp_string.split("'", 1)[0]
    temp_string = temp_string.replace('"',"''").replace(",","")
    if(temp_string == ""):
        return " "
    return temp_string


#scrape_project_detail(url="https://create.arduino.cc/projecthub/LithiumION/mpu6050-gyroscope-with-arduino-64b931")
#category_scraper(url = "https://create.arduino.cc/projecthub?category=sensors-environment&page=1&sort=trending",pages=31, file_name='project_links.txt')
#project_links_scraper(url = "https://create.arduino.cc/projecthub?&page=259&sort=recent",file_name="all_projects.txt")
#project_links_scraper(url = "https://create.arduino.cc/projecthub?&page=47&sort=recent",file_name="all_projects2.txt")
#project_links_scraper_cycle (pages=276,file_name='all_projects_links.txt',project_detail_file='all_project_detail_final.txt')
scrape_project_detail_new(url="https://create.arduino.cc/projecthub/ericBcreator/stereo-neopixel-ring-vu-meter-b28e78?ref=platform&ref_id=424_trending___&offset=11",file_name="test_project_detail.txt")
#read_columns("components.txt")
#read_columns("tools.txt")
#clean_string ("'b")
