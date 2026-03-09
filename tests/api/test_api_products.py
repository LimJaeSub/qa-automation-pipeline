import requests
import allure

BASE_URL = "https://automationexercise.com/api"

@allure.epic("상품")
@allure.feature("상품 API")
class TestProductsAPI:

    @allure.story("상품 목록 조회")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description("상품 목록 API 호출 시 200 응답과 상품 데이터 확인")
    def test_get_products(self):
        with allure.step("상품 목록 API 호출"):
            response = requests.get(f"{BASE_URL}/productsList")

        with allure.step("응답 상태 코드 확인"):
            assert response.status_code == 200, "응답 상태 코드는 200이어야 합니다"

        with allure.step("상품 데이터 확인"):
            data = response.json()
            assert "products" in data, "응답에 'products' 키가 있어야 합니다"
            assert isinstance(data["products"], list), "'products'는 리스트여야 합니다"
            assert len(data["products"]) > 0, "상품이 최소 1개 이상 있어야 합니다"

    @allure.story("상품 검색 api")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.description("상품 검색 API 호출 시 200 응답과 검색 결과 확인")
    def test_search_products(self):
        with allure.step("/searchProduct API 호출 (키워드: 'dress')"):
            response = requests.post(
                f"{BASE_URL}/searchProduct",
                data={"search_product": "dress"}
            )

        with allure.step("상태 코드 200 확인"):
            assert response.status_code == 200, "응답 상태 코드는 200이어야 합니다."

        with allure.step("검색 결과 1개 이상 확인"):
            data = response.json()
            assert "products" in data
            assert len(data["products"]) > 0, "검색 결과가 최소 1개 이상이여야 합니다."

    @allure.story("잘못된 HTTP 메서드 검증")
    @allure.severity(allure.severity_level.MINOR)
    @allure.description("상품 목록 API에 잘못된 HTTP 메서드 사용 시 405 응답 확인")
    def test_post_products_list_no_allowed(self):
        with allure.step("상품 목록 POST 요청"):
            response = requests.post(
                f"{BASE_URL}/productsList",
            )

        with allure.step("상태코드 200 확인"):
            assert response.status_code == 200, "응답 상태 코드는 200이어야 합니다."
        
        with allure.step("응답 코드 405 확인"):
            data = response.json()
            assert data["responseCode"] == 405
            assert data["message"] == "This request method is not supported."
            
    @allure.story("상품 검색 - 파라미터 누락")
    @allure.severity(allure.severity_level.MINOR)
    @allure.description("상품 검색 파라미터 없이 호출 시 400 응답 확인")
    def test_search_products_no_parameter(self):
        with allure.step("/searchProduct API 호출 (파라미터 누락)"):
            response = requests.post(
                f"{BASE_URL}/searchProduct",
            )
        
        with allure.step("상태 코드 200 확인"):
            assert response.status_code == 200, "응답 상태 코드는 200이어야 합니다."
            # 사이트는 항상 200으로 응답
        
        with allure.step("에러 메시지 확인"):
            data = response.json()
            assert data["responseCode"] == 400
            assert data["message"] == "Bad request, search_product parameter is missing in POST request."
        