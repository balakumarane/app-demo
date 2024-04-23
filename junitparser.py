from junitparser import JUnitXml

xml = JUnitXml.fromfile('results.xml')
for suite in xml:
    # handle suites
    for case in suite:
        # handle cases
        print(case)
