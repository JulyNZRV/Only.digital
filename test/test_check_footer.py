from selenium.webdriver.common.by import By
import re

def test_footer_elements(browser):
    browser.get("https://only.digital/job")

    footer = browser.find_element(By.TAG_NAME, "footer")
    assert footer.is_displayed(), "Футер не отображается на странице"

    footer_text = footer.text

    assert "©" in footer_text, "В футере отсутствует символ копирайта"

    assert "Политика конфиденциальности" in footer_text, "В футере отсутствует 'Политика конфиденциальности'"

    years = re.findall(r"20\d{2}", footer_text)
    assert years, "В футере не найден год"
    if len(years) == 2:
        start, end = map(int, years)
        assert start <= end, f"Некорректный диапазон лет: {start} - {end}"

    links = footer.find_elements(By.TAG_NAME, "a")
    hrefs = [link.get_attribute("href") for link in links if link.get_attribute("href")]

    print("Ссылки в футере:", hrefs)

    expected_socials = {
        "behance.net": "Behance",
        "dprofile.ru": "DProfile",
        "t.me": "Telegram",
        "vk.com": "ВКонтакте"
    }

    for domain, name in expected_socials.items():
        assert any(domain in href.lower() for href in hrefs), f"В футере отсутствует ссылка на {name}"
