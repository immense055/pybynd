import unittest

import pybynd.test

testLoad = unittest.TestLoader()
suites = testLoad.loadTestsFromModule(pylynd.test)

runner = unittest.TextTestRunner(verbosity=1)
runner.run(suites)
