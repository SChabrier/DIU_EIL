from unittest import TestCase
from partage import partager_montant
	
class TestPartage(TestCase):
	def test_partage_montant(self):
		self.assertEqual(partager_montant(4,2), [2,2])
		self.assertEqual(partager_montant(1,1), [1])
		self.assertEqual(partager_montant(5,3), [2,2,1])
		self.assertEqual(partager_montant(15,3), [5,5,5])
