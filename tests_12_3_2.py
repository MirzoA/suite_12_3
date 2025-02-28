import unittest

class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers

class TournamentTest(unittest.TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = []

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def setUp(self):
        self.runner1 = Runner('Усэйн', 10)
        self.runner2 = Runner('Андрей', 9)
        self.runner3 = Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        for i in cls.all_results:
            print({place: runner.name for place, runner in i.items()})

    def test_Tournament1(self):
        t = Tournament(90, self.runner1, self.runner3)
        result = t.start()
        TournamentTest.all_results.append(result)
        res = "Ник" == next(reversed(result.values()))
        self.assertTrue(res, f"Получен: {next(reversed(result.values()))}")

    def test_Tournament2(self):
        t = Tournament(90, self.runner2, self.runner3)
        result = t.start()
        TournamentTest.all_results.append(result)
        res = "Ник" == next(reversed(result.values()))
        self.assertTrue(res, f"Получен: {next(reversed(result.values()))}")

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_Tournament3(self):
        t = Tournament(90, self.runner1, self.runner2, self.runner3)
        result = t.start()
        TournamentTest.all_results.append(result)
        res = "Ник" == next(reversed(result.values()))
        self.assertTrue(res, f"Получен: {next(reversed(result.values()))}")

if __name__ == '__main__':
    unittest.main()