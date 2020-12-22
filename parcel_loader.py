import subprocess
import re
import pytest
import os



def setup_file(points):
    fpath = 'input_file.txt'
    num_points = len(points)
    try: 
        subprocess.check_call ('echo "{}" > {}'.format(num_points, fpath), shell=True)
        for i in range (num_points):
            subprocess.check_call('echo "\n{},{},{}" >> {}'.format(points[i][0], points[i][1], points[i][2], fpath), shell=True)
    except subprocess.CalledProcessError as e:
        pytest.fail("Failled to create test file. Error: {}".format(e))
    return fpath

def call_process(fpath):
        output = subprocess.check_output('./parcel_loader_v1 -f ./'+fpath, stderr=subprocess.STDOUT, shell=True).decode()
        return output

def find_match(regxs,output):
    match = re.findall(regxs, output, re.MULTILINE)  
    if not match:
        pytest.fail('Failed to parse the desire match from output: {}'.format(output))
    return  (match[0])

@pytest.fixture
def setup_test_001():
    points = ((11,20,20),)
    fpath = setup_file(points)
    yield fpath
    os.remove(fpath)

def test_001_load_time(setup_test_001):
    fpath = setup_test_001
    points = open(fpath, "r")
    points = points.read()
    print('Testing points: {}'.format(points))
    output = call_process(fpath)
    regxs = r'^Minimum\stime\s\=\s(\d\d\.\d\d)'
    min_time = float(find_match(regxs,output))
    print ('Actual result = {}\n'
           'Expected result = {}'.format(min_time, 30.00))
    assert min_time == 30.00, 'Minimum time should be 30 for point: {}'.format(points)

@pytest.fixture
def setup_test_002():
    points = ()
    fpath = setup_file(points)
    yield fpath
    os.remove(fpath)

def test_002_load_time(setup_test_002):
    fpath = setup_test_002
    points = open(fpath, "r")
    points = points.read()
    print('Testing points: {}'.format(points))
    output = call_process(fpath)
    regxs = r'^Minimum\stime\s\=\s(\d\d\.\d\d)'
    min_time = float(find_match(regxs,output))
    print ('Actual result = {}\n'
           'Expected result = {}'.format(min_time, 20.00))
    assert min_time == 20.00, 'Minimum time should be 20 for point: {}'.format(points)

@pytest.fixture
def setup_test_003():
    points = ()
    fpath = setup_file(points)
    yield fpath
    os.remove(fpath)    

def test_003_start_point(setup_test_003):
    fpath = setup_test_003
    points = open(fpath, "r")
    points = points.read()
    print('Testing points: {}'.format(points))
    output = call_process(fpath)
    regxs = r'^Starting\sfrom\spoint\:\s\w\=(\d)\,\w\=(\d)'
    start_point = find_match(regxs, output)
    print ('Actual result = {}\n'
           'Expected result = {}'.format(start_point, (0,0)))
    assert start_point == ('0','0'), 'start point should be (0,0)' 

@pytest.fixture
def setup_test_004():
    points = ()
    fpath = setup_file(points)
    yield fpath
    os.remove(fpath) 

def test_004_stop_point(setup_test_004):
    fpath = setup_test_004
    points = open(fpath, "r")
    points = points.read()
    print('Testing points: {}'.format(points))
    output = call_process(fpath)    
    regxs = r'Stopping\sat\spoint\:\s\w\=(\d\d)\,\w\=(\d\d)'
    stop_point = find_match(regxs, output)
    print ('Actual result = {}\n'
           'Expected result = {}'.format(stop_point, (20,20)))
    assert stop_point == ('20','20'), 'Stop point should be at (20,20)'

@pytest.fixture
def setup_test_005():
    points = ((11,20,20),(20,10,10))
    fpath = setup_file(points)
    yield fpath
    os.remove(fpath) 

def test_005_load_time(setup_test_005):
    fpath = setup_test_005
    points = open(fpath, "r")
    points = points.read()
    print('Testing points: {}'.format(points))
    output = call_process(fpath)
    regxs = r'^Minimum\stime\s\=\s(\d\d\.\d\d)'
    min_time = float(find_match(regxs,output))
    print ('Actual result = {}\n'
           'Expected result = {}'.format(min_time, 41.00))
    assert min_time == 41.00, 'Minimum time should be 41 for point: {}'.format(points)

@pytest.fixture
def setup_test_006():
    points = ((60,20,20),(40,10,10))
    fpath = setup_file(points)
    yield fpath
    os.remove(fpath) 


def test_006_load_time(setup_test_006):
    fpath = setup_test_006
    points = open(fpath, "r")
    points = points.read()
    print('Testing points: {}'.format(points))
    output = call_process(fpath)
    regxs = r'^Minimum\stime\s\=\s(\d\d\.\d\d)'
    min_time = float(find_match(regxs,output))
    print ('Actual result = {}\n'
           'Expected result = {}'.format(min_time, 60.00))
    assert min_time == 60.00, 'Minimum time should be 41 for point: {}'.format(points)
    
@pytest.fixture
def setup_test_007():
    points = ((50, 10, 10), (40, 17, 19), (50,20,20))
    fpath = setup_file(points)
    yield fpath
    os.remove(fpath) 


def test_007_load_time(setup_test_007):
    fpath = setup_test_007
    points = open(fpath, "r")
    points = points.read()
    print('Testing points: {}'.format(points))
    output = call_process(fpath)
    regxs = r'^Minimum\stime\s\=\s(\d\d\.\d\d)'
    min_time = float(find_match(regxs,output))
    print ('Actual result = {}\n'
           'Expected result = {}'.format(min_time, 50.00))
    assert min_time == 50.00, 'Minimum time should be 50 for point: {}'.format(points)