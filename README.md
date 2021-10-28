# centrica-test
1. To run the project, type: 

       python main.py 
       
       and a directory html_data will be created in which you will find the scrapped links.


2. The functions used in main.py are stored in scripts directory. 

3. The directory tests contains automated tests written in pytest, type: 

      pytest -v 
      
      to run all the tests. Fixtures were used to avoid to reuse codes.

4.You will need the following packages if you want to run in local: requests, bs4, requests_html, shutil and pytest.


5. You have the possiblities to change the global variables as number of top links considered or the keywords on the main.py file.
