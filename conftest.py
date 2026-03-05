import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless") # 브라우저를 띄우지 않고 실행
    options.add_argument("--no-sandbox") # CI(리눅스 환경)에서 권한 문제 방지
    options.add_argument("--disable-dev-shm-usage") # CI 환경에서 메모리 부족 문제 방지
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    # ChromeDriver 설치
    driver.implicitly_wait(10)
    yield driver
    driver.quit()
    
# 테스트 실패 시 스크린샷 저장
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    
    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver")
        if driver:
            allure.attach(
                driver.get_screenshot_as_png(),
                name = "실패 스크린샷",
                attachment_type = allure.attachment_type.PNG
            )
            