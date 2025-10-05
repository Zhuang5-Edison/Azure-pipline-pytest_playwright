import pytest

@pytest.mark.asyncio
async def test_example_ignore_ssl(playwright):
    browser = await playwright.chromium.launch(headless=True)
    context = await browser.new_context(ignore_https_errors=True)
    page = await context.new_page()
    await page.goto("https://www.baidu.com/")
    assert "Welcome" in await page.title()
    await browser.close()
