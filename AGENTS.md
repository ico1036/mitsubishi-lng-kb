# AGENTS.md — 미쓰비시상사 LNG 밸류체인 지식베이스

> **에이전트(너)에게:** 이 파일 하나만 읽으면 이 지식베이스를 막힘없이 쓸 수 있다.
> 사용자는 코드를 모를 수 있다. 사용자가 "설치해라/명령어 쳐라"를 하게 만들지 마라 —
> **네가** 파일을 읽거나 아래 도구를 대신 실행해서 답하라.

---

## 1. 이게 뭔가
워런 버핏이 장기 보유하는 일본 종합상사 **미쓰비시상사(8058.T)**가 50년에 걸쳐 구축한
**LNG 밸류체인**(상류 가스전 지분→액화→수송→트레이딩→발전/데이터센터)과 그 **한국 에너지산업 함의**를
정리한 리서치 지식베이스다. 출처: deep-research(106 에이전트, 24소스→14검증발견) + 미쓰비시 IR/AFR 재무 + 자체 종합 리포트 3종(Equity Research 포함) + 발표자료 3종.

**핵심 메시지:** 미쓰비시는 LNG *물량*이 아니라 *경로 선택권(option value)*을 샀고, 위기 때 그 가치가 드러난다.
한국의 질문은 "어디서 더 살까"가 아니라 "가진 것을 누가 어떻게 운용할까"다.

## 2. START HERE — 3단계
1. **목차 먼저 읽기:** `Mitsubishi-LNG-Vault/00-INDEX.md` — 전체 지도(클러스터·발견·소스·데이터).
2. **질문 유형 판단** (아래 §4 결정표).
3. **답하기:** 정성 질문 → 노트(.md) 읽기 / 정량 질문 → 데이터 도구나 CSV / 관계 질문 → 온톨로지.

## 3. 폴더 구조
```
mitsubishi-lng-kb/
├─ AGENTS.md                         ← 지금 이 파일
├─ README.md                         ← 사람(비개발자)용 한 장 안내
├─ Mitsubishi-LNG-Vault/             ← 지식베이스 본체 (Obsidian 볼트, 그냥 마크다운)
│  ├─ 00-INDEX.md                    ← ★ 목차/허브. 항상 여기서 시작
│  ├─ ONTOLOGY-관계지도.md            ← 33노드·41관계 지식그래프 설명
│  ├─ S/                             ← 소스 노트 (S- = 출처, 16개)
│  ├─ F/                             ← 발견 노트 (F- = 검증된 사실/주장, 24개)
│  ├─ MOC/                           ← 허브 노트 (MOC- = 주제별 묶음, 6개)
│  ├─ _data/*.csv                    ← ★ 숫자/관계 데이터 (재무·온톨로지·소스)
│  ├─ _raw-sources/                  ← 원본 추출 텍스트 (전문검색용)
│  └─ _raw-deep-research-result.json ← deep-research 원본 결과
├─ .claude/skills/mitsubishi-data/   ← 조회 도구 (query.py, 의존성 없음)
├─ sources-original/                 ← 빌드 원본 (재무 xlsx + 자체 리포트 HTML 3종, Equity Research 포함) — 노트가 provenance로 인용
└─ reports/                          ← 최종 산출물·발표자료 (발표/비교 PDF 3종 + reports/README.md) — 사람이 읽기/발표용
```
> 📄 **`reports/`는 읽기·발표용 산출물**이다. 사용자가 "리포트/발표자료 보여줘"라고 하면 여기를 안내하라(사람용 가이드 = `reports/README.md`).
> 단, 사실의 1차 출처는 `S/` 노트와 `sources-original/`이다 — **reports/의 PDF를 출처로 인용하지 마라.**

## 4. 질문 → 어디를 볼까 (결정표)
| 사용자 질문 유형 | 우선 행동 |
|---|---|
| 숫자·시계열 ("순이익 추이?", "Aethon 얼마?") | `query.py finance` 또는 `_data/*.csv` 읽기 |
| 무엇이든 키워드 검색 ("버핏?", "호르무즈?") | `query.py search "키워드"` (CSV+노트 동시) |
| 분석·맥락·왜 ("왜 중요?", "한국 함의?") | `F/`·`MOC/` 노트 읽기 (00-INDEX에서 링크 따라가기) |
| 회사·프로젝트 관계 ("KOGAS와 무슨 관계?") | `query.py graph --entity kogas` 또는 `ONTOLOGY-관계지도.md` |
| 출처/근거 ("이거 어디서 나온 거야?") | `query.py sources` 또는 해당 F-노트의 **출처:** 줄 |

## 5. 조회 도구 (선택사항, 의존성 없음)
`python3`만 있으면 동작한다. **설치 불필요**(pandas 안 씀). 어느 폴더에서 실행해도 데이터 경로 자동 탐지.
```bash
python3 .claude/skills/mitsubishi-data/query.py finance              # 순이익 시계열 + LNG 베타 6.8배
python3 .claude/skills/mitsubishi-data/query.py search "호르무즈"     # CSV+노트 전체 검색
python3 .claude/skills/mitsubishi-data/query.py graph --entity donggi
python3 .claude/skills/mitsubishi-data/query.py sources --quality primary
python3 .claude/skills/mitsubishi-data/query.py list                 # 데이터셋 목록
```
**도구가 안 되면(또는 python3 없으면):** 막히지 말고 **그냥 파일을 직접 읽어라.**
모든 게 평문이다 — `_data/*.csv`는 표, `*.md`는 분석. 도구는 단지 편의 기능이다.

## 6. 노트 읽는 법 (규칙)
- **S-** 소스: `quality: primary/secondary`, 기관·URL. **F-** 발견: `confidence`, `vote`, **클레임/근거/출처/허브** 구조. **MOC-** 허브: 주제별 묶음 + 링크.
- `[[이중대괄호]]` = 노트 간 링크. 따라가며 맥락을 넓혀라.
- 인덱스 마커: **🆕** = 추가 자료 통합, **✅** = 감사로 보강.

## 7. ⚠️ 틀리면 안 되는 것 (반드시 지켜라)
1. **버핏은 "미쓰비시만 영원히 보유"라고 말한 적 없다.** 정확히는 일본 5대 상사 바스켓을 *very long term·many decades* 보유. ([[F-버핏-very-long-term-many-decades]])
2. **호르무즈 통과 비중 — 원유는 두 값 공존, LNG는 수렴:** *원유* vault/Reuters **~35%** vs EIA **~21%**(EIA는 '석유류 전체' 정의) — 하나만 단정 말고 출처·정의를 밝혀라. *LNG*는 양측 **~20%**로 일치. ([[F-호르무즈-EIA-KIET-한국원가]] · [[F-호르무즈-chokepoint-35-20]])
3. **미쓰비시는 Cameron LNG 시설을 *운영*하지 않는다** (지분/톨링만). 이 주장은 검증에서 기각(0-3).
4. **`confidence: low` 데이터**(NWS 16.67%·사할린 10%·2030s 18Mtpa·석유공사 90만배럴 사건)는 1차 미확인 — "검증 필요"라고 밝혀라.
5. **재무 FY 표기 주의:** 연결순이익_추이는 일본 FY(FY2022=Mar2023 종료), EE세그먼트 CSV 컬럼은 회계연도 *종료월*(FYE Mar2023) 기준. FY2022 순이익 권위값 = **11,806억엔**.
6. **동의어:** 버핏↔버크셔, Aethon↔헤인스빌, DGI↔Diamond Gas International, 소고쇼샤↔종합상사. 검색이 0건이면 동의어로 재시도.
7. **투자 자문 아님.** 리서치 정리물이다. 매수/매도 권유로 답하지 마라.
8. **밸류에이션·시장수치는 자체 추정/시점 의존이다.** DCF 적정가 ≈¥3,101·고평가 판단([[F-밸류에이션-DCF-고평가-진입신호]])은 자체 DCF·가정 의존으로 시장 합의가 아니다. KOGAS 미수금 14조·2026 공급과잉(+300bcm·<$10·카타르 75%)은 2026.06 시점 의존이며 일부 1차 미확인 — 단정하지 말고 출처·시점을 밝혀라.

## 8. 예시 — 비개발자가 Claude에게 물었을 때 (네가 이렇게 한다)
- **"미쓰비시 순이익 언제가 제일 높았어?"** → `query.py finance` 실행 → "FY2022(Mar2023) 11,806억엔 역대 최고. COVID 저점 FY2020 1,725억엔에서 3년 만에 6.8배." (도구 안 되면 `_data/financials_net_income.csv` 읽기)
- **"버핏이 미쓰비시 영원히 갖는다던데 진짜야?"** → `search 버핏` → F-버핏 노트 읽기 → "정확히는 5대 상사 바스켓을 수십 년(very long term) 보유 의사. '미쓰비시만 영원히'는 부정확." (§7-1)
- **"호르무즈가 한국에 왜 중요해?"** → `search 호르무즈` → MOC-5 + F-호르무즈 노트 → 통과 비중(35% vs 21% 둘 다 명시)·일본 의존도·KIET 한국 제조원가 +11.8% 설명.
- **"이 내용 근거 있어?"** → 해당 F-노트의 **출처:** 줄 + `query.py sources` → URL·품질등급 제시.

## 9. 데이터를 더 합치거나 검증하려면 (선택)
새 자료를 받으면: ① 추출 → ② `00-INDEX` 인벤토리와 diff(닥택체크) → ③ 빈칸만 노트/CSV로 추가, 적대검증으로 확인.
숫자는 `_data/*.csv`에, 출처 URL은 `sources.csv`·온톨로지 엣지에, 분석은 S/F/MOC 노트에. 적대검증 안 한 항목은 노트에 명시.

## 10. 한계
- 시점: 2026년 6월 기준. 일부 단서(버핏 투자논리·석유공사 사건 1차보도·KOGAS 통합도 정량비교)는 미해결 → `MOC-6-미해결질문-supersearch.md`.
- 무료/공개 출처 + 사용자 제공 IR 기반. 1차 미확인 항목은 confidence로 구분돼 있다.
