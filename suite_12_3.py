import unittest
import tests_12_3_1
import tests_12_3_2

run_tourST = unittest.TestSuite()
run_tourST.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3_1.RunnerTest))
run_tourST.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3_2.TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(run_tourST)

