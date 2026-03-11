# test_search.py
import allure
import pytest
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

    @allure.story("검색 결과 없음 - 안내 문구")
    @allure.severity(allure.severity_level.MINOR)
    @allure.description("존재하지 않는 키워드 입력 시 'No products found' 메시지 노출 확인")
    @pytest.mark.xfail(reason="SCRUM-26: 검색 결과 없을 때 안내 문구 미구현") # 현재 버그로 인해 실패하는 테스트 표시
    def test_search_no_result_message(self, driver):
        page = SearchPage(driver)

        with allure.step("상품 목록 페이지 접속"):
            page.open()

        with allure.step("'zzzzinvalidkeyword' 키워드로 검색"):
            page.search("zzzzinvalidkeyword")

        with allure.step("'No products found' 메시지 노출 확인"):
            message = page.get_no_results_message()
            assert message == "No products found!", "검색 결과 없음 메시지가 표시되어야 합니다"