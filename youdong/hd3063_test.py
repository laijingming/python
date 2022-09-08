import json
import unittest
import core.dushi as dushi


class TestHd3063(unittest.TestCase):
    def test_create(self):
        res = dushi.cmd(1000465, {
            "huodong2": {
                "hd3063Info": {"name": "n1"}
            }
        })
        text = res.text
        if text.find("<pre>")!=-1:
            text = json.loads(text[:text.find("<pre>")])
        else:
             text = json.loads(text)
        if text['s']==0:
            print(text['a']['system']['errror']['msg'])
        self.assertEqual(text['s'], 1)


if __name__ == '__main__':
    unittest.main()
