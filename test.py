import pytest
from faker import Faker


@pytest.fixture(scope="module",autouse=True)
def dumb_fixture(faker: Faker):    
    pass


def test_something(faker):    
    print(faker)
    # expect The faker fixture will return the session-scoped instance    
    pass
