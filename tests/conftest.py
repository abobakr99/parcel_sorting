import configparser
import pytest
import os.path


@pytest.fixture(scope='session')
def read_configs(request):
    config_dict = dict()
    config = configparser.ConfigParser()
    config.read(request.config.inifile)
    for section in config.sections():
        config_dict[section] = dict(config[section])
    return config_dict

@pytest.fixture(scope='session',autouse=True)
def bin_path(read_configs):
    if not os.path.exists(read_configs['bin_under_test']['path']):
        pytest.exit("Failled to locate binary test file")
    else:
        return read_configs['bin_under_test']['path']