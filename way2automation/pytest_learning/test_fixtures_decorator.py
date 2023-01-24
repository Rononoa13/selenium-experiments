import pytest

# Module level ma
@pytest.fixture(scope="module")
def setup():
    print("Creating DB Connection")
    
    yield #Teardown module jastai
    print("Closing DB Connection")


# Function level ma
@pytest.fixture(scope="function")
def before():
    print("Launching Browser")

    yield
    print("Closing Browser")


# def test_login(setup, before):
#     print("Executing login test.")

# def test_user_registration(before):
#     print("Executing user registration.")

@pytest.mark.usefixtures("setup", "before")
def test_login():
    print("Executing login test.")

@pytest.mark.usefixtures("before")
def test_user_registration():
    print("Executing user registration.")