import unittest

suite = unittest.TestSuite()
test_modules = ["tests.test_bot", "tests.test_dataset_item", "tests.test_args_parser"]
for t in test_modules:
    try:
        mod = __import__(t, globals(), locals(), ["suite"])
        suite_fn = getattr(mod, "suite")
        suite.addTest(suite_fn())
    except (ImportError, AttributeError):
        suite.addTest(unittest.defaultTestLoader.loadTestsFromName(t))

unittest.TextTestRunner().run(suite)
