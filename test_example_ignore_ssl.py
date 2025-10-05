from playwright.sync_api import sync_playwright

def test_example_ignore_ssl():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://mms.uat.exyte.net/")
        assert "OneERP UAT" in page.title()
        browser.close()
