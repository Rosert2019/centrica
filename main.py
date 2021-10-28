from scripts import centric
import os


if __name__ == "__main__":
   top = 5 #maximum of links to retain from google search
   query_search = 'how to data engineering' #the search to be done on google
   result_from_google = centric.search_on_google(query_search)
   top_five_links = centric.get_top_links(result_from_google, top)
   html_content_links = centric.get_content_html(top_five_links)
   
   #the directory where html files wiil be stored
   if not os.path.exists("html_data"):
      os.mkdir("html_data")
	  
   centric.write_html_files(html_content_links)
   
   #move html files in the html_data directory
   centric.move("html_data")
   