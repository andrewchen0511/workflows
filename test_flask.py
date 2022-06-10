import pytest, json
from urllib.request import urlopen
from urllib.error import HTTPError

@pytest.mark.parametrize(
    "a, b, expected",
    [
        ("10", "5", {"status":"a>b"}),
        ("1", "5", {"status":"a<=b"}),
    ]
)
def test_flask1(a, b, expected):
    excepted = json.loads(urlopen(f"http://127.0.0.1:5001?a={a}&b={b}").read())
def test_flask2():
    with pytest.raises(HTTPError):
        json.loads(urlopen(f"http://127.0.0.1:5001?a=aaa&b=10").read())