from hello import cool, toyou, add, subtract


def test_cool():
    assert cool("Miley") == "Cool!"
    assert cool("Bubble") == "Not cool at all.."

def setup_function(function):
    print(f" Running Setup: {function.__name__}")
    function.x = 10


def teardown_function(function):
    print(f" Running Teardown: {function.__name__}")
    del function.x


### Run to see failed test
#def test_hello_add():
#    assert add(test_hello_add.x) == 12

def test_hello_subtract():
    assert subtract(test_hello_subtract.x) == 9