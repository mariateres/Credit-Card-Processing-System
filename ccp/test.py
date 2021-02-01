import pytest

@pytest.fixture
def name():
    return 'Don'
    
@pytest.fixture
def name_invalid_card():
    return 'Dan'
    
@pytest.fixture
def limit():
    return 2000

@pytest.fixture
def valid_card():
    return '4111111111111111'

@pytest.fixture
def invalid_card():
    return '4111111111111112'
