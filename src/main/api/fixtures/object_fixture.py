from typing import Any, List

import pytest


@pytest.fixture
def created_obj():
    objects: List[Any] = []
    yield objects
    clean_user(objects)


def clean_user(objects: List[Any]):...