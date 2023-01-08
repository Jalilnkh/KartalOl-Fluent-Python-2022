# content of test_sample.py
def func(x):
    return x + 1


def test_answer():
    assert func(3) == 4

# content of test_class.py
class TestClass:
    def test_one(self):
        x = "this"
        assert "h" in x

    def test_two(self):
        x = "hello"
        assert hasattr(x, "check")