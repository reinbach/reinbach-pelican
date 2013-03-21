Title: Simple Test Runner
Date: 2012-07-25
Tags: flask, python
Slug: simple-test-runner
Author: Greg Reinbach

Working on a prototype using [Flask](http://flask.pocoo.org/docs/) and wanted a test runner as the unit tests were starting to grow.

I wanted something that was easy to add news tests to and allow me to spread them over multiple files/modules. The project has the following dir. structure;

    |- config.py 
    |- /project
        ... snip ...
    |- /tests
        |- api_config_type.py
    |- runserver.py
    | -test_runner.py <- this is the test runner script 

So the script starts off updating the sys.path, as to allow the tests to be able to access the relevant modules in the project

    sys.path.append(os.path.abspath(__file__))

Next I setup the list of the test modules I want to pull in a run each time I call the test runner. This is a simple list of them;

    test_modules = [
        'tests.api_config_type'
    ]

The next bit is the meat of it all. Here we loop through the test_modules list and import the test_cases from them which is another simple list. The test cases list in the module would look something like this;

    test_cases = [APIConfigTypeTest, APIConfigKeyTest]

Which holds the test cases you want to include in the test runner. So as the test runner loops through these test cases it uses UnitTest's test loader to load the test cases

    suites = []
    for test_mod in test_modules:
        _temp = __import__(test_mod, globals(), locals(), ['test_cases'], -1)
        for test_case in _temp.test_cases:
            suites.append(unittest.TestLoader().loadTestsFromTestCase(test_case))

The result of this is a master suites list of test cases to run. We add that to the test suite and then call the test runner to run them;

    alltests = unittest.TestSuite(suites)
    runner = unittest.TextTestRunner()

That's it, not perfect could do with some improvements, but it gets the job done and I'm back to writing more tests and adding them simply enough to the test runner.

The complete script (test_runner.py);

    import os
    import sys
    import unittest

    sys.path.append(os.path.abspath(__file__))

    test_modules = [
        'tests.api_config_type'
    ]

    suites = []
    for test_mod in test_modules:
        _temp = __import__(test_mod, globals(), locals(), ['test_cases'], -1)
        for test_case in _temp.test_cases:
            suites.append(unittest.TestLoader().loadTestsFromTestCase(test_case))

    alltests = unittest.TestSuite(suites)
    runner = unittest.TextTestRunner()

    if __name__ == "__main__":
        runner.run(alltests)

