from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.informatyka.agh.edu.pl/pl/")
    page.get_by_role("link").first.click()
    page.get_by_role("link", name="Wydział", exact=True).click()
    page.get_by_role("link", name="O Wydziale").click()
    page.get_by_role("link", name="Strona główna").click()
    page.get_by_role("link", name="Nasze kierunki").click()
    page.get_by_role("heading", name="Nasze kierunki").click()
    page.get_by_role("link", name="Tworzenie przestrzeni").click()
    page.get_by_role("heading", name="Tworzenie przestrzeni").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
