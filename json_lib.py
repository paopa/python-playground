import json


def test_json_str_with_newline():
    text = '{"sql": "Hello \n World!"}'
    json_str = json.loads(text)
    print(json_str)


def test_parse_json_array():
    text = '[{"sql": "Hello World!"}, {"sql": "SELECT 1"}]'
    res = json.loads(text)
    for r in res:
        print(r)
        print(r["sql"])


if __name__ == "__main__":
    # test_json_str_with_newline()
    test_parse_json_array()
