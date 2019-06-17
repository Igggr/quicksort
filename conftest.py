import random
import pytest

@pytest.fixture
def random_list():
    print("generating new list")
    return [ random.randint(-1000, 1000) for i in range(random.randint(500, 1000))]
