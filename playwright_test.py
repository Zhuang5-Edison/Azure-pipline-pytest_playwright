from playwright.sync_api import sync_playwright

def test_example():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(ignore_https_errors=True)  # ← 忽略 HTTPS 错误
        page = context.new_page()
        page.goto("https://apps.uat.exyte.net/eTimesheetOneERPUAT/Default.aspx")
        page.screenshot(path="screenshots/sit.png", full_page=True)
        assert "MMS" in page.title()
        browser.close()
