import os
import subprocess
import re
import pytest 
import collections

fpath = 'input_file.txt'

def setup_file(points):
    points = points 
    num_points = len(points)
    try:  
        subprocess.check_call ('echo "{}" > {}'.format(num_points, fpath), shell=True)
        for i in range (num_points):
            subprocess.check_call('echo "\n{},{},{}" >> {}'.format(points[i][0], points[i][1], points[i][2], fpath), shell=True)
    except subprocess.CalledProcessError as e:
        pytest.fail("Failled to create test file. Error: {}".format(e))

def read_from_file():
    file1 = open(fpath, 'r') 
    Lines = file1.readlines()
    for line in Lines:
        if line.isspace():
            Lines.remove(line)
        
    num_points = int (Lines[0].strip())

    points = []
    for point in Lines[1:]:
        points.append(point.rstrip())

    file_content = []
    file_content.append(num_points)
    file_content.append(points)
    return file_content

def call_process():
    out = subprocess.check_output('./parcel_loader_v1 -f ./{}'.format(fpath), stderr=subprocess.STDOUT, shell=True).decode()
    return out

def find_match(regex,out):
    #points = setup_test
    #print('Testing points: {}'.format(points))
    match = re.findall(regex,out, re.MULTILINE)  
    print('Out: \n {} Type: \n {} Match: {}'.format(out,type(out),type(match)))
    print(type(match[0]))
    if not match:
        pytest.fail('Failed to parse minimum time value from output: {}'.format(out))
    return match[0]

@pytest.fixture
def setup_test_008():
    points = ((12,10,10),)
    setup_file(points)
    yield points
    os.remove(fpath)

def test_008_load_time(setup_test_008):
    points = setup_test_008
    regex = r'^Minimum time = (\d+\.\d\d)'
    print('Testing points: {}'.format(points))
    out = call_process()
    match = find_match(regex,out)
    min_time = float (match)
    print ('Actual result = {}\n''Expected result <={}'.format(min_time, 30.00))
    assert min_time <= 30.00, 'Minimum time should be 30 or less for point: {}'.format(points)

@pytest.fixture
def setup_test_009():
    points = ((1,10,10),)
    setup_file(points)
    yield points
    os.remove(fpath)
#rest multiple points 
def test_009_load_time_format(setup_test_009):
    points = setup_test_009
    regex = r'^Minimum time = \d+\.\d\d'
    out = call_process()
    min_time_format = find_match(regex,out)
    print ('Actual pointsresult = {}\n''Expected result = {}'.format(min_time_format, 'Minimum time = 21.00'))
    assert min_time_format == 'Minimum time = 21.00' , 'Minimum time should look like [Minimum time = 21.00] for point: {}'.format(points)

@pytest.fixture
def setup_test_010():
    points = ((1,10,10),)
    setup_file(points)
    yield points
    os.remove(fpath)

def test_010_load_time_fromat(setup_test_010):
    points = setup_test_010
    regex = r'^Starting from point: x=\d,y=\d'
    out = call_process()
    min_time_format = find_match(regex,out)
    print ('Actual result = {}\n''Expected result = {}'.format(min_time_format, 'Minimum time = 21.00'))
    assert min_time_format == 'Starting from point: x=0,y=0' , 'Minimum time should look like [Starting from point: x=0,y=0] for point: {}'.format(points)

@pytest.fixture
def setup_test_011():
    points = ((1,10,10),)
    setup_file(points)
    yield points
    os.remove(fpath)

def test_011_load_time_format(setup_test_011):
    points = setup_test_011
    regex = r'^Stopping at point: x=\d\d,y=\d\d'
    out = call_process()
    min_time_format = find_match(regex,out)
    print ('Actual result = {}\n''Expected result = {}'.format(min_time_format, 'Minimum time = 21.00'))
    assert min_time_format == 'Stopping at point: x=20,y=20' , 'Minimum time should look like [Stopping at point: x=20,y=20] for point: {}'.format(points)

@pytest.fixture
def setup_test_012():
    #(20, d, , (2,3), )
    points = ((1,10,10),(2,10,20))
    setup_file(points)
    yield points
    os.remove(fpath)

def test_012_validate_points(setup_test_012):
    test_points = setup_test_012
    file_content = read_from_file()
    num_points = file_content[0]
    points = file_content[1]
    print ('points: == {}==\n num points === {} ==='.format(points,num_points))
    #assert num_points == 2
    assert num_points == len(points) ,'THe total number of points should be eqaul to the number points in the test file for {}'.format(test_points)

@pytest.fixture
def setup_test_013():
    points = ((1,14,5),(2,5,4))
    setup_file(points)
    yield points
    os.remove(fpath)

def test_013_point_foramt(setup_test_013): 
    file_content = read_from_file()
    num_points = file_content[0]
    points = file_content[1]

    #regex = r'[0-9]+,[0-9]|[0-9][0-9],[0-9]'
    regex = r'\d+,\d+,\d+'
    match = []
    found = None
    for p in points:
        found = re.search(regex,p)
        if found != None:
            match.append(found.group())

    print ('points: == {} ==\n'.format(points))
    print ('Match: == {} ==\n'.format(match))

    assert  collections.Counter(match) == collections.Counter(points), 'The point format should be 3 comma seprated values'

def test_process_with_no_file():
    pass