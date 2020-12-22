import os
import subprocess
import re
import pytest 


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

def invalid_points_file_setup(points):
    if not isinstance(points,str):
       points = str(points)

    with open(fpath, 'w') as file:
        file.write(points)

def call_process(fpath):
    out = subprocess.check_output('../bins/parcel_loader_v1 -f ./'+fpath, stderr=subprocess.STDOUT, shell=True).decode()
    return out

def find_match(regex,out):
    match = re.findall(regex,out, re.MULTILINE)  
    print('Out: \n {} Type: \n {} Match: {}'.format(out,type(out),type(match)))
    if not match:
        pytest.fail('Failed to parse minimum time value from output: {}'.format(out))
    return match[0]
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
@pytest.fixture
def setup_test_008():
    points = ((12,10,10),)
    fpath = setup_file(points)
    yield fpath
    os.remove(fpath)

def test_008_load_time(setup_test_008):
    fpath = setup_test_008
    regex = r'^Minimum time = (\d+\.\d\d)'
    print('Testing points: {}'.format(points))
    out = call_process(fpath)
    match = find_match(regex,out)
    min_time = float (match)
    print ('Actual result = {}\n''Expected result <={}'.format(min_time, 30.00))
    assert min_time <= 30.00, 'Minimum time should be 30 or less for point: {}'.format(points)

@pytest.fixture(params = [((1,10,10),) , ((12,10,10),) ])
def setup_test_009(request):
    points = request.param
    fpath = setup_file(points)
    yield fpath
    os.remove(fpath)

def test_009_load_time_format(setup_test_009):
    fpath = setup_test_009
    regex = r'^Minimum time = \d+\.\d\d'
    min_time =0
    if points == ((1,10,10),):
        min_time = '21.00'
    elif points == ((12,10,10),): 
        min_time = '30.00'

    out = call_process(fpath)
    min_time_string = find_match(regex,out)

    print ('Actual pointsresult = {}\n''Expected result = {}'.format(min_time_string, 'Minimum time = '+ min_time))
    
    assert min_time_string == 'Minimum time = '+ min_time, 'Minimum time should look like [Minimum time = 21.00] for point: {}'.format(points)

@pytest.fixture
def setup_test_010():
    points = ((1,10,10),)
    fpath = setup_file(points)
    yield fpath
    os.remove(fpath)

def test_010_load_time_fromat(setup_test_010):
    fpath = setup_test_010
    regex = r'^Starting from point: x=\d,y=\d'
    out = call_process(fpath)
    min_time_format = find_match(regex,out)
    print ('Actual result = {}\n''Expected result = {}'.format(min_time_format, 'Minimum time = 21.00'))
    assert min_time_format == 'Starting from point: x=0,y=0' , 'Minimum time should look like [Starting from point: x=0,y=0] for point: {}'.format(points)

@pytest.fixture
def setup_test_011():
    points = ((1,10,10),)
    fpath = setup_file(points)
    yield fpath
    os.remove(fpath)

def test_011_load_time_format(setup_test_011):
    fpath = setup_test_011
    regex = r'^Stopping at point: x=\d\d,y=\d\d'
    out = call_process(fpath)
    min_time_format = find_match(regex,out)
    print ('Actual result = {}\n''Expected result = {}'.format(min_time_format, 'Minimum time = 21.00'))
    assert min_time_format == 'Stopping at point: x=20,y=20' , 'Minimum time should look like [Stopping at point: x=20,y=20] for point: {}'.format(points)

@pytest.fixture(params = [ 15 , (12,10,), 'test' ])
def setup_test_012(request):
    points = request.param
    invalid_points_file_setup(points)
    yield points
    os.remove(fpath)

def test_012_invalid_points(setup_test_012):
    points = setup_test_012
    regex = r'^Minimum time = (\d+\.\d\d)'
    print('Testing points: {}'.format(points))
    out = call_process()
    match = find_match(regex,out)
    min_time = float (match)
    print ('Actual result = {}\n''Expected result ={}'.format(min_time, 20.00))
    assert min_time == 20.00, 'Minimum time should be 20 for point: {}'.format(points)
    
@pytest.fixture()
def setup_test_013():
    fpath = setup_file(points)
    yield fpath
    os.remove(fpath)

def test_013_process_with_no_file():
    return_code = subprocess.call(['../bins/parcel_loader_v1' ], stderr=subprocess.STDOUT)
    print(' code ==== {} ==='.format(return_code))
    assert  return_code != 0