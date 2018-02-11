import pytest

@pytest.fixture
def chrome_options(chrome_options):
    chrome_options.set_headless()
    return chrome_options

@pytest.fixture
def firefox_options(firefox_options):
    firefox_options.add_argument('-headless')
    return firefox_options

def test_example(selenium):
    selenium.get('http://www.example.com')

