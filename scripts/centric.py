# -*- coding: utf-8 -*-
"""
Created on Wed Oct 27 12:03:49 2021

@author: Djonga
"""


import requests 
import bs4
import os 
from requests_html import HTML, HTMLSession
from shutil import copy 


#----------------------Global variables----------------------------------

#this variable will help us to make a search on google
global_query = 'https://google.com/search?q='


def search_on_google(query):
    query = global_query + query
    session = HTMLSession()
    response = session.get(query)
    return response
	
	
def get_top_links(http_reponse, top):
    links = http_reponse.html.absolute_links
    links = list(links) 
    top_list = []
    #we exclude the link with word search in it because it return to google search
    for link in links:
        if ('search' in link) == False:
            top_list.append(link)
         
            if len(top_list) == top:
                break
    return top_list

def get_content_html(top_list_links):
    list_html = []
    for link in top_list_links:
        try:
            res = requests.get(link)
            list_html.append(bs4.BeautifulSoup(res.text,"html.parser"))
        except:
            continue
    return list_html	
	
def write_html_files(list_links):
    for link in list_links:  
        #arbitrary name of expected html file
        name_file = str(list_links.index(link))+ "_" + "file.html"		
        # Write HTML String as file.html
        with open(name_file, "wb") as file:
            file.write(link.encode('utf-8'))

def move(folder):
    docs = os.listdir() 
    for doc in docs:
        if '_file' in doc:
            copy(doc, folder)
            os.remove(doc)
      
			
			
	