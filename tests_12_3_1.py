class Runner:
    def __init__(self, name):
        self.name = "Eva"
        self.name = "Anna"
        self.name = "Janet"
        self.distance = 0

    def run(self):
        self.distance += 10

    def walk(self):
        self.distance += 5

    def __str__(self):
        return self.name


import unittest

class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, "Запускаем тест")
    def test_walk(self):
        eva = Runner("Eva")
        for _ in range(10):
            eva.walk()
        self.assertEqual(eva.distance, 50)

    @unittest.skipIf(is_frozen, "Запускаем тест")
    def test_run(self):
        eva = Runner("Eva")
        for _ in range(10):
            eva.run()
        self.assertEqual(eva.distance, 100)

    @unittest.skipIf(is_frozen, "Запускаем тест")
    def test_challenge(self):
        anna = Runner("Anna")
        jan = Runner("Janet")
        for _ in range(10):
            anna.walk()
            jan.run()
        self.assertNotEqual(anna.distance, jan.distance)


if __name__ == "__main__":
    unittest.main()