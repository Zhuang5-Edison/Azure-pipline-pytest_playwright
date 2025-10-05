from playwright.sync_api import sync_playwright

def test_example_ignore_ssl():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(ignore_https_errors=True)
        page = context.new_page()
        page.goto("https://mms.uat.exyte.net/TestLoginPage.aspx")
        page.locator("#txtAccount").click()
        page.locator("#txtAccount").fill("admin")
        page.locator("#txtPwd").click()
        page.locator("#txtPwd").press("CapsLock")
        page.locator("#txtPwd").fill("MMS@MW")
        page.get_by_role("button", name="Login").click()
        page.once("dialog", lambda dialog: dialog.dismiss())
        page.get_by_role("link", name="Huang, Zhi Cheng Edison").click()
        page.goto("https://mms.uat.exyte.net/NavigationPage.aspx")
        assert "OneERP UAT" in page.title()
        browser.close()
