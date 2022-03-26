import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti


class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.maksukortti_paljon = Maksukortti(1000)  # 10€
        self.maksukortti_vahan = Maksukortti(100)  # 1€

    # Alustus
    def test_kassapaate_saldo_alustettu_oikein(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_kassapaate_edulliset_alustettu_oikein(self):
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_kassapaate_maukkaat_alustettu_oikein(self):
        self.assertEqual(self.kassapaate.maukkaat, 0)

    # Käteisostot
    def test_kateismaksu_edullisesti_kasvattaa_saldoa(self):
        self.kassapaate.syo_edullisesti_kateisella(240)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)

    def test_kateismaksu_maukkaasti_kasvattaa_saldoa(self):
        self.kassapaate.syo_maukkaasti_kateisella(400)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100400)

    def test_kateismaksu_edullisesti_vaihtoraha_oikein(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(400), 160)

    def test_kateismaksu_maukkaastu_vaihtoraha_oikein(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(600), 200)

    def test_kateismaksu_edullisesti_myytyjen_maara_kasvaa(self):
        self.kassapaate.syo_edullisesti_kateisella(240)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_kateismaksu_maukkaasti_myytyjen_maara_kasvaa(self):
        self.kassapaate.syo_maukkaasti_kateisella(400)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    # Liian vähän käteismaksulla
    def test_kateismaksu_edullisesti_liian_vahan_ei_kasvata_saldoa(self):
        self.kassapaate.syo_edullisesti_kateisella(100)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_kateismaksu_maukkaasti_liian_vahan_ei_kasvata_saldoa(self):
        self.kassapaate.syo_maukkaasti_kateisella(300)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_kateismaksu_edullisesti_liian_vahan_palauttaa_kaiken(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(100), 100)

    def test_kateismaksu_maukkaastu_liian_vahan_palauttaa_kaiken(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(300), 300)

    def test_kateismaksu_edullisesti_liian_vahan_myytyjen_maara_ei_kasva(self):
        self.kassapaate.syo_edullisesti_kateisella(100)
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_kateismaksu_maukkaasti_liian_vahan_myytyjen_maara_ei_kasva(self):
        self.kassapaate.syo_maukkaasti_kateisella(200)
        self.assertEqual(self.kassapaate.edulliset, 0)

    # Korttiostot
    def test_kortti_edullisesti_veloitetaan_kortilta(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti_paljon)
        self.assertEqual(str(self.maksukortti_paljon), "saldo: 7.6")

    def test_kortti_maukkaasti_veloitetaan_kortilta(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti_paljon)
        self.assertEqual(str(self.maksukortti_paljon), "saldo: 6.0")

    def test_kortti_edullisesti_palauttaa_true(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(
            self.maksukortti_paljon), True)

    def test_kortti_maukkaasti_palauttaa_true(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(
            self.maksukortti_paljon), True)

    def test_kortti_edullisesti_nostaa_myytyjen_maaraa(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti_paljon)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_kortti_maukkaasti_nostaa_myytyjen_maaraa(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti_paljon)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_kortti_edullisesti_kassa_saldo_ei_muutu(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti_paljon)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_kortti_maukkaasti_kassa_saldo_ei_muutu(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti_paljon)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    # Liian vähän kortilla
    def test_kortti_edullisesti_liian_vahan_ei_veloiteta_kortilta(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti_vahan)
        self.assertEqual(str(self.maksukortti_vahan), "saldo: 1.0")

    def test_kortti_maukkaasti_liian_vahan_ei_veloiteta_kortilta(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti_vahan)
        self.assertEqual(str(self.maksukortti_vahan), "saldo: 1.0")

    def test_kortti_edullisesti_liian_vahan_palauttaa_false(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(
            self.maksukortti_vahan), False)

    def test_kortti_maukkaasti_liian_vahan_palauttaa_false(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(
            self.maksukortti_vahan), False)

    def test_kortti_edullisesti_liian_vahan_ei_nosta_myytyjen_maaraa(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti_vahan)
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_kortti_maukkaasti_liian_vahan_ei_nosta_myytyjen_maaraa(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti_vahan)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    # Kortin lataus
    def test_kortin_lataus_lisaa_kortin_saldoa(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti_vahan, 100)
        self.assertEqual(str(self.maksukortti_vahan), "saldo: 2.0")

    def test_kortin_lataus_lisaa_rahan_kassaan(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti_vahan, 100)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100100)

    def test_kortin_lataus_negatiivinen_summa_ei_toimi_kortin_osalta(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti_vahan, -100)
        self.assertEqual(str(self.maksukortti_vahan), "saldo: 1.0")

    def test_kortin_lataus_negatiivinen_summa_ei_toimi_kassan_osalta(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti_vahan, -100)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
