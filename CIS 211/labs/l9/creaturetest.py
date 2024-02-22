import unittest
import creature


class TestCreature(unittest.TestCase):

    def test_all(self):
        doggy1 = creature.Head("Kane")
        doggy2 = creature.Head("Wolfie")
        doggy3 = creature.Head("Rugal")
        doggy4 = creature.Head("Taker")
        ort1 = creature.Orthrus(doggy1, doggy2)
        ort2 = creature.Orthrus(doggy3, creature.Head("Jeff"))
        cer = creature.Cerberus(ort1, doggy4, ort2)
        self.assertEqual(str(cer), "[(Kane Wolfie) Taker (Rugal Jeff)]")
        self.assertEqual(cer.search("Drogon"), False)
        self.assertEqual(cer.search("Rugal"), True)