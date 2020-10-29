from unittest import TestCase

from published.published import published

class Test_published(TestCase):
    def test_is_published(self):
        p = published()
        self.assertTrue(p.is_published())

    def test_is_published_false(self):
        p = published()
        p.published = False
        self.assertRaises(RuntimeError, lambda: p.is_published())
