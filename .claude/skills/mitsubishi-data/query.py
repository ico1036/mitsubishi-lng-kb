#!/usr/bin/env python3
"""
mitsubishi-data — 미쓰비시 LNG 밸류체인 리서치 데이터 조회 (표준 라이브러리 전용, 의존성 없음)

이 스크립트는 pandas/외부 패키지가 필요 없습니다. python3만 있으면 어디서나 동작합니다.
(설치 명령 불필요 — 코드를 모르는 사용자도 막힘 없이 쓰도록 stdlib만 사용.)

데이터는 Mitsubishi-LNG-Vault/_data/ 의 CSV들이며, 경로는 자동 탐지됩니다.
환경변수 MITSUBISHI_DATA_DIR 로 재정의 가능.

사용법:
  python3 query.py                       # 데이터셋 개요 (인자 없을 때)
  python3 query.py list                  # 데이터셋 목록 + 행수/컬럼
  python3 query.py show <dataset>        # 데이터셋 전체 출력
  python3 query.py show <dataset> --where 컬럼=값   # 부분일치 필터
  python3 query.py search "<검색어>"      # 모든 CSV의 모든 셀에서 검색
  python3 query.py finance               # 연결순이익 시계열 + LNG 베타 요약
  python3 query.py sources [--quality primary]    # 소스 원장
  python3 query.py graph [--entity <키>] # 온톨로지 노드/관계
"""
import csv
import os
import sys
from pathlib import Path


def find_data_dir() -> Path:
    env = os.environ.get("MITSUBISHI_DATA_DIR")
    if env:
        return Path(env)
    here = Path(__file__).resolve()
    for base in [here] + list(here.parents):
        cand = base / "Mitsubishi-LNG-Vault" / "_data"
        if cand.is_dir():
            return cand
    # 현재 작업 디렉토리 기준 폴백
    for base in [Path.cwd()] + list(Path.cwd().parents):
        cand = base / "Mitsubishi-LNG-Vault" / "_data"
        if cand.is_dir():
            return cand
    return here.parent / "Mitsubishi-LNG-Vault" / "_data"


DATA = find_data_dir()


def datasets():
    return sorted(p.stem for p in DATA.glob("*.csv")) if DATA.is_dir() else []


def load(name):
    path = DATA / (name if name.endswith(".csv") else name + ".csv")
    if not path.exists():
        sys.exit(f"데이터셋 없음: {name}\n사용 가능: {', '.join(datasets())}")
    with open(path, newline="", encoding="utf-8") as f:
        r = csv.reader(f)
        rows = list(r)
    return rows[0], rows[1:]


def _w(s):
    # 대략적인 표시폭: CJK/전각은 2칸으로 계산
    return sum(2 if ord(c) > 0x1100 and (
        0x1100 <= ord(c) <= 0x115F or 0x2E80 <= ord(c) <= 0xA4CF or
        0xAC00 <= ord(c) <= 0xD7A3 or 0xF900 <= ord(c) <= 0xFAFF or
        0xFE30 <= ord(c) <= 0xFE4F or 0xFF00 <= ord(c) <= 0xFF60 or
        0xFFE0 <= ord(c) <= 0xFFE6) else 1 for c in str(s))


def _pad(s, width):
    s = str(s)
    return s + " " * max(0, width - _w(s))


def print_table(header, rows, maxcol=60):
    if not rows:
        print("(행 없음)")
        return
    cols = list(range(len(header)))
    trunc = lambda v: (str(v)[:maxcol] + "…") if _w(str(v)) > maxcol else str(v)
    data = [[trunc(c) for c in r] for r in rows]
    widths = [max(_w(header[i]), max((_w(r[i]) for r in data), default=0)) for i in cols]
    print(" | ".join(_pad(header[i], widths[i]) for i in cols))
    print("-+-".join("-" * widths[i] for i in cols))
    for r in data:
        print(" | ".join(_pad(r[i] if i < len(r) else "", widths[i]) for i in cols))


def cmd_list(_):
    if not DATA.is_dir():
        sys.exit(f"데이터 디렉토리를 찾을 수 없음: {DATA}\n"
                 f"이 스크립트는 Mitsubishi-LNG-Vault/_data 가 상위 경로에 있어야 합니다.")
    print(f"데이터 경로: {DATA}\n")
    for name in datasets():
        h, rows = load(name)
        print(f"• {name:28s} {len(rows):>4d}행  [{', '.join(h)}]")
    print("\n예) python3 query.py finance   |   python3 query.py search 호르무즈")


def cmd_show(args):
    h, rows = load(args.dataset)
    for cond in (args.where or []):
        col, _, val = cond.partition("=")
        if col not in h:
            sys.exit(f"컬럼 없음: {col}  (가능: {', '.join(h)})")
        idx = h.index(col)
        rows = [r for r in rows if idx < len(r) and val.lower() in r[idx].lower()]
    print_table(h, rows)
    print(f"\n{len(rows)}행")


def _vault_dir():
    for base in [DATA] + list(DATA.parents):
        if base.name == "Mitsubishi-LNG-Vault" and base.is_dir():
            return base
    return DATA.parent  # _data 의 부모 = 볼트


def cmd_search(args):
    term = args.term.lower()
    total = 0
    # 1) 구조화 데이터(CSV)
    for name in datasets():
        h, rows = load(name)
        hit = [r for r in rows if any(term in str(c).lower() for c in r)]
        if hit:
            print(f"\n=== [데이터] {name} ({len(hit)}행) ===")
            print_table(h, hit)
            total += len(hit)
    # 2) 정성 노트(.md) — 제목/본문 부분일치
    notes = []
    vd = _vault_dir()
    if vd.is_dir():
        for md in sorted(vd.rglob("*.md")):
            try:
                txt = md.read_text(encoding="utf-8")
            except Exception:
                continue
            if term in txt.lower() or term in md.stem.lower():
                # 첫 일치 줄 스니펫
                snip = next((ln.strip() for ln in txt.splitlines()
                             if term in ln.lower() and not ln.startswith("---")), "")
                notes.append((md.stem, snip[:90]))
    if notes:
        print(f"\n=== [노트] {len(notes)}개 일치 ===")
        for stem, snip in notes:
            print(f"  • {stem}  —  {snip}")
        total += len(notes)
    if not total:
        print(f"'{args.term}' 일치 없음. (동의어로 재시도: 예 '버핏'→'버크셔', 'Aethon'/'헤인스빌')")
    else:
        print(f"\n총 {total}건 일치 (데이터+노트)")


def cmd_finance(_):
    h, rows = load("financials_net_income")
    print("미쓰비시상사(8058.T) 연결 순이익 시계열 (억엔, 지배주주귀속)\n")
    print_table(h, rows, maxcol=40)
    m = {r[0]: r[2] for r in rows}
    try:
        low, peak, last = int(m["FY2020"]), int(m["FY2022"]), int(m["FY2025"])
        print(f"\n저점 FY2020 {low:,} → 정점 FY2022 {peak:,} = {peak/low:.1f}배 (3년)")
        print(f"최근 FY2025 {last:,} (정점 대비 {last/peak-1:+.0%}) — LNG·자원 가격 베타가 큼")
    except (KeyError, ValueError):
        pass


def cmd_sources(args):
    h, rows = load("sources")
    if args.quality:
        idx = h.index("quality")
        rows = [r for r in rows if args.quality.lower() in r[idx].lower()]
    print_table(h, rows, maxcol=70)
    print(f"\n총 {len(rows)}개 소스")


def cmd_graph(args):
    nh, nrows = load("ontology_nodes")
    eh, erows = load("ontology_edges")
    if args.entity:
        e = args.entity.lower()
        print(f"=== 노드: {args.entity} ===")
        print_table(nh, [r for r in nrows if e in r[0].lower() or e in r[1].lower()])
        print(f"\n=== 관계: {args.entity} ===")
        print_table(eh, [r for r in erows if e in r[0].lower() or e in r[1].lower()])
    else:
        print(f"노드 {len(nrows)}개 / 관계 {len(erows)}개\n")
        top = sorted(nrows, key=lambda r: int(r[-1]), reverse=True)[:8]
        print("연결도 상위 노드:")
        print_table([nh[0], nh[1], nh[2], nh[4], nh[6]],
                    [[r[0], r[1], r[2], r[4], r[6]] for r in top])
        from collections import Counter
        c = Counter(r[2] for r in erows)
        print("\n관계 유형 분포: " + ", ".join(f"{k} {v}" for k, v in c.most_common()))


def main():
    import argparse
    p = argparse.ArgumentParser(description="미쓰비시 LNG 리서치 데이터 조회 (의존성 없음)")
    sub = p.add_subparsers(dest="cmd")
    sub.add_parser("list")
    sp = sub.add_parser("show"); sp.add_argument("dataset"); sp.add_argument("--where", action="append")
    sp = sub.add_parser("search"); sp.add_argument("term")
    sub.add_parser("finance")
    sp = sub.add_parser("sources"); sp.add_argument("--quality")
    sp = sub.add_parser("graph"); sp.add_argument("--entity")
    args = p.parse_args()
    cmds = {"list": cmd_list, "show": cmd_show, "search": cmd_search,
            "finance": cmd_finance, "sources": cmd_sources, "graph": cmd_graph}
    (cmds.get(args.cmd) or cmd_list)(args)


if __name__ == "__main__":
    main()
