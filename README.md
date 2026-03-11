# QA Automation Pipeline

![CI](https://github.com/LimJaeSub/qa-automation-pipeline/actions/workflows/ci.yml/badge.svg)

Selenium + Python 기반 UI/API 자동화 테스트 프로젝트입니다.  
GitHub Actions CI/CD 파이프라인, Allure 리포트 자동 배포, Jira 스프린트 운영, Confluence 문서화를 포함합니다.

---

## 기술 스택

| 분류 | 기술 |
|------|------|
| 언어 | Python 3.11 |
| UI 자동화 | Selenium, pytest |
| API 자동화 | requests |
| 성능 테스트 | Apache JMeter |
| 리포트 | Allure Report |
| CI/CD | GitHub Actions |
| 배포 | GitHub Pages |
| 이슈 관리 | Jira (Scrum) |
| 문서화 | Confluence |

---

## 폴더 구조

```
qa-automation-pipeline/
├── pages/
│   ├── base_page.py           # 공통 메서드 (find, click, type)
│   ├── login_page.py          # 로그인 페이지 POM
│   └── search_page.py         # 상품 검색 페이지 POM
├── tests/
│   ├── ui/
│   │   ├── test_login.py      # 로그인 테스트
│   │   └── test_search.py     # 상품 검색 테스트
│   └── api/
│       ├── test_api_products.py  # 상품 API 테스트
│       ├── test_api_login.py     # 로그인 API 테스트
│       └── test_api_user.py      # 회원 CRUD API 테스트
├── conftest.py                # Selenium 드라이버 설정, 실패 시 스크린샷 자동 첨부
├── pytest.ini                 # pytest 설정
├── requirements.txt           # 의존성 목록
└── .github/workflows/
    └── ci.yml                 # GitHub Actions 파이프라인
```

---

## 테스트 시나리오

### UI 테스트 (Selenium)

| Epic | Feature | 시나리오 | 중요도 | 상태 |
|------|---------|---------|--------|------|
| 사용자 인증 | 로그인 | 정상 로그인 | CRITICAL | ✅ Pass |
| 사용자 인증 | 로그인 | 잘못된 비밀번호로 로그인 시도 | NORMAL | ✅ Pass |
| 상품 | 상품 검색 | 유효한 키워드 검색 | NORMAL | ✅ Pass |
| 상품 | 상품 검색 | 존재하지 않는 키워드 검색 결과 0개 확인 | MINOR | ✅ Pass |
| 상품 | 상품 검색 | 검색 결과 없을 때 안내 문구 표시 확인 | MINOR | ⚠️ xfail (SCRUM-26) |

### API 테스트 (requests)

| Epic | Feature | 시나리오 | 상태 |
|------|---------|---------|------|
| 상품 | 상품 조회 | 전체 상품 목록 조회 | ✅ Pass |
| 상품 | 상품 조회 | 단일 상품 조회 | ✅ Pass |
| 상품 | 상품 조회 | 잘못된 HTTP 메서드 요청 | ✅ Pass |
| 사용자 인증 | 로그인 | 정상 로그인 API | ✅ Pass |
| 사용자 인증 | 로그인 | 잘못된 비밀번호 로그인 | ✅ Pass |
| 사용자 인증 | 로그인 | 파라미터 누락 요청 | ✅ Pass |
| 회원관리 | 회원 CRUD | 회원 가입 | ✅ Pass |
| 회원관리 | 회원 CRUD | 회원 정보 수정 | ✅ Pass |
| 회원관리 | 회원 CRUD | 회원 삭제 | ✅ Pass |
| 회원관리 | 회원 CRUD | 중복 회원 가입 | ✅ Pass |
| 회원관리 | 회원 CRUD | 파라미터 누락 요청 | ✅ Pass |

---

## Jira 스프린트 운영

Jira Scrum 프로젝트(QAP)를 활용하여 스프린트 기반 이슈 관리를 진행했습니다.

| 스프린트 | 목표 | 내용 |
|---------|------|------|
| Sprint 1 | 자동화 파이프라인 구축 | UI/API 자동화 TC 15개 작성 + CI/CD 구성 |
| Sprint 2 | 탐색적 테스트 + 자동화 보강 | 수동 탐색 중 버그 발견(SCRUM-26) → 자동화 TC 추가(SCRUM-27) |

> 수동 탐색 테스트에서 발견한 버그를 Jira에 등록하고, 회귀 방지를 위해 자동화 TC로 추가하는 프로세스를 적용했습니다.

---

## 실행 방법

```bash
# 의존성 설치
pip install -r requirements.txt

# 전체 테스트 실행
pytest

# Allure 리포트 로컬 확인
allure serve allure-results
```

---

## Allure 리포트

🔗 [GitHub Pages에서 리포트 확인](https://LimJaeSub.github.io/qa-automation-pipeline/)

---

## Confluence 문서

📄 [Sprint 1 테스트 계획서](https://wotjw734843-1772693672178.atlassian.net/wiki/spaces/QAP/pages/327792)