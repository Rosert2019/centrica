import pytest
from scripts.centric import search_on_google, get_top_links, get_content_html, write_html_files

top = 5 #maximum of links to retain from google search
query_search = 'how to data engineering' #the search to be done on google

"""
We firstly test that we get results for our search in google. We must get statuts code equal 200
"""
@pytest.fixture
def first_fixture():
    result = search_on_google(query_search)
    return result
	
def test_google_statut_code(first_fixture):
    assert first_fixture.status_code == 200
	
"""
we want to test that we have top links returned
"""	
@pytest.fixture
def second_fixture(first_fixture):
    result = get_top_links(first_fixture, top)
    return result

def test_top_links_returned(second_fixture):
    assert len(second_fixture)== top
	
"""
we will test that we made three downloads from links. These down are to be written as html file
"""	
@pytest.fixture
def third_fixture(second_fixture):
    result = get_content_html(second_fixture)
    return result

def test_all_is_soup(third_fixture):
    assert len(third_fixture)== top
    
 