from src.crud_api.models import Project

def test_time_cant_be_negative():
    Project(name="test", time=-1)