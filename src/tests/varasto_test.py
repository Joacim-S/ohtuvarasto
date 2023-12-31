import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_negatiivinen_tilavuus_luodessa_muutetaan_nollaksi(self):
        self.varasto = Varasto(-5)
        
        self.assertAlmostEqual(self.varasto.tilavuus, 0.0)
        
    def test_negatiivinen_alkusaldo_nollataan(self):
        self.varasto = Varasto(5, -1)
        
        self.assertAlmostEqual(self.varasto.saldo, 0.0)
        
    def test_alkutilavuutta_suurempi_alkusaldo_asetetaan_alkutilavuuteen(self):
        self.varasto = Varasto(10, 15)
        
        self.assertAlmostEqual(self.varasto.saldo, 10)
        
    def test_negatiivise_maaran_lisays_ei_muuta_saldoa(self):
        self.varasto.lisaa_varastoon(-10)
        
        self.assertAlmostEqual(self.varasto.saldo, 0)
        
    def test_lisaa_varastoon_muuttaa_saldoa_oikein(self):
        self.varasto.lisaa_varastoon(5)
        
        self.assertAlmostEqual(self.varasto.saldo, 5)
        
    def test_liikaa_lisaaminen_asettaa_saldoksi_tilavuuden(self):
        self.varasto.lisaa_varastoon(200)
        
        self.assertAlmostEqual(self.varasto.saldo, 10)
    
    def test_negatiivinen_otto_palauttaa_nollan(self):
        saatu_maara = self.varasto.ota_varastosta(-12)
        
        self.assertAlmostEqual(saatu_maara, 0)
        
    def test_liikaa_ottaminen_palauttaa_saldon(self):
        self.varasto.lisaa_varastoon(7)
        saatu_maara = self.varasto.ota_varastosta(91)
        
        self.assertAlmostEqual(saatu_maara, 7)
        
    def test_varaston_tulostus_on_oikein(self):
        self.assertEqual(self.varasto.__str__(), 'saldo = 0, vielä tilaa 10')