# test_api_login.py
import requests
import allure

BASE_URL = "https://automationexercise.com/api"


@allure.epic("사용자 인증")
@allure.feature("로그인 API")

class TestLoginAPI:

    @allure.story("정상 로그인")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description("유효한 계정으로 로그인 API 호출 시 200 응답과 토큰 확인")
    
    def test_login_sucess(self):
        with allure.step("로그인 API 호출"):
            response = requests.post(
                f"{BASE_URL}/verifyLogin",
                data={"email":"jasubtest@example.com", "password":"test1234"}
            )
        with allure.step("응답 상태 코드 확인"):
            assert response.status_code == 200, "응답 상태 코드는 200이어야 합니다"

    @allure.story("로그인 실패")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description("잘못된 계정으로 로그인 API 호출 시 404 응답과 실패 메시지 확인")
    
    def test_login_failure(self):
        with allure.step("잘못된 로그인 API 호출"):
            response = requests.post(
                f"{BASE_URL}/verifyLogin",
                data={"email":"test@example.com","password":"asdfd123x"}
            )
        
        with allure.step("응답 상태 코드 확인"):
            assert response.status_code == 200
        with allure.step("로그인 실패 메시지 확인"):
            data = response.json()
            assert data["responseCode"] == 404

    
    @allure.story("이메일 파라미터 누락 검증")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.description("POST /verifyLogin 이메일 없이 호출 시 400 응답 확인")
    def test_verify_login_missing_email(self):
        with allure.step("POST /verifyLogin 이메일 없이 요청"):
            response = requests.post(
                f"{BASE_URL}/verifyLogin",
                data={"password": "test1234"}
            )
        with allure.step("상태코드 200 확인"):
            assert response.status_code == 200
        with allure.step("응답 코드 400 확인"):
            data = response.json()
            assert data["responseCode"] == 400
            assert data["message"] == "Bad request, email or password parameter is missing in POST request."

    @allure.story("잘못된 HTTP 메서드 검증")
    @allure.severity(allure.severity_level.MINOR)
    @allure.description("DELETE /verifyLogin 호출 시 405 응답 확인")
    def test_verify_login_delete_not_allowed(self):
        with allure.step("DELETE /verifyLogin 요청"):
            response = requests.delete(f"{BASE_URL}/verifyLogin")
        with allure.step("상태코드 200 확인"):
            assert response.status_code == 200
        with allure.step("응답 코드 405 확인"):
            data = response.json()
            assert data["responseCode"] == 405
            assert data["message"] == "This request method is not supported."