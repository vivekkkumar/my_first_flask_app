from tests.system.Base import BaseTest
import json


class TestHome(BaseTest):
    def test_home(self):
        with self.app() as c:
            r = c.get('/')
            self.assertEqual(r.status_code, 200)
            self.assertEqual(json.loads(r.get_data()), {'message': 'Hai world (Intentional hai instead of hello :) )'})