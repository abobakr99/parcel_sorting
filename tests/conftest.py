import configparser
import pytest

@pytest.fixture(scope='session')
def read_configs(request):
    config_dict = dict()
    config = configparser.ConfigParser()
    config.read(request.config.inifile)
    for section in config.sections():
        config_dict[section] = dict(config[section])
    return config_dict

@pytest.fixture(autouse=True)
def bin_path(read_configs):
    return read_configs['bin_under_test']['path']
