import types
import pytest
import logging
from faker import Faker

logger = logging.getLogger()



def patch_ascii_email(faker: Faker) -> str:
    """
    WARNING: for new tests file Please consider using Faker.ascii_free_email()
    """
    logger.warning(f"faker instance:{faker}")
    # avoid recursive
    return f"11111111112@gmail.com{faker.email()}"


@pytest.fixture(scope="session",autouse=True)
def dumb_fixture(_session_faker: Faker):    
    logger.info(_session_faker)
    _session_faker.ascii_free_email = types.MethodType(patch_ascii_email, fake)
    pass


fake = Faker()
fake.ascii_free_email = types.MethodType(patch_ascii_email, fake)


def test_something(faker):    
    logger.info(faker)
    logger.warning(faker.ascii_free_email())
    pass

