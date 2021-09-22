import types
import pytest
import logging
import string
import random
from faker import Faker
from functools import partialmethod, partial

logger = logging.getLogger()


class Patcher:
    def prepare_class( self, clazz ):
        @classmethod
        def on_class_patcher( cls, func_name ):
            def patch_by_name( new_func) :
                old_func = getattr( cls(), func_name )
                def patched_func( self, *args, **kwargs ):                    
                    return new_func( self, old_func, *args, **kwargs )
                setattr( cls, func_name, patched_func )
            return patch_by_name

        setattr( clazz, "patch", on_class_patcher )

Patcher().prepare_class( clazz = Faker )

# logger.info(Faker.patch)


def random_lower_string(length: int = 32) -> str:
    return "".join(random.choices(string.ascii_lowercase, k=length));

@Faker.patch("ascii_free_email")
def patch_ascii_email(self, old_func) -> str:
    """
    WARNING: for new tests file Please consider using Faker.ascii_free_email()
    """
    # logger.warning(f"faker instance:{faker}")
    
    # avoid recursive
    return f"{random_lower_string(8)}__{old_func()}"


    


@pytest.fixture(scope="session", autouse=True)
def dumb_fixture(_session_faker: Faker):    
    logger.info(_session_faker)
    # _session_faker.ascii_free_email = types.MethodType(patch_ascii_email, fake)   
    # old_func = getattr(_session_faker, "ascii_free_email")     
    # _session_faker.ascii_free_email = partial(patch_ascii_email, old_func)
    logger.info(_session_faker)
    logger.info(_session_faker.ascii_free_email())
    pass



def test_something(faker):    
    logger.info(faker)
    logger.warning(faker.ascii_free_email())
    pass

