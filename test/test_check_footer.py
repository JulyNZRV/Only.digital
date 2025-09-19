from selenium.webdriver.common.by import By

URL = "https://only.digital/job"


def test_footer_elements(driver):
    driver.get(URL)

    footer = driver.find_element(By.TAG_NAME, "footer")
    assert footer.is_displayed(), "Футер не отображается на странице"

    social_links = ["be", "dp", "tg", "vk"]
    footer_text = footer.text.lower()
    for link_text in social_links:
        assert link_text in footer_text, f"В футере отсутствует '{link_text}'"


    assert "© 2014 - 2025" in footer.text, "В футере отсутствует © 2014 - 2025"
    assert "Политика конфиденциальности" in footer.text, "В футере отсутствует 'Политика конфиденциальности'"

