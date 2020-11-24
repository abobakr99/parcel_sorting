import subprocess
import re
import pytest
import os

fpath = 'input_file.txt'

@pytest.fixture
def setup_test_001():
    points = ((11,20,20),)
    num_points = len(points)
    try: 
        subprocess.check_call ('echo "{}" > {}'.format(num_points, fpath), shell=True)
        for i in range (num_points):
            subprocess.check_call('echo "\n{},{},{}" >> {}'.format(points[i][0], points[i][1], points[i][2], fpath), shell=True)
    except subprocess.CalledProcessError as e:
        pytest.fail("Failled to create test file. Error: {}".format(e))
    yield points



def test_001_load_time(setup_test_001):
    points = setup_test_001

    print('Testing points: {}'.format(points))
    output = subprocess.check_output('./parcel_loader_v1 -f ./'+fpath, stderr=subprocess.STDOUT, shell=True).decode()
    print(output)
    match = re.findall(r'^Minimum\stime\s\=\s(\d\d\.\d\d)', output, re.MULTILINE)  
    print(match)
    if not match:
        pytest.fail('Failed to parse minimum time value from output: {}'.format(output))
    min_time = float (match[0])
    print ('Actual result = {}\n'
           'Expected result = {}'.format(min_time, 30.00))
    assert min_time == 30.00, 'Minimum time should be 20 for point: {}'.format(points)
    
    os.remove("input_file.txt")

 
