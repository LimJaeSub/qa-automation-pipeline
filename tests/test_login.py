import allure
from pages.login_page import LoginPage

# 사용자 인증
@allure.epic("사용자 인증")
# 로그인 테스트 그룹화
@allure.feature("로그인")


class TestLogin:
    # 로그인 : 정상 로그인
    @allure.story("정상 로그인")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description("유효한 계정으로 로그인 후 URL 변경 확인")
    
    def test_login_success(driver):
        page = LoginPage(driver)
        
        with allure.step("로그인 페이지 열기"):
            page.open()
        
        with allure.step("계정 로그인 시도"):
            page.login("jasubtest@example.com", "test1234")
            
        with allure.step("로그인 성공 여부 확인"):
            assert "https://automationexercise.com" in driver.current_url
            
    # 로그인 : 로그인 실패
    @allure.story("로그인 실패")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.description("잘못된 비밀번호 로그인 시도 후 오류 메시지 확인")
    
    def test_login_failure_password(driver):
        page = LoginPage(driver)
        
        with allure.step("로그인 페이지 열기"):
            page.open()
        
        with allure.step("잘못된 비밀번호로 로그인 시도"):
            page.login("jasubtest@example.com", "wrongpassword")
        
        with allure.step("에러 메시지 노출 확인"):
            error = page.get_error_message()
            assert error is not None, "에러 메시지가 표시되어야 합니다"
        

        
    

