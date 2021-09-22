import types
import pytest
import logging
import string
import random
from faker import Faker
from functools import partialmethod, partial

logger = logging.getLogger()



def random_lower_string(length: int = 32) -> str:
    return "".join(random.choices(string.ascii_lowercase, k=length));



def patch_ascii_email(faker: Faker) -> str:
    """
    WARNING: for new tests file Please consider using Faker.ascii_free_email()
    """
    logger.warning(f"faker instance:{faker}")
    # avoid recursive
    return f"{random_lower_string(8)}{faker.email()}"


@pytest.fixture(scope="session", autouse=True)
def dumb_fixture(_session_faker: Faker):    
    logger.info(_session_faker)
    # _session_faker.ascii_free_email = types.MethodType(patch_ascii_email, fake)    
    _session_faker.ascii_free_email = partial(patch_ascii_email, fake)
    pass


fake = Faker()
fake.ascii_free_email = types.MethodType(patch_ascii_email, fake)


def test_something(faker):    
    logger.info(faker)
    logger.warning(faker.ascii_free_email())
    pass

