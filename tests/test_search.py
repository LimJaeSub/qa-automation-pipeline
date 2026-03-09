# test_search.py
import allure
from pages.search_page import SearchPage

@allure.epic("상품")
@allure.feature("상품 검색")
class TestSearch:

    @allure.story("키워드 검색 성공")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.description("유효한 키워드 입력 시 검색 결과 1개 이상 노출 확인")
    def test_search_valid_keyword(self, driver):
        page = SearchPage(driver)

        with allure.step("상품 목록 페이지 접속"):
            page.open()

        with allure.step("'dress' 키워드로 검색"):
            page.search("dress")

        with allure.step("검색 결과 1개 이상 확인"):
            results = page.get_results()
            assert len(results) > 0, "검색 결과가 있어야 합니다"

    @allure.story("검색 결과 없음")
    @allure.severity(allure.severity_level.MINOR)
    @allure.description("존재하지 않는 키워드 입력 시 결과 0개 확인")
    def test_search_no_result(self, driver):
        page = SearchPage(driver)

        with allure.step("상품 목록 페이지 접속"):
            page.open()

        with allure.step("'zzzzinvalidkeyword' 키워드로 검색"):
            page.search("zzzzinvalidkeyword")

        with allure.step("검색 결과 0개 확인"):
            results = page.get_results()
            assert len(results) == 0, "검색 결과가 없어야 합니다"