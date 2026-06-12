import base64
from textwrap import dedent
from pathlib import Path

import streamlit as st


BASE_DIR = Path(__file__).parent
ASSET_DIR = BASE_DIR / "assets"

STAT_LABELS = {
    "bond": "가족 유대감",
    "knowledge": "탐험 지식",
    "safety": "안전 감각",
}

ENDING_BY_STAT = {
    "bond": {
        "title": "따뜻한 굴",
        "image": ASSET_DIR / "ending-warm-burrow.png",
        "quote": "집은 크기가 아니라 함께 있는 온기였구나.",
        "body": (
            "가족은 이끼가 부드럽게 깔린 작고 포근한 굴에 도착했습니다. "
            "수프 냄새가 다시 피어오르고, 아기 두더지는 도토리 가방을 베개 삼아 잠이 듭니다. "
            "무너진 굴을 떠나왔지만, 가족은 서로를 잃지 않았습니다."
        ),
    },
    "knowledge": {
        "title": "넓은 굴",
        "image": ASSET_DIR / "ending-wide-burrow.png",
        "quote": "여긴 우리가 다시 시작하기에 충분히 넓다.",
        "body": (
            "할아버지의 굴착일지를 따라간 가족은 여러 갈래 터널이 이어진 넓은 지하 광장에 도착했습니다. "
            "도토리 창고, 버섯밭, 아기 두더지의 놀이 터널까지 만들 수 있는 곳입니다. "
            "이곳은 새로운 두더지 마을의 시작이 될지도 모릅니다."
        ),
    },
    "safety": {
        "title": "안전한 굴",
        "image": ASSET_DIR / "ending-safe-burrow.png",
        "quote": "여긴 흔들려도 무섭지 않아.",
        "body": (
            "가족은 단단한 흙벽과 자연 배수로가 있는 안정적인 굴에 도착했습니다. "
            "위쪽의 진동은 거의 느껴지지 않고, 비가 와도 물이 고이지 않습니다. "
            "아빠 두더지는 벽을 두드려보고 조용히 고개를 끄덕입니다."
        ),
    },
}

SCENES = [
    {
        "name": "무너진 식탁굴",
        "story": (
            "아빠 두더지는 구운 버섯을 나누고, 엄마 두더지는 도토리 수프를 젓고, "
            "아기 두더지는 흙감자 하나를 몰래 숨기고 있었습니다. 그때 굴 전체가 흔들립니다. "
            "천장에서 흙가루가 쏟아지고, 식탁 옆 벽이 무너져 내립니다.\n\n"
            "흙더미 속에서 낡은 가죽 표지의 책이 발견됩니다. 아기 두더지가 책 위의 흙을 털어내자 "
            "익숙한 냄새가 퍼집니다. 할아버지 두더지가 쓰던 오래된 굴착일지입니다.\n\n"
            "책 첫 장에는 이렇게 적혀 있습니다.\n\n"
            "“언젠가 위쪽 세계가 땅을 깨우면,\n"
            "오래된 굴은 집이 아니라 덫이 된다.\n"
            "그때는 바람이 흐르는 길을 찾아라.\n"
            "따뜻한 이끼 언덕으로 가야 한다.”"
        ),
        "clue": "할아버지의 굴착일지",
        "hint": "첫 선택은 정답 찾기보다 가족이 어떤 방식으로 위기를 받아들이는지 정하는 장면입니다.",
        "choices": [
            {
                "label": "가족이 다치지 않았는지 먼저 확인한다",
                "stat": "bond",
                "fallback": (
                    "엄마 두더지가 아기 두더지를 꼭 안고, 아빠 두더지가 모두의 손을 확인합니다. "
                    "가족은 겁에 질렸지만 서로가 무사하다는 사실에 힘을 얻습니다."
                ),
                "clue": "서로의 체온",
            },
            {
                "label": "할아버지의 굴착일지를 자세히 읽는다",
                "stat": "knowledge",
                "fallback": (
                    "엄마 두더지가 랜턴을 가까이 들고 책장을 넘깁니다. "
                    "낡은 지도에는 오래된 뿌리길과 바람구멍 표시가 희미하게 남아 있습니다."
                ),
                "clue": "낡은 뿌리 지도",
            },
            {
                "label": "천장과 벽의 균열을 살펴본다",
                "stat": "safety",
                "fallback": (
                    "아빠 두더지가 삽 끝으로 벽을 두드려봅니다. "
                    "왼쪽 천장은 약하지만 오른쪽 벽틈에서는 차가운 바람이 새어 나옵니다."
                ),
                "clue": "바람이 새는 벽틈",
            },
        ],
    },
    {
        "name": "뿌리 미로",
        "story": (
            "무너진 식탁굴을 빠져나오자 거대한 나무뿌리들이 터널 전체를 가로막고 있습니다. "
            "어떤 뿌리는 계단처럼 보이고, 어떤 뿌리는 오래된 문처럼 얽혀 있습니다. "
            "굴착일지에는 짧은 문장이 적혀 있습니다.\n\n"
            "“뿌리는 길을 막지 않는다. 오래된 나무는 길을 기억한다.”"
        ),
        "clue": "뿌리 미로의 문장",
        "hint": "뿌리 미로에서는 지도, 가족의 감각, 안전한 우회 중 무엇을 믿을지 고르면 됩니다.",
        "choices": [
            {
                "label": "엄마 두더지와 지도와 뿌리 모양을 비교한다",
                "stat": "knowledge",
                "fallback": (
                    "엄마 두더지가 지도 위에 뿌리 그림자를 겹쳐 봅니다. "
                    "가장 오래된 뿌리 아래에 숨은 통로 표시가 있다는 걸 알아냅니다."
                ),
                "clue": "오래된 뿌리 아래 통로",
            },
            {
                "label": "아기 두더지에게 냄새가 다른 뿌리를 찾아보게 한다",
                "stat": "bond",
                "fallback": (
                    "아기 두더지가 코를 씰룩이며 앞장섭니다. "
                    "가족은 아기의 작은 발견을 믿고 조심스럽게 뒤따릅니다."
                ),
                "clue": "달콤한 뿌리 냄새",
            },
            {
                "label": "흙이 덜 무른 쪽으로 천천히 우회한다",
                "stat": "safety",
                "fallback": (
                    "아빠 두더지가 바닥을 눌러보며 단단한 흙길을 고릅니다. "
                    "시간은 더 걸렸지만 천장이 흔들리지 않는 길을 찾았습니다."
                ),
                "clue": "단단한 우회로",
            },
        ],
    },
    {
        "name": "지하수 울림길",
        "story": (
            "터널 아래쪽에서 물방울 소리가 점점 커집니다. "
            "차가운 바람이 발밑을 스치고, 진흙은 발목까지 들러붙습니다. "
            "굴착일지 가장자리에는 물에 번진 글씨가 남아 있습니다.\n\n"
            "“물은 낮은 곳을 기억한다. 살아남으려면 물보다 먼저 길을 골라라.”"
        ),
        "clue": "물에 번진 경고문",
        "hint": "물이 있는 구역에서는 빠르게 가는 길보다 왜 그 길을 고르는지가 중요합니다.",
        "choices": [
            {
                "label": "가족이 한 줄로 손을 잡고 천천히 이동한다",
                "stat": "bond",
                "fallback": (
                    "가족은 서로의 손을 놓지 않고 진흙길을 건넙니다. "
                    "아기 두더지가 미끄러질 때마다 아빠와 엄마가 번갈아 잡아줍니다."
                ),
                "clue": "놓치지 않은 손",
            },
            {
                "label": "책에 적힌 물길 표시를 따라 마른 길을 찾는다",
                "stat": "knowledge",
                "fallback": (
                    "엄마 두더지가 번진 글씨를 해석합니다. "
                    "물소리가 크게 울리는 곳이 아니라, 소리가 끊기는 곳에 마른 길이 있었습니다."
                ),
                "clue": "소리가 끊기는 마른 길",
            },
            {
                "label": "천장 높이와 배수 방향을 먼저 확인한다",
                "stat": "safety",
                "fallback": (
                    "아빠 두더지가 천장 높이와 물의 흐름을 확인합니다. "
                    "가족은 물이 갑자기 차올라도 빠져나갈 수 있는 높은 통로를 선택합니다."
                ),
                "clue": "높은 배수 통로",
            },
        ],
    },
    {
        "name": "인간 정원 아래",
        "story": (
            "위쪽에서 둔탁한 발소리와 금속 삽 소리가 들립니다. "
            "흙벽 사이로 밝은 빛이 한 줄기 새어 들어오고, 터널은 불규칙하게 흔들립니다. "
            "아기 두더지는 도토리 가방을 꼭 끌어안고 묻습니다.\n\n"
            "“대장, 우리 정말 새 집에 갈 수 있어?”"
        ),
        "clue": "위쪽 세계의 진동",
        "hint": "마지막 선택 전 장면입니다. 어떤 태도로 위기를 통과할지 고르면 엔딩 성향이 더 분명해집니다.",
        "choices": [
            {
                "label": "아기 두더지를 안심시키고 모두 잠시 숨을 고른다",
                "stat": "bond",
                "fallback": (
                    "엄마 두더지가 작은 노래를 부르고, 아빠 두더지가 아기 두더지의 가방끈을 고쳐줍니다. "
                    "가족은 다시 함께 움직일 용기를 얻습니다."
                ),
                "clue": "다시 얻은 용기",
            },
            {
                "label": "할아버지 일지의 마지막 지도를 펼쳐 길을 계산한다",
                "stat": "knowledge",
                "fallback": (
                    "굴착일지의 마지막 장에는 인간 정원 아래를 피하는 곡선 통로가 그려져 있었습니다. "
                    "가족은 가장 넓은 지하 공간으로 이어지는 길을 찾아냅니다."
                ),
                "clue": "마지막 곡선 지도",
            },
            {
                "label": "삽 소리가 멈출 때까지 기다렸다가 이동한다",
                "stat": "safety",
                "fallback": (
                    "가족은 어둠 속에서 조용히 기다립니다. "
                    "위쪽이 잠잠해진 뒤 움직이자, 흔들림 없는 단단한 길이 드러납니다."
                ),
                "clue": "흔들림 없는 길",
            },
        ],
    },
]


def get_api_key() -> str | None:
    # OpenAI 사용 준비: 방문자가 화면에 직접 입력한 API 키만 사용합니다.
    # Streamlit Cloud Secrets나 서버 환경변수를 자동으로 쓰지 않아 배포자 키가 소모되지 않습니다.
    key = st.session_state.get("user_api_key", "")
    if not key or key.strip() in {"your_api_key_here", "your_api_key", "..."}:
        return None
    return key.strip()


def image_data_uri(path: Path) -> str:
    encoded = base64.b64encode(path.read_bytes()).decode("ascii")
    return f"data:image/png;base64,{encoded}"


def generate_ai_result(scene: dict, choice: dict) -> str:
    # AI 사용 지점 1: 사용자가 선택지를 누른 뒤, 선택 결과와 가족 대사를 OpenAI가 동적으로 생성합니다.
    api_key = get_api_key()
    if not api_key or not st.session_state.use_ai:
        # API 키가 없거나 AI 기능을 끄면 미리 준비한 기본 문장으로 진행합니다.
        return choice["fallback"]

    try:
        from openai import OpenAI

        client = OpenAI(api_key=api_key)
        stats_text = ", ".join(
            f"{STAT_LABELS[key]} {value}" for key, value in st.session_state.stats.items()
        )
        clues_text = ", ".join(st.session_state.clues[-5:])
        prompt = f"""
너는 한국어 동화형 방탈출 게임의 AI 게임 마스터다.
세계관: 두더지 가족이 무너진 굴을 떠나 새 보금자리를 찾아가는 지하 굴착 생존 모험.
등장인물은 아빠 두더지, 엄마 두더지, 아기 두더지 셋뿐이다.

현재 구역: {scene["name"]}
현재 장면 요약: {scene["story"]}
유저 선택: {choice["label"]}
상승 스탯: {STAT_LABELS[choice["stat"]]}
획득 단서: {choice["clue"]}
현재 스탯: {stats_text}
최근 단서: {clues_text}

요청:
- 선택 결과를 4~6문장으로 생생하게 써라.
- 아빠/엄마/아기 두더지 중 최소 2명의 짧은 대사를 넣어라.
- 무섭거나 잔인하지 않게, 따뜻한 모험 분위기로 써라.
- 이야기는 반드시 앞으로 진행되어야 하며 실패/죽음/게임오버로 끝내지 마라.
- 마지막 줄은 "[단서 획득: {choice["clue"]}]" 형식으로 끝내라.
- 마크다운 제목은 쓰지 마라.
""".strip()

        response = client.chat.completions.create(
            model=st.session_state.model_name,
            messages=[
                {
                    "role": "system",
                    "content": "너는 따뜻하고 재치 있는 한국어 AI 게임 마스터다. 출력은 게임 본문만 작성한다.",
                },
                {"role": "user", "content": prompt},
            ],
            temperature=0.85,
            max_tokens=450,
        )
        return response.choices[0].message.content.strip()
    except Exception as exc:
        st.warning(f"AI 응답 생성에 실패해서 기본 스토리로 진행합니다: {exc}")
        return choice["fallback"]


def generate_ai_hint(scene: dict) -> str:
    # AI 사용 지점 2: 힌트 버튼을 누르면 현재 구역과 선택지를 바탕으로 OpenAI가 힌트를 생성합니다.
    api_key = get_api_key()
    if not api_key or not st.session_state.use_ai:
        # API 키가 없거나 AI 기능을 끄면 기본 힌트를 보여줍니다.
        return scene["hint"]

    try:
        from openai import OpenAI

        client = OpenAI(api_key=api_key)
        prompt = f"""
현재 구역은 "{scene["name"]}"이다.
장면 내용: {scene["story"]}
선택지: {", ".join(choice["label"] for choice in scene["choices"])}

두더지 가족 중 한 명이 말하는 힌트를 2문장으로 써라.
정답을 직접 말하지 말고, 유저가 선택의 성향을 이해하도록 도와라.
따뜻하고 귀엽게 써라.
""".strip()

        response = client.chat.completions.create(
            model=st.session_state.model_name,
            messages=[
                {"role": "system", "content": "너는 한국어 방탈출 게임의 힌트 담당 두더지다."},
                {"role": "user", "content": prompt},
            ],
            temperature=0.7,
            max_tokens=180,
        )
        return response.choices[0].message.content.strip()
    except Exception as exc:
        st.warning(f"AI 힌트 생성에 실패해서 기본 힌트를 보여줍니다: {exc}")
        return scene["hint"]


def generate_ai_scene_intro(scene: dict) -> str:
    # AI 사용 지점 3: 각 구역에 들어갈 때 OpenAI가 현재 스탯과 단서를 반영한 현장 묘사를 생성합니다.
    api_key = get_api_key()
    if not api_key or not st.session_state.use_ai:
        return ""

    try:
        from openai import OpenAI

        client = OpenAI(api_key=api_key)
        stats_text = ", ".join(
            f"{STAT_LABELS[key]} {value}" for key, value in st.session_state.stats.items()
        )
        clues_text = ", ".join(st.session_state.clues[-5:])
        choices_text = ", ".join(choice["label"] for choice in scene["choices"])
        prompt = f"""
너는 한국어 동화형 방탈출 게임의 AI 게임 마스터다.
고정 세계관은 유지하되, 매 장면을 새롭게 살아 움직이는 현장 묘사로 확장한다.

현재 구역: {scene["name"]}
기본 장면: {scene["story"]}
현재 스탯: {stats_text}
보유 단서: {clues_text}
이번 장면 선택지: {choices_text}

요청:
- 3~5문장으로 현재 장면을 새롭게 묘사해라.
- 아빠 두더지, 엄마 두더지, 아기 두더지 중 1~2명의 짧은 대사를 넣어라.
- 선택지의 정답을 직접 알려주지 마라.
- 무섭거나 잔인하지 않게, 따뜻한 지하 모험 분위기로 써라.
- 마크다운 제목 없이 본문만 써라.
""".strip()

        response = client.chat.completions.create(
            model=st.session_state.model_name,
            messages=[
                {
                    "role": "system",
                    "content": "너는 따뜻하고 생동감 있는 한국어 AI 게임 마스터다.",
                },
                {"role": "user", "content": prompt},
            ],
            temperature=0.9,
            max_tokens=360,
        )
        return response.choices[0].message.content.strip()
    except Exception as exc:
        st.warning(f"AI 현장 묘사 생성에 실패했습니다: {exc}")
        return ""


def get_ai_scene_intro(scene: dict) -> str:
    # 같은 장면에서 API를 반복 호출하지 않도록, 한 번 생성한 AI 현장 묘사는 세션에 저장합니다.
    if not get_api_key() or not st.session_state.use_ai:
        return ""
    scene_index = st.session_state.scene_index
    if scene_index not in st.session_state.ai_scene_messages:
        st.session_state.ai_scene_messages[scene_index] = generate_ai_scene_intro(scene)
    return st.session_state.ai_scene_messages[scene_index]


def reset_game() -> None:
    st.session_state.scene_index = 0
    st.session_state.stats = {"bond": 0, "knowledge": 0, "safety": 0}
    st.session_state.clues = ["할아버지의 굴착일지"]
    st.session_state.log = []
    st.session_state.hints_used = 0
    st.session_state.hint_messages = {}
    st.session_state.ai_scene_messages = {}
    st.session_state.last_stat = None
    st.session_state.finished = False


def ensure_state() -> None:
    defaults = {
        "use_ai": True,
        "model_name": "gpt-4o-mini",
        "user_api_key": "",
        "api_key_input": "",
        "api_key_input_main": "",
    }
    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value
    if "scene_index" not in st.session_state:
        reset_game()


def add_clue(clue: str) -> None:
    if clue not in st.session_state.clues:
        st.session_state.clues.append(clue)


def choose_option(choice: dict) -> None:
    scene = SCENES[st.session_state.scene_index]
    stat = choice["stat"]
    st.session_state.stats[stat] += 1
    st.session_state.last_stat = stat
    add_clue(scene["clue"])
    add_clue(choice["clue"])

    # 선택 결과 문장은 OpenAI가 생성하며, 실패 시 fallback 문장을 사용합니다.
    result = generate_ai_result(scene, choice)
    st.session_state.log.append(
        {
            "scene": scene["name"],
            "choice": choice["label"],
            "result": result,
            "stat": STAT_LABELS[stat],
        }
    )

    if st.session_state.scene_index >= len(SCENES) - 1:
        st.session_state.finished = True
    else:
        st.session_state.scene_index += 1


def use_hint(scene: dict) -> None:
    if st.session_state.hints_used < 3:
        st.session_state.hints_used += 1
        # 힌트 문장도 OpenAI가 현재 장면을 보고 생성합니다.
        st.session_state.hint_messages[st.session_state.scene_index] = generate_ai_hint(scene)


def get_ending_key() -> str:
    stats = st.session_state.stats
    max_score = max(stats.values())
    winners = [key for key, value in stats.items() if value == max_score]
    if st.session_state.last_stat in winners:
        return st.session_state.last_stat
    return winners[0]


def opening_story_html() -> str:
    return (
        '<div class="scene-box opening-scene">'
        "<p>아빠 두더지는 구운 버섯을 나누고, 엄마 두더지는 도토리 수프를 젓고, "
        "아기 두더지는 흙감자 하나를 몰래 숨기고 있었습니다. 그때 굴 전체가 흔들립니다. "
        "천장에서 흙가루가 쏟아지고, 식탁 옆 벽이 무너져 내립니다.</p>"
        "<p>흙더미 속에서 낡은 가죽 표지의 책이 발견됩니다. 아기 두더지가 책 위의 흙을 털어내자 "
        "익숙한 냄새가 퍼집니다. 할아버지 두더지가 쓰던 오래된 굴착일지입니다.</p>"
        '<div class="opening-label">책 첫 장에는 이렇게 적혀 있습니다.</div>'
        '<div class="opening-quote">'
        '<span class="quote-nowrap">“언젠가 위쪽 세계가 땅을 깨우면,</span><br>'
        "오래된 굴은 집이 아니라 덫이 된다.<br>"
        "그때는 바람이 흐르는 길을 찾아라.<br>"
        "따뜻한 이끼 언덕으로 가야 한다.”"
        "</div>"
        "</div>"
    )


st.set_page_config(page_title="두더지 굴착단", page_icon="⛏️", layout="wide")
ensure_state()

st.markdown(
    """
    <style>
    .main .block-container {
        max-width: 1180px;
        padding-top: 28px;
    }
    .title {
        font-size: 40px;
        font-weight: 900;
        letter-spacing: 0;
        margin-bottom: 4px;
        color: #2b241b;
    }
    .subtitle {
        color: #665c4e;
        font-size: 17px;
        margin-bottom: 22px;
    }
    .scene-box {
        border: 1px solid #ded4c4;
        background: #fffaf1;
        border-radius: 8px;
        padding: 18px 20px;
        line-height: 1.72;
        color: #2d271f;
        white-space: pre-line;
        margin-bottom: 14px;
    }
    .opening-scene {
        white-space: normal;
        padding: 20px 22px;
        line-height: 1.62;
    }
    .opening-scene p {
        margin: 0 0 14px 0;
    }
    .opening-label {
        margin-top: 18px;
        margin-bottom: 10px;
        color: #5c4730;
        font-size: 20px;
        font-weight: 800;
    }
    .opening-quote {
        border-left: 6px solid #b97832;
        background: #fff3dc;
        border-radius: 8px;
        padding: 16px 18px;
        color: #2b2116;
        font-size: 25px;
        font-weight: 900;
        line-height: 1.45;
        word-break: keep-all;
        box-shadow: inset 0 0 0 1px rgba(185, 120, 50, 0.18);
    }
    .quote-nowrap {
        white-space: nowrap;
    }
    .result-box {
        border: 1px solid #cfd9c5;
        background: #f6fbf1;
        border-radius: 8px;
        padding: 14px 16px;
        margin-bottom: 12px;
        line-height: 1.6;
        color: #24301f;
        white-space: pre-line;
    }
    .result-box b {
        color: #2f4426;
    }
    .ai-box {
        border: 1px solid #c7d7e8;
        background: #f3f8ff;
        border-radius: 8px;
        padding: 15px 16px;
        margin: 12px 0 14px 0;
        line-height: 1.65;
        color: #243242;
        white-space: pre-line;
    }
    .ai-box-title {
        color: #2f5f8f;
        font-size: 14px;
        font-weight: 800;
        margin-bottom: 8px;
    }
    .api-login-note {
        border: 1px solid #34495e;
        background: #111820;
        border-radius: 8px;
        padding: 12px;
        color: #d8e3ec;
        font-size: 13px;
        line-height: 1.5;
        margin-bottom: 10px;
    }
    .api-login-main {
        border: 1px solid #3c526a;
        background: #101923;
        border-radius: 8px;
        padding: 16px 18px;
        margin: 0 0 20px 0;
        color: #e8f1f8;
    }
    .api-login-main-title {
        font-size: 18px;
        font-weight: 800;
        margin-bottom: 6px;
    }
    .api-login-main-body {
        color: #bfd0dd;
        font-size: 14px;
        line-height: 1.55;
    }
    .journal-frame img {
        border: 1px solid #d8c8ad;
        border-radius: 8px;
        box-shadow: 0 12px 26px rgba(74, 55, 32, 0.16);
        background: #fff7e8;
    }
    .journal-caption {
        color: #766c60;
        font-size: 13px;
        margin-top: 6px;
        text-align: center;
    }
    .small-note {
        color: #766c60;
        font-size: 14px;
    }
    div.stButton > button {
        min-height: 48px;
        white-space: normal;
        border-radius: 8px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

with st.sidebar:
    st.subheader("메인 스탯")
    for key, label in STAT_LABELS.items():
        st.progress(st.session_state.stats[key] / len(SCENES), text=f"{label}: {st.session_state.stats[key]}")

    st.divider()
    st.header("굴착 기록")
    if st.button("처음부터 다시", use_container_width=True):
        reset_game()
        st.rerun()

    st.divider()
    st.subheader("AI 게임 마스터")
    if get_api_key():
        st.success("API 키 연결됨")
        if st.button("API 키 연결 해제", use_container_width=True):
            st.session_state.user_api_key = ""
            st.session_state.api_key_input = ""
            st.session_state.ai_scene_messages = {}
            st.session_state.hint_messages = {}
            st.rerun()
    else:
        st.markdown(
            """
            <div class="api-login-note">
                AI 묘사를 사용하려면 본인의 OpenAI API 키를 입력하세요.
                키는 현재 브라우저 세션에서만 사용됩니다.
            </div>
            """,
            unsafe_allow_html=True,
        )
        st.text_input(
            "OpenAI API Key",
            type="password",
            placeholder="sk-...",
            key="api_key_input",
        )
        if st.button("API 키로 시작하기", use_container_width=True):
            if st.session_state.api_key_input.strip():
                st.session_state.user_api_key = st.session_state.api_key_input.strip()
                st.session_state.ai_scene_messages = {}
                st.session_state.hint_messages = {}
                st.rerun()
            else:
                st.warning("API 키를 입력해주세요.")

    st.session_state.use_ai = st.toggle(
        "OpenAI로 묘사 생성",
        value=st.session_state.use_ai,
        disabled=not bool(get_api_key()),
    )
    st.session_state.model_name = st.text_input("모델", value=st.session_state.model_name)
    if not get_api_key():
        st.caption("API 키를 입력하지 않으면 기본 스토리 문장으로 진행됩니다.")

    st.divider()
    st.subheader("보유 단서")
    for clue in st.session_state.clues:
        st.markdown(f"- {clue}")

    st.divider()
    st.subheader("힌트")
    st.caption(f"{st.session_state.hints_used}/3 사용")
    if st.session_state.hints_used >= 3:
        st.button("힌트 모두 사용", disabled=True, use_container_width=True)
    elif not st.session_state.finished:
        current_scene = SCENES[st.session_state.scene_index]
        if st.button("힌트 보기", use_container_width=True):
            use_hint(current_scene)
            st.rerun()

st.markdown('<div class="title">두더지 굴착단</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="subtitle">무너진 굴을 떠나, 가족의 선택과 AI 게임 마스터의 묘사로 새 보금자리를 찾아가는 지하 굴착 모험</div>',
    unsafe_allow_html=True,
)

if not get_api_key():
    st.markdown(
        """
        <div class="api-login-main">
            <div class="api-login-main-title">OpenAI API Key로 AI 게임 마스터 시작하기</div>
            <div class="api-login-main-body">
                방문자 본인의 API 키를 입력하면 장면 묘사, 선택 결과, 힌트가 AI로 생성됩니다.
                입력한 키는 현재 브라우저 세션에서만 사용됩니다.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
    login_col, button_col = st.columns([1.6, 0.8], gap="medium")
    with login_col:
        st.text_input(
            "OpenAI API Key",
            type="password",
            placeholder="sk-...",
            key="api_key_input_main",
            label_visibility="collapsed",
        )
    with button_col:
        if st.button("API 키 연결", type="primary", use_container_width=True):
            if st.session_state.api_key_input_main.strip():
                st.session_state.user_api_key = st.session_state.api_key_input_main.strip()
                st.session_state.api_key_input = st.session_state.api_key_input_main.strip()
                st.session_state.ai_scene_messages = {}
                st.session_state.hint_messages = {}
                st.rerun()
            else:
                st.warning("API 키를 입력해주세요.")

if not st.session_state.finished:
    scene = SCENES[st.session_state.scene_index]
    add_clue(scene["clue"])
    left, right = st.columns([1.55, 0.65], gap="large")

    with left:
        if st.session_state.scene_index == 0:
            st.image(str(ASSET_DIR / "mole-family-hero.png"), use_container_width=True)

        st.subheader(f"현재 구역: {scene['name']}")
        if st.session_state.scene_index == 0:
            story_col, journal_col = st.columns([1.25, 1.0], gap="medium")
            with story_col:
                st.markdown(opening_story_html(), unsafe_allow_html=True)
            with journal_col:
                st.markdown(
                    dedent(f"""
                    <div class="journal-frame">
                        <img src="{image_data_uri(ASSET_DIR / "grandfather-journal.png")}" style="width: 100%;" />
                        <div class="journal-caption">흙더미 속에서 발견된 할아버지의 굴착일지</div>
                    </div>
                    """).strip(),
                    unsafe_allow_html=True,
                )
        else:
            st.markdown(f'<div class="scene-box">{scene["story"]}</div>', unsafe_allow_html=True)

        # 화면에 표시되는 "AI 생성 현장 묘사" 블록입니다.
        ai_scene_intro = get_ai_scene_intro(scene)
        if ai_scene_intro:
            st.markdown(
                f"""
                <div class="ai-box">
                    <div class="ai-box-title">AI 생성 현장 묘사</div>
                    {ai_scene_intro}
                </div>
                """,
                unsafe_allow_html=True,
            )
        elif st.session_state.use_ai:
            st.caption("OpenAI API 키가 연결되면 이 위치에 장면별 AI 현장 묘사가 생성됩니다.")

        hint_message = st.session_state.hint_messages.get(st.session_state.scene_index)
        if hint_message:
            st.info(hint_message)

    with right:
        st.subheader("무엇을 할까요?")
        st.caption("선택은 모두 이야기를 앞으로 나아가게 합니다. 가장 많이 오른 스탯이 마지막 굴을 결정합니다.")
        for index, choice in enumerate(scene["choices"], start=1):
            if st.button(f"{index}. {choice['label']}", use_container_width=True):
                choose_option(choice)
                st.rerun()

        if st.session_state.log:
            st.divider()
            latest = st.session_state.log[-1]
            st.markdown(
                f"""
                <div class="result-box">
                    <b>이전 선택:</b> {latest["choice"]}<br>
                    <b>상승 스탯:</b> {latest["stat"]}<br><br>
                    {latest["result"]}
                </div>
                """,
                unsafe_allow_html=True,
            )

else:
    ending_key = get_ending_key()
    ending = ENDING_BY_STAT[ending_key]

    left, right = st.columns([1.05, 0.95], gap="large")
    with left:
        st.image(str(ending["image"]), use_container_width=True)

    with right:
        st.subheader("탈출 성공")
        st.markdown(f"## {ending['title']}")
        st.markdown(f"> {ending['quote']}")
        st.write(ending["body"])

        st.divider()
        st.subheader("최종 스탯")
        for key, label in STAT_LABELS.items():
            st.progress(st.session_state.stats[key] / len(SCENES), text=f"{label}: {st.session_state.stats[key]}")

        st.caption(f"힌트 사용: {st.session_state.hints_used}/3")

        if st.button("다른 굴 찾아보기", type="primary", use_container_width=True):
            reset_game()
            st.rerun()

    with st.expander("여정 다시 보기"):
        for item in st.session_state.log:
            st.markdown(f"**{item['scene']}**")
            st.write(f"선택: {item['choice']}")
            st.write(f"결과: {item['result']}")
            st.caption(f"상승 스탯: {item['stat']}")
