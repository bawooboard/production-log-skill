from __future__ import annotations

import json
import tempfile
from pathlib import Path

from production_log_skill import ProductionLogSkill


def assert_success(result: dict) -> None:
    assert result["success"] is True, result


def assert_fail(result: dict) -> None:
    assert result["success"] is False, result


def main() -> None:
    with tempfile.TemporaryDirectory() as temp_dir:
        db_path = Path(temp_dir) / "production_log.csv"
        skill = ProductionLogSkill(storage_path=str(db_path))

        cases = [
            {
                "name": "정상 등록 A-100",
                "input": {"date": "2026-07-09", "item": "A-100", "quantity": 100, "good": 97, "defect": 3},
                "expect_success": True,
            },
            {
                "name": "정상 등록 B-200",
                "input": {"date": "2026-07-09", "item": "B-200", "quantity": 250, "good": 245, "defect": 5},
                "expect_success": True,
            },
            {
                "name": "수량 불일치 검증",
                "input": {"date": "2026-07-09", "item": "BAD-1", "quantity": 100, "good": 95, "defect": 10},
                "expect_success": False,
            },
        ]

        outputs = []
        for case in cases:
            result = skill.add_record(case["input"])
            if case["expect_success"]:
                assert_success(result)
            else:
                assert_fail(result)
            outputs.append({"case": case["name"], "result": result})

        outputs.append({"case": "전체 조회", "result": skill.list_records()})
        outputs.append({"case": "품목별 집계", "result": skill.summary_by_item()})
        outputs.append({"case": "생산일보 출력", "result": skill.daily_report(date="2026-07-09")})

        print(json.dumps(outputs, ensure_ascii=False, indent=2))
        print("\n✅ 하네스 테스트 통과")


if __name__ == "__main__":
    main()
