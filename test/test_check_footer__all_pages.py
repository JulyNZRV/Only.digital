from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

SOCIAL_DOMAINS = {
    "behance.net": "Behance",
    "dprofile.ru": "Dribbble",
    "t.me": "Telegram",
    "vk.com": "ВКонтакте"
}

def check_footer(browser):
    """Проверяет футер на странице"""
    try:
        # Ждём элемент футера в DOM
        footer = WebDriverWait(browser, 15).until(
            EC.presence_of_element_located((By.TAG_NAME, "footer"))
        )
    except:
        print(f"Футер отсутствует на странице {browser.current_url}")
        return

    # Проверяем текст футера
    footer_text = footer.text.strip()
    if not footer_text:
        print(f"Футер пустой на странице {browser.current_url}")

    # Копирайт
    try:
        footer.find_element(By.XPATH, "//*[contains(text(),'©')]")
    except:
        print(f"© отсутствует на странице {browser.current_url}")

    # Политика конфиденциальности
    try:
        footer.find_element(By.LINK_TEXT, "Политика конфиденциальности")
    except:
        print(f"Политика конфиденциальности отсутствует на странице {browser.current_url}")

    # Проверка соцсетей
    links = footer.find_elements(By.TAG_NAME, "a")
    hrefs = [link.get_attribute("href") for link in links if link.get_attribute("href")]

    for domain, name in SOCIAL_DOMAINS.items():
        if not any(domain in href for href in hrefs):
            print(f"Ссылка на {name} ({domain}) отсутствует на странице {browser.current_url}")

def test_footer_on_all_pages(browser):
    """Проверяет футер на всех страницах сайта"""
    pages = [
        "https://only.digital/",
        "https://only.digital/projects",
        "https://only.digital/company",
        "https://only.digital/fields",
        "https://only.digital/job",
        "https://only.digital/blog",
        "https://only.digital/contacts"
    ]

    for url in pages:
        browser.get(url)
        print(f"\nПроверка футера на странице: {url}")
        check_footer(browser)
