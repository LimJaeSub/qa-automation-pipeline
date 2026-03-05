# QA Automation Pipeline

![CI](https://github.com/LimJaeSub/qa-automation-pipeline/actions/workflows/ci.yml/badge.svg)

Selenium + Python 기반 UI 자동화 테스트 프로젝트입니다.  
GitHub Actions CI/CD 파이프라인과 Allure 리포트 자동 배포를 포함합니다.

---

## 기술 스택

| 분류 | 기술 |
|------|------|
| 언어 | Python 3.11 |
| 자동화 | Selenium, pytest |
| 리포트 | Allure Report |
| CI/CD | GitHub Actions |
| 배포 | GitHub Pages |

---

## 폴더 구조

```
qa-automation-pipeline/
├── pages/
│   ├── base_page.py       # 공통 메서드 (find, click, type)
│   ├── login_page.py      # 로그인 페이지 POM
│   └── search_page.py     # 상품 검색 페이지 POM
├── tests/
│   ├── test_login.py      # 로그인 테스트
│   └── test_search.py     # 상품 검색 테스트
├── conftest.py            # Selenium 드라이버 설정, 실패 시 스크린샷 자동 첨부
├── pytest.ini             # pytest 설정
├── requirements.txt       # 의존성 목록
└── .github/workflows/
    └── ci.yml             # GitHub Actions 파이프라인
```

---

## 테스트 시나리오

| Epic | Feature | 시나리오 | 중요도 |
|------|---------|---------|--------|
| 사용자 인증 | 로그인 | 정상 로그인 | CRITICAL |
| 사용자 인증 | 로그인 | 잘못된 비밀번호로 로그인 시도 | NORMAL |
| 상품 | 상품 검색 | 유효한 키워드 검색 | NORMAL |
| 상품 | 상품 검색 | 존재하지 않는 키워드 검색 | MINOR |

---

## 실행 방법

```bash
# 의존성 설치
pip install -r requirements.txt

# 테스트 실행
pytest

# Allure 리포트 로컬 확인
allure serve allure-results
```

---

## Allure 리포트

🔗 [GitHub Pages에서 리포트 확인](https://LimJaeSub.github.io/qa-automation-pipeline/)