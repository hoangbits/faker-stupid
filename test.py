import pytest
import logging
from faker import Faker

logger = logging.getLogger()


@pytest.fixture(scope="module",autouse=True)
def dumb_fixture(faker: Faker):    
    logger.info(faker)
    pass



def test_something(faker):    
    logger.info(faker)
    # expect The faker fixture will return the session-scoped instance    
    pass


def test_somethingelse(faker):    
    logger.info(faker)
    # expect The faker fixture will return the session-scoped instance    
    pass
