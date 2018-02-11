import pytest

@pytest.fixture
def chrome_options(chrome_options):
    chrome_options.set_headless()
    return chrome_options

def test_example(selenium):
    selenium.get('http://www.example.com')

