import pytest

# Before running any function in the file
# At very first.
def setup_module(module):
    print("Creating DB connection")

# Execute after running every test cases
# At the very end
def teardown_module(module):
    print("Closing DB Connection")


# setup function s 
def setup_function():
    print("launching browser")

# Executes at end of each/every function
def teardown_function():
    print("Closing the browser")

def test_login():
    print("Executing login test.")

def test_user_registration():
    print("Executing user registration.")