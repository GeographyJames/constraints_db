from src.db import main

class TestMain:
    def test_should_return_hello(self):
        assert main.hello() == "hello"