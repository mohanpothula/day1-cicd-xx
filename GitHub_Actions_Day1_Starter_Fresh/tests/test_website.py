"""Tiny, dependency-free checks used as the GitHub Actions CI quality gate."""
from html.parser import HTMLParser
from pathlib import Path
import unittest

HTML = (Path(__file__).resolve().parents[1] / "site" / "index.html").read_text(encoding="utf-8")


class StatusParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.inside_status = False
        self.status_text = []

    def handle_starttag(self, tag, attrs):
        if tag == "span" and dict(attrs).get("id") == "service-status":
            self.inside_status = True

    def handle_data(self, data):
        if self.inside_status:
            self.status_text.append(data)

    def handle_endtag(self, tag):
        if tag == "span" and self.inside_status:
            self.inside_status = False


class TestWebsite(unittest.TestCase):
    def test_has_application_heading(self):
        self.assertIn('id="app-title"', HTML)
        self.assertIn("Customer Order Status", HTML)

    def test_health_gate(self):
        parser = StatusParser()
        parser.feed(HTML)
        self.assertEqual("".join(parser.status_text).strip(), "Healthy", "Release blocked: website status must be Healthy")

    def test_has_version_label(self):
        self.assertIn('id="release-version"', HTML)

    def test_loads_relative_assets(self):
        self.assertIn('href="./style.css"', HTML)
        self.assertIn('src="./app.js"', HTML)


if __name__ == "__main__":
    unittest.main()
