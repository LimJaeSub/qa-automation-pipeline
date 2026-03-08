import requests
import allure

BASE_URL = "https://automationexercise.com/api"

# 테스트 임시 계정
TEST_USER = {
    "name": "Jasub Test",
    "email": "jasub_auto_test@example.com",
    "password": "test1234",
    "title": "Mr",
    "birth_date": "1",
    "birth_month": "1",
    "birth_year": "1995",
    "firstname": "Jasub",
    "lastname": "Moon",
    "company": "TestCorp",
    "address1": "123 Test Street",
    "address2": "",
    "country": "Korea",
    "zipcode": "12345",
    "state": "Seoul",
    "city": "Seoul",
    "mobile_number": "01012345678"
}

@allure.epic("사용자 인증")
@allure.feature("회원가입 API")
class TestUserAPI:

    @allure.story("회원가입")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description("회원가입 API 호출 시 201 응답과 성공 메시지 확인")
    def test_create_account(self):
        with allure.step("기존 계정 삭제 (테스트 초기화)"):
            requests.delete(
                f"{BASE_URL}/deleteAccount",
                data={"email": TEST_USER["email"], "password": TEST_USER["password"]}
            )
        
        with allure.step("회원가입 요청"):
            response = requests.post(
                f"{BASE_URL}/createAccount",
                data=TEST_USER
            )
        
        with allure.step("응답 상태 코드 확인"):
            assert response.status_code == 200
        
        with allure.step("회원가입 성공 메시지 확인"):
            data = response.json()
            assert data["responseCode"] == 201
            assert data["message"] == "User created!"

    @allure.story("회원 삭제")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description("회원 삭제 API 호출 시 계정 삭제 확인")
    def test_delete_account(self):
        with allure.step("테스트용 계정 생성"):
            requests.post(
                f"{BASE_URL}/createAccount",
                data=TEST_USER
            )

        with allure.step("회원 삭제 요청"):
            response = requests.delete(
                f"{BASE_URL}/deleteAccount",
                data={"email": TEST_USER["email"], "password": TEST_USER["password"]}
            )
        
        with allure.step("응답 상태 코드 확인"):
            assert response.status_code == 200

        with allure.step("회원 삭제 성공 메시지 확인"):
            data = response.json()
            assert data["responseCode"] == 200
            assert data["message"] == "Account deleted!"