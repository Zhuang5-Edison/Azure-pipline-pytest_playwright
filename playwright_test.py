from playwright.sync_api import sync_playwright

def test_example():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("https://sit.mms.exyte.net/")
        page.screenshot(path="fullpage.png", full_page=True)
        print("Test Pass !")
        browser.close()
