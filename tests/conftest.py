import pytest
bin_test = '../bins/parcel_loader_v1'
@pytest.fixture(autouse=True)
def bin_path():
    return bin_test