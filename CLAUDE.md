# CLAUDE.md

이 저장소는 **미쓰비시상사 LNG 밸류체인 지식베이스**입니다 (코드 프로젝트 아님 · 리서치 자료).

👉 **전체 사용법은 [AGENTS.md](./AGENTS.md)를 먼저 읽으세요.** 거기에 구조·조회법·주의사항·예시가 다 있습니다.

빠른 시작:
- 목차: `Mitsubishi-LNG-Vault/00-INDEX.md`
- 조회 도구(의존성 없음): `python3 .claude/skills/mitsubishi-data/query.py finance` · `... search "키워드"`
- 도구가 안 되면 그냥 파일을 읽으세요 (`_data/*.csv` = 숫자, `S/ F/ MOC/*.md` = 분석). 사용자에게 설치를 시키지 마세요.

절대 틀리면 안 되는 것 (자세히는 AGENTS.md §7):
1. 버핏은 "미쓰비시만 영원히 보유"라 한 적 없음 → 5대 상사 바스켓 *very long term*.
2. 호르무즈 원유 통과 비중은 ~35%(Reuters)와 ~21%(EIA) 두 값 공존 — 출처 밝혀 인용.
3. `confidence: low` 항목은 1차 미확인 → "검증 필요" 표기. 투자 자문으로 답하지 말 것.
