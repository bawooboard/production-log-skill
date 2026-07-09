# Production Log Skill

[![Python tests](https://github.com/bawooboard/production-log-skill/actions/workflows/python.yml/badge.svg)](https://github.com/bawooboard/production-log-skill/actions/workflows/python.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.9%2B-blue.svg)](https://www.python.org/)

생산 현장의 **품목, 수량, 양품, 불량** 정보를 관리하고, 생산일보를 출력할 수 있는 오픈소스 Python 스킬과 테스트 하네스입니다.

- Version: 1.0.0
- Python: 3.9+
- License: MIT
- Storage: CSV
- Repository: <https://github.com/bawooboard/production-log-skill>

---

## 1. 주요 기능

1. **생산일지 등록**  
   날짜, 품목, 총수량, 양품, 불량 정보를 CSV에 저장합니다.

2. **생산일지 조회**  
   전체 생산일지를 조회하거나 날짜/품목 기준으로 필터링합니다.

3. **품목별 집계**  
   품목별 총 생산수량, 양품수량, 불량수량, 양품률, 불량률을 계산합니다.

4. **생산일보 출력**  
   특정 날짜 또는 전체 기간의 생산일보 요약을 출력합니다.

5. **수량 검증**  
   `수량 = 양품 + 불량` 규칙을 자동 검증합니다.

6. **CSV 저장**  
   별도 DB 없이 CSV 파일로 데이터를 저장합니다.

7. **CLI 지원**  
   터미널에서 `production-log` 명령어로 사용할 수 있습니다.

8. **Python API 지원**  
   Python 코드에서 `ProductionLogSkill` 클래스를 import해서 사용할 수 있습니다.

9. **하네스 제공**  
   설치 후 기능이 정상 동작하는지 `harness/run_harness.py`로 검증할 수 있습니다.

---

## 2. 설치 및 연결 전체 흐름

이 프로젝트는 세 가지 방식으로 사용할 수 있습니다.

1. **CLI 연결**  
   맥북/윈도우/리눅스 터미널에서 `production-log ...` 명령어로 직접 실행합니다.

2. **Python 코드 연결**  
   다른 Python 프로그램에서 `ProductionLogSkill`을 import해서 사용합니다.

3. **LLM/에이전트 연결**  
   ChatGPT, Claude, Gemini, Cursor, Codex CLI 같은 LLM/에이전트가 이 패키지의 Python API 또는 CLI를 호출하도록 연결합니다.

> 중요: `/production-log-skill 생산일보 출력해줘` 같은 문장은 **터미널 명령어가 아니라 LLM/챗봇에서 사용할 예시 프롬프트**입니다.  
> 실제 동작하려면 LLM 환경에서 이 패키지 또는 CLI를 Tool, Function Calling, MCP, 로컬 에이전트 등으로 연결해야 합니다.

---

## 3. GitHub에 오픈소스로 배포하는 방법

### 3.1 압축 해제 후 폴더 이동

```bash
unzip production-log-skill.zip
cd production-log-skill
```

### 3.2 로컬 Git 저장소 생성

```bash
git init
git add .
git commit -m "Initial release v1.0.0"
```

### 3.3 GitHub에서 Public 저장소 생성

GitHub에서 public repository를 만듭니다.

예시 저장소 이름:

```text
production-log-skill
```

### 3.4 GitHub 주소 연결 후 push

`YOUR_GITHUB_ID`를 본인 GitHub 아이디로 바꿔 실행하세요.

```bash
git branch -M main
git remote add origin https://github.com/YOUR_GITHUB_ID/production-log-skill.git
git push -u origin main
```

### 3.5 GitHub CLI로 한 번에 Public 저장소 생성

GitHub CLI를 쓰면 더 간단합니다.

```bash
brew install gh
gh auth login
```

프로젝트 폴더에서 실행합니다.

```bash
git init
git add .
git commit -m "Initial release v1.0.0"
gh repo create production-log-skill --public --source=. --remote=origin --push
```

---

## 4. 다른 사람이 GitHub 주소로 설치하는 방법

### 4.1 pip로 바로 설치

```bash
pip install git+https://github.com/YOUR_GITHUB_ID/production-log-skill.git
```

설치 확인:

```bash
production-log --help
```

### 4.2 clone 후 개발 모드로 설치

```bash
git clone https://github.com/YOUR_GITHUB_ID/production-log-skill.git
cd production-log-skill
pip install -e .
```

### 4.3 로컬 압축파일에서 설치

GitHub에 올리기 전, 다운로드한 압축파일을 맥북에서 테스트하려면 다음처럼 합니다.

```bash
unzip production-log-skill.zip
cd production-log-skill
python3 -m venv .venv
source .venv/bin/activate
pip install -e .
production-log --help
```

---

## 5. CLI 사용법

CLI는 실제 터미널에서 실행하는 방식입니다.

### 5.1 생산일지 등록

간략 설명: 생산일자, 품목, 총수량, 양품, 불량을 등록합니다.

```bash
production-log add \
  --date 2026-07-09 \
  --item A-100 \
  --quantity 100 \
  --good 97 \
  --defect 3
```

### 5.2 전체 생산일지 조회

간략 설명: 저장된 모든 생산일지를 조회합니다.

```bash
production-log list
```

### 5.3 날짜별 생산일지 조회

간략 설명: 특정 날짜의 생산일지만 조회합니다.

```bash
production-log list --date 2026-07-09
```

### 5.4 품목별 생산일지 조회

간략 설명: 특정 품목의 생산일지만 조회합니다.

```bash
production-log list --item A-100
```

### 5.5 품목별 집계

간략 설명: 품목별 총수량, 양품, 불량, 양품률, 불량률을 집계합니다.

```bash
production-log summary
```

### 5.6 생산일보 출력

간략 설명: 특정 날짜의 생산일보를 JSON 형태로 출력합니다.

```bash
production-log report --date 2026-07-09
```

전체 기간 생산일보를 출력하려면 날짜를 생략합니다.

```bash
production-log report
```

### 5.7 CSV 저장 위치 지정

간략 설명: 기본 파일이 아닌 원하는 CSV 경로에 저장합니다.

```bash
production-log --db data/my_production_log.csv add \
  --date 2026-07-09 \
  --item B-200 \
  --quantity 250 \
  --good 245 \
  --defect 5
```

---

## 6. Python 코드에서 스킬 불러서 사용하는 방법

### 6.1 스킬 초기화

```python
from production_log_skill import ProductionLogSkill

skill = ProductionLogSkill(storage_path="production_log.csv")
```

### 6.2 생산일지 등록

```python
result = skill.add_record({
    "date": "2026-07-09",
    "item": "A-100",
    "quantity": 100,
    "good": 97,
    "defect": 3,
})

print(result)
```

### 6.3 생산일지 조회

```python
records = skill.list_records()
print(records)
```

### 6.4 품목별 집계

```python
summary = skill.summary_by_item()
print(summary)
```

### 6.5 생산일보 출력

```python
report = skill.daily_report(date="2026-07-09")
print(report)
```

---

## 7. 하네스를 불러서 사용하는 방법

하네스는 설치된 스킬이 정상 작동하는지 검증하는 실행 파일입니다.

### 7.1 하네스 실행

```bash
python harness/run_harness.py
```

정상 실행되면 마지막에 아래 메시지가 출력됩니다.

```text
✅ 하네스 테스트 통과
```

### 7.2 하네스가 검증하는 기능

1. **정상 생산일지 등록**  
   올바른 입력값이 저장되는지 확인합니다.

2. **수량 검증 실패 처리**  
   `수량 != 양품 + 불량`인 경우 실패 처리되는지 확인합니다.

3. **전체 조회**  
   등록된 생산일지를 조회할 수 있는지 확인합니다.

4. **품목별 집계**  
   품목 기준으로 총수량, 양품, 불량이 집계되는지 확인합니다.

5. **생산일보 출력**  
   날짜별 생산일보가 출력되는지 확인합니다.

---

## 8. LLM 사이트에서 하네스 스킬처럼 사용하는 방법

LLM 사이트, 사내 챗봇, 로컬 에이전트 환경에서는 아래처럼 자연어 명령으로 사용할 수 있게 연결할 수 있습니다.

### 8.1 기능별 프롬프트 예시

1. **생산일지 등록**  
   간략 설명: 날짜, 품목, 수량, 양품, 불량 정보를 등록합니다.

```text
/production-log-skill 생산일지 등록해줘. 날짜 2026-07-09, 품목 A-100, 수량 100, 양품 97, 불량 3
```

2. **전체 생산일지 조회**  
   간략 설명: 저장된 생산일지 전체를 조회합니다.

```text
/production-log-skill 전체 생산일지 조회해줘
```

3. **날짜별 생산일지 조회**  
   간략 설명: 특정 날짜의 생산일지만 조회합니다.

```text
/production-log-skill 2026-07-09 생산일지 조회해줘
```

4. **품목별 생산일지 조회**  
   간략 설명: 특정 품목의 생산 이력을 조회합니다.

```text
/production-log-skill A-100 품목 생산일지 조회해줘
```

5. **품목별 집계**  
   간략 설명: 품목별 총수량, 양품, 불량, 불량률을 집계합니다.

```text
/production-log-skill 품목별 집계해줘
```

6. **생산일보 출력**  
   간략 설명: 특정 날짜 또는 전체 기간 생산일보를 출력합니다.

```text
/production-log-skill 생산일보 출력해줘
```

```text
/production-log-skill 2026-07-09 생산일보 출력해줘
```

7. **불량률 계산**  
   간략 설명: 등록된 생산일지 기준으로 불량률을 계산합니다.

```text
/production-log-skill 불량률 계산해줘
```

8. **CSV 저장 위치 지정**  
   간략 설명: 원하는 CSV 파일에 생산일지를 저장하도록 요청합니다.

```text
/production-log-skill data/my_production_log.csv 파일에 생산일지 저장해줘
```

### 8.2 실제로 이렇게 사용하는 것이 맞나요?

정리하면 다음과 같습니다.

1. **CLI에서 직접 사용**  
   실제 컴퓨터 터미널에서는 `production-log ...` 명령어를 사용합니다.

2. **Python 코드에서 사용**  
   프로그램 내부에서는 `ProductionLogSkill` 클래스를 import해서 사용합니다.

3. **LLM 사이트에서 사용**  
   `/production-log-skill 생산일보 출력해줘` 같은 문장은 프롬프트입니다.  
   이 문장이 실제로 작동하려면 LLM 사이트나 에이전트가 이 Python 패키지 또는 CLI 명령어를 호출하도록 별도 연결되어 있어야 합니다.

4. **하네스 실행**  
   하네스는 기능 검증용입니다. 실제 업무 입력용 명령어라기보다는 설치 후 정상 동작 확인용입니다.

---

## 9. Claude Code / Codex CLI로 GitHub에 올리는 방법

맥북에서 압축파일을 풀고 프로젝트 폴더로 이동한 뒤, Claude Code나 Codex CLI 같은 로컬 에이전트에게 아래처럼 요청하면 됩니다.

```text
이 폴더를 GitHub public repository로 등록해줘.
저장소 이름은 production-log-skill로 해줘.
git init, initial commit, gh repo create, git push까지 진행해줘.
README의 GitHub 주소는 내 GitHub 아이디에 맞게 수정해줘.
```

로컬 에이전트가 실제로 실행할 대표 명령은 다음과 같습니다.

```bash
git init
git add .
git commit -m "Initial release v1.0.0"
gh repo create production-log-skill --public --source=. --remote=origin --push
```

필요 조건:

```bash
git --version
gh --version
```

GitHub CLI 로그인이 필요하면 다음을 먼저 실행합니다.

```bash
gh auth login
```

---

## 10. LLM/에이전트에 연결하는 기본 방식

### 10.1 CLI 호출 방식

가장 단순한 연결 방식입니다. LLM 또는 로컬 에이전트가 아래 CLI 명령을 실행하도록 연결합니다.

```bash
production-log report --date 2026-07-09
```

### 10.2 Python Function Calling 방식

LLM Tool 또는 Function Calling에서 내부적으로 아래 Python 함수를 호출하도록 연결할 수 있습니다.

```python
from production_log_skill import ProductionLogSkill

skill = ProductionLogSkill("production_log.csv")
result = skill.daily_report(date="2026-07-09")
```

### 10.3 MCP 연결 방식

MCP를 지원하는 환경에서는 별도의 MCP 서버 래퍼를 만들어 이 패키지의 Python API를 호출하도록 연결할 수 있습니다.

예시 구조:

```text
LLM → MCP 서버 → ProductionLogSkill → CSV 저장소
```

예시 설정:

```json
{
  "mcpServers": {
    "production-log-skill": {
      "command": "python",
      "args": [
        "-m",
        "your_mcp_wrapper_for_production_log"
      ]
    }
  }
}
```

> 참고: 위 MCP 설정은 연결 방식 예시입니다. 실제 MCP 서버 파일명과 실행 명령은 사용하는 MCP SDK와 환경에 맞게 작성해야 합니다.

---

## 11. pytest 테스트 실행

개발자가 자동 테스트를 실행하려면 아래처럼 합니다.

```bash
pip install pytest
pytest
```

---

## 12. 데이터 검증 규칙

입력 데이터는 아래 조건을 만족해야 합니다.

```text
수량 = 양품 + 불량
수량 >= 0
양품 >= 0
불량 >= 0
품목은 빈 값이 아니어야 함
날짜는 YYYY-MM-DD 형식이어야 함
```

잘못된 예:

```json
{
  "date": "2026-07-09",
  "item": "A-100",
  "quantity": 100,
  "good": 95,
  "defect": 10
}
```

결과:

```json
{
  "success": false,
  "message": "총수량과 양품+불량 수량이 일치하지 않습니다."
}
```

---

## 13. 실행 예시

```text
$ production-log report --date 2026-07-09

{
  "success": true,
  "date": "2026-07-09",
  "total_quantity": 350,
  "total_good": 342,
  "total_defect": 8,
  "defect_rate": 2.29,
  "yield_rate": 97.71,
  "records": [...]
}
```

---

## 14. Roadmap

- [x] CSV 저장
- [x] CLI
- [x] Python API
- [x] 테스트 하네스
- [x] 생산일보 출력
- [ ] SQLite 지원
- [ ] Excel Export
- [ ] PDF 생산일보 출력
- [ ] REST API
- [ ] Docker 지원
- [ ] Web UI
- [ ] MCP 서버 지원

---

## 15. Contributing

Pull Request를 환영합니다.

1. Fork
2. Branch 생성
3. Commit
4. Push
5. Pull Request 생성

---

## 16. License

MIT License
