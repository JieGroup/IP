import pytest

from app.dp.update_topics.update_method.api import (
    GetStaticUpdate,
    GetUniformUpdate
)

@pytest.fixture
def StaticUpdate():    
    return GetStaticUpdate.get_class()

@pytest.fixture
def UniformUpdate():    
    return GetUniformUpdate.get_class()