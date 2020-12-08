import subprocess
import re
import pytest
import os


fpath = 'input_file.txt'

def setup_file(points):
    num_points = len(points)
    try: 
        subprocess.check_call ('echo "{}" > {}'.format(num_points, fpath), shell=True)
        for i in range (num_points):
            subprocess.check_call('echo "\n{},{},{}" >> {}'.format(points[i][0], points[i][1], points[i][2], fpath), shell=True)
    except subprocess.CalledProcessError as e:
        pytest.fail("Failled to create test file. Error: {}".format(e))

def find_match(regxs):
    output = subprocess.check_output('./parcel_loader_v1 -f ./'+fpath, stderr=subprocess.STDOUT, shell=True).decode()
    match = re.findall(regxs, output, re.MULTILINE)  
    if not match:
        pytest.fail('Failed to parse the desire match from output: {}'.format(output))
    return  (match[0])


@pytest.fixture
def setup_test_001():
    points = ((11,20,20),)
    setup_file(points)
    yield points
    os.remove(fpath)

@pytest.fixture
def setup_test_003():
    points = ()
    setup_file(points)
    yield points
    os.remove(fpath)

@pytest.fixture
def setup_test_004():
    points = ()
    setup_file(points)
    yield points
    os.remove(fpath)

@pytest.fixture
def setup_test_005():
    points = ((11,20,20),(20,10,10))
    setup_file(points)
    yield points
    os.remove(fpath)

@pytest.fixture
def setup_test_006():
    points = ((60,20,20),(40,10,10))
    setup_file(points)
    yield points
    os.remove(fpath)

@pytest.fixture
def setup_test_007():
    points = ((50, 10, 10), (40, 17, 19), (50,20,20))
    setup_file(points)
    yield points
    os.remove(fpath)
    
def test_001_load_time(setup_test_001):
    points = setup_test_001
    print('Testing points: {}'.format(points))
    regxs = r'^Minimum\stime\s\=\s(\d\d\.\d\d)'
    min_time = float(find_match(regxs))
    print ('Actual result = {}\n'
           'Expected result = {}'.format(min_time, 30.00))
    assert min_time == 30.00, 'Minimum time should be 30 for point: {}'.format(points)
     
def test_003_load_time(setup_test_003):
    regxs = r'^Starting\sfrom\spoint\:\s\w\=(\d)\,\w\=(\d)'
    start_point = find_match(regxs)
    print ('Actual result = {}\n'
           'Expected result = {}'.format(start_point, (0,0)))
    assert start_point == ('0','0'), 'start point should be (0,0)' 
    
def test_004_load_time(setup_test_004):
    regxs = r'Stopping\sat\spoint\:\s\w\=(\d\d)\,\w\=(\d\d)'
    stop_point = find_match(regxs)
    print ('Actual result = {}\n'
           'Expected result = {}'.format(stop_point, (20,20)))
    assert stop_point == ('20','20'), 'Stop point should be at (20,20)'
    
def test_005_load_time(setup_test_005):
    points = setup_test_005
    regxs = r'^Minimum\stime\s\=\s(\d\d\.\d\d)'
    min_time = float(find_match(regxs))
    print ('Actual result = {}\n'
           'Expected result = {}'.format(min_time, 41.00))
    assert min_time == 41.00, 'Minimum time should be 41 for point: {}'.format(points)
    
def test_006_load_time(setup_test_006):
    points = setup_test_006
    regxs = r'^Minimum\stime\s\=\s(\d\d\.\d\d)'
    min_time = float(find_match(regxs))
    print ('Actual result = {}\n'
           'Expected result = {}'.format(min_time, 60.00))
    assert min_time == 60.00, 'Minimum time should be 41 for point: {}'.format(points)
    
def test_007_load_time(setup_test_007):
    points = setup_test_007
    regxs = r'^Minimum\stime\s\=\s(\d\d\.\d\d)'
    min_time = float(find_match(regxs))
    print ('Actual result = {}\n'
           'Expected result = {}'.format(min_time, 50.00))
    assert min_time == 50.00, 'Minimum time should be 50 for point: {}'.format(points)
    