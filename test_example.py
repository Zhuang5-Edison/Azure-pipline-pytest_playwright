from playwright.sync_api import sync_playwright

def handle_ssl_errors():
    with sync_playwright() as p:
        browser = p.chromium.launch(args=['--ignore-ssl-errors', '--ignore-certificate-errors'])
        context = browser.new_context(ignore_https_errors=True)
        page = context.new_page()
        page.goto("https://apps.uat.exyte.net/eTimesheetOneERPUAT/Default.aspx")
        print(page.title())
        browser.close()
