from playwright.sync_api import sync_playwright

def test_example_ignore_ssl():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://mms.uat.exyte.net/TestLoginPage.aspx",timeout=60_0000)
        page.locator("#txtAccount").click()
        page.locator("#txtAccount").fill("admin")
        page.locator("#txtPwd").click()
        page.locator("#txtPwd").fill("MMS@MW")
        page.get_by_role("button", name="Login").click()
        page.get_by_role("link", name="Huang, Zhi Cheng Edison").click()
        page.goto("https://mms.uat.exyte.net/NavigationPage.aspx")
        assert "OneERP UAT" in page.title()
        browser.close()
