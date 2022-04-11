import unittest
from src.msg import mensagem


class RoteiroTeste(unittest.TestCase):

	def test_ct01(self):
		res = mensagem('casos-de-teste/ct01.txt')
		self.assertEqual(res, 'spam')
	
	def test_ct02(self):
		res = mensagem('casos-de-teste/ct02.txt')
		self.assertEqual(res, 'ham')

	def test_ct03(self):
		res = mensagem('casos-de-teste/ct03.txt')
		self.assertEqual(res, 'spam')
	
	def test_ct04(self):
		res = mensagem('casos-de-teste/ct04.txt')
		self.assertEqual(res, 'spam')


if __name__ == '__main__':
	unittest.main()
