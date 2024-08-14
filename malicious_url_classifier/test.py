import os, sys, inspect, csv, requests

from classifier import classify_url

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

import unittest



def chunks(lst, chunk_size):
    """Yield successive n-sized chunks from l."""
    i = 0
    while True:
        chunk = lst[i: i + chunk_size]
        if not chunk:
            break
        yield chunk
        i += chunk_size


solution = {}
raw_url = "https://abnormalsecurity-public.s3.us-east-1.amazonaws.com/url_interview_cleaned.csv"
response = requests.get(raw_url)
decoded_content = response.content.decode('utf-8')
solution = {}
reader = csv.reader(decoded_content.replace(" ", "\t").splitlines(), delimiter='\t')
for is_malicious, url in reader:
    solution[url] = is_malicious == "1"

safe_urls = [x for x, y in solution.items() if not y]
malicious_urls = [x for x, y in solution.items() if y]

test_urls = list(chunks(sorted(safe_urls, key=lambda x: x[12]), 25))
for index, url in enumerate(malicious_urls):
    actual_index = index % len(test_urls)
    test_urls[actual_index].append(url)


def generate_tests(urls):
    def test(self):
        misclassified = []
        for url in urls:
            result = classify_url(url)
            expected = solution[url]
            if result != expected:
                misclassified.append((url, result, expected))
        if misclassified:
            error = ["Following URLs are misclassified:"] + [
                "%s classified as %s, should be %s" % x
                for x in misclassified
            ]
            self.fail("\n".join(error))

    return test


class TestingSumNumbers(unittest.TestCase):
    pass


for index, urls in enumerate(test_urls):
    setattr(
        TestingSumNumbers,
        f"test_{index}",
        generate_tests(urls)
    )