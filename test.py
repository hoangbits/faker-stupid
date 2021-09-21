import pytest
import logging
from faker import Faker

logger = logging.getLogger()


@pytest.fixture(scope="function",autouse=True)
def dumb_fixture(faker: Faker):    
    logger.critical(faker)
    pass


@pytest.fixture(scope="session",autouse=True)
def dumb_fixture1(faker: Faker):    
    logger.critical(faker)
    pass


def test_something(faker):    
    logger.critical(faker)
    # expect The faker fixture will return the session-scoped instance    
    pass


def test_somethingelse(faker):    
    logger.info(faker)
    # expect The faker fixture will return the session-scoped instance    
    pass
