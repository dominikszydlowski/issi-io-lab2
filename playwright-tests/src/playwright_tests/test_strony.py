from playwright.sync_api import Page, expect


def test_strona_glowna(page: Page):
    page.goto("https://www.informatyka.agh.edu.pl/pl/")

    expect(
        page.get_by_role("heading", name="Współpraca")
    ).to_be_visible()


def test_o_wydziale(page: Page):
    page.goto("https://www.informatyka.agh.edu.pl/pl/")

    page.get_by_role("link", name="Wydział", exact=True).click()
    page.get_by_role("link", name="O Wydziale").click()

    expect(
        page.get_by_role("heading", name="O Wydziale")
    ).to_be_visible()

    expect(
        page.get_by_text("Adres siedziby:")
    ).to_have_count(1)


def test_nasze_kierunki(page: Page):
    page.goto("https://www.informatyka.agh.edu.pl/pl/")

    page.get_by_role("link", name="Nasze kierunki").click()

    expect(
        page.get_by_role("heading", name="Nasze kierunki")
    ).to_be_visible()


def test_zmiana_url(page: Page):
    page.goto("https://www.informatyka.agh.edu.pl/pl/")

    page.get_by_role("link", name="Nasze kierunki").click()
    page.get_by_role("link", name="Tworzenie przestrzeni").click()

    print(f"Aktualny URL: {page.url}")

    expect(page).to_have_url(
        "https://www.informatyka.agh.edu.pl/pl/studenci/"
        "dla-kandydatow/kierunki/"
        "tworzenie-przestrzeni-wirtualnych-i-gier/"
    )
