import unittest

suite = unittest.TestSuite()
test_modules = []
for t in test_modules:
    try:
        mod = __import__(t, globals(), locals(), ["suite"])
        suite_fn = getattr(mod, "suite")
        suite.addTest(suite_fn())
    except (ImportError, AttributeError):
        suite.addTest(unittest.defaultTestLoader.loadTestsFromName(t))

unittest.TextTestRunner().run(suite)
