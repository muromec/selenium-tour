import pytest

@pytest.fixture
def chrome_options(chrome_options):
    chrome_options.binary_location = '/usr/lib/chromium-browser/chromedriver'
    chrome_options.add_argument('--headless')
    return chrome_options

def test_example(selenium):
    selenium.get('http://www.example.com')

