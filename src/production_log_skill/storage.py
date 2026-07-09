from __future__ import annotations

import csv
from pathlib import Path
from typing import Iterable, List, Optional

from .models import ProductionRecord


FIELDNAMES = ["date", "item", "quantity", "good", "defect", "defect_rate", "yield_rate"]


class CsvProductionStore:
    def __init__(self, path: str | Path = "production_log.csv") -> None:
        self.path = Path(path)
        if not self.path.exists():
            self.path.parent.mkdir(parents=True, exist_ok=True)
            with self.path.open("w", newline="", encoding="utf-8-sig") as f:
                writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
                writer.writeheader()

    def add(self, record: ProductionRecord) -> dict:
        record.validate()
        row = record.to_dict()
        with self.path.open("a", newline="", encoding="utf-8-sig") as f:
            writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
            writer.writerow(row)
        return row

    def list(self, item: Optional[str] = None, date: Optional[str] = None) -> List[dict]:
        with self.path.open("r", newline="", encoding="utf-8-sig") as f:
            rows = list(csv.DictReader(f))
        if item:
            rows = [r for r in rows if r["item"] == item]
        if date:
            rows = [r for r in rows if r["date"] == date]
        return rows

    def summary_by_item(self) -> List[dict]:
        summary: dict[str, dict] = {}
        for row in self.list():
            item = row["item"]
            if item not in summary:
                summary[item] = {"item": item, "quantity": 0, "good": 0, "defect": 0}
            summary[item]["quantity"] += int(row["quantity"])
            summary[item]["good"] += int(row["good"])
            summary[item]["defect"] += int(row["defect"])

        result = []
        for item_summary in summary.values():
            quantity = item_summary["quantity"]
            item_summary["defect_rate"] = round((item_summary["defect"] / quantity) * 100, 2) if quantity else 0.0
            item_summary["yield_rate"] = round((item_summary["good"] / quantity) * 100, 2) if quantity else 0.0
            result.append(item_summary)
        return result
