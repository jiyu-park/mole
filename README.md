# 두더지 굴착단

무너진 굴을 떠난 두더지 가족이 새 보금자리를 찾아가는 Streamlit 선택형 모험 게임입니다.

## 실행 방법

```bash
pip install -r requirements.txt
streamlit run app.py
```

## OpenAI 사용

OpenAI API 키가 있으면 선택 결과와 힌트가 AI 게임 마스터의 문장으로 생성됩니다.

PowerShell 예시:

```powershell
$env:OPENAI_API_KEY="your_api_key"
streamlit run app.py
```

API 키가 없어도 기본 스토리 문장으로 게임을 플레이할 수 있습니다.

## 게임 구조

- 사용자는 매 장면 2~3개의 행동 중 하나를 선택합니다.
- 선택에 따라 `가족 유대감`, `탐험 지식`, `안전 감각` 중 하나가 상승합니다.
- 마지막에는 가장 높은 스탯에 따라 `따뜻한 굴`, `넓은 굴`, `안전한 굴` 중 하나의 엔딩이 표시됩니다.
- 힌트는 최대 3회까지 사용할 수 있습니다.
