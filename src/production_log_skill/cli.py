from __future__ import annotations

import argparse
import json
from typing import Any

from .skill import ProductionLogSkill


def print_json(value: Any) -> None:
    print(json.dumps(value, ensure_ascii=False, indent=2))


def main() -> None:
    parser = argparse.ArgumentParser(description="생산일지 관리 CLI")
    parser.add_argument("--db", default="production_log.csv", help="CSV 저장 경로")

    sub = parser.add_subparsers(dest="command", required=True)

    add = sub.add_parser("add", help="생산일지 등록")
    add.add_argument("--date", required=True, help="YYYY-MM-DD")
    add.add_argument("--item", required=True, help="품목명 또는 품번")
    add.add_argument("--quantity", required=True, type=int, help="총 생산수량")
    add.add_argument("--good", required=True, type=int, help="양품수량")
    add.add_argument("--defect", required=True, type=int, help="불량수량")

    list_parser = sub.add_parser("list", help="생산일지 조회")
    list_parser.add_argument("--item", help="품목 필터")
    list_parser.add_argument("--date", help="날짜 필터: YYYY-MM-DD")

    sub.add_parser("summary", help="품목별 집계")

    report_parser = sub.add_parser("report", help="생산일보 출력")
    report_parser.add_argument("--date", help="출력할 생산일: YYYY-MM-DD. 생략하면 전체 기간")

    args = parser.parse_args()
    skill = ProductionLogSkill(storage_path=args.db)

    if args.command == "add":
        print_json(skill.add_record({
            "date": args.date,
            "item": args.item,
            "quantity": args.quantity,
            "good": args.good,
            "defect": args.defect,
        }))
    elif args.command == "list":
        print_json(skill.list_records(item=args.item, date=args.date))
    elif args.command == "summary":
        print_json(skill.summary_by_item())
    elif args.command == "report":
        print_json(skill.daily_report(date=args.date))


if __name__ == "__main__":
    main()
