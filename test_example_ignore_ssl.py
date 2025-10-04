import pytest

@pytest.mark.parametrize("browser_name", ["chromium"])
def test_example_ignore_ssl(browser_name, playwright):
    browser = playwright[browser_name].launch()
    context = browser.new_context(ignore_https_errors=True)
    page = context.new_page()
    page.goto("https://www.baidu.com/")
    assert "Timesheet" in page.title()
