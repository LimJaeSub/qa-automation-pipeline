import allure
from pages.login_page import LoginPage

# 로그인 테스트 그룹화
@allure.feature("로그인")

# 로그인 : 정상 로그인
@allure.story("정상 로그인")
def test_login_success(driver):
    page = LoginPage(driver)
    page.open()
    page.login("jasubtest@example.com", "test1234")
    assert "https://automationexercise.com" in driver.current_url