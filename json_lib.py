import json


def test_json_str_with_newline():
    text = '{"sql": "Hello \n World!"}'
    json_str = json.loads(text)
    print(json_str)


if __name__ == "__main__":
    test_json_str_with_newline()
