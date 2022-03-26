import unittest
from maksukortti import Maksukortti


class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)  # 1000 senttiä == 10 euroa

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_saldo_alustettu_oikein(self):
        self.assertEqual(str(self.maksukortti), "saldo: 10.0")

    def test_saldon_kasvattaminen_toimii(self):
        self.maksukortti.lataa_rahaa(25)
        self.assertEqual(str(self.maksukortti), "saldo: 10.25")

    def test_saldon_vahentaminen_toimii(self):
        self.maksukortti.ota_rahaa(65)
        self.assertEqual(str(self.maksukortti), "saldo: 9.35")

    def test_saldo_ei_muutu_jos_otetaan_liikaa(self):
        self.maksukortti.ota_rahaa(1200)
        self.assertEqual(str(self.maksukortti), "saldo: 10.0")

    def test_ota_rahaa_palauttaa_true_jos_riittaa(self):
        self.assertEqual(self.maksukortti.ota_rahaa(400), True)

    def test_ota_rahaa_palauttaa_false_jos_ei_riita(self):
        self.assertEqual(self.maksukortti.ota_rahaa(1200), False)
