import unittest
from app import soma

class TestSoma(unittest.TestCase):
    def test_soma(self):
        self.assertEqual(soma(2, 2), 5)  # Erro intencional: 2 + 2 != 5
