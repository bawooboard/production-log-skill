from __future__ import annotations

from typing import Any, Dict, Optional

from .models import ProductionRecord
from .storage import CsvProductionStore


class ProductionLogSkill:
    """생산일지 품목, 수량, 양품, 불량 정보를 관리하는 스킬."""

    def __init__(self, storage_path: str = "production_log.csv") -> None:
        self.store = CsvProductionStore(storage_path)

    def add_record(self, data: Dict[str, Any]) -> Dict[str, Any]:
        try:
            record = ProductionRecord.from_dict(data)
            saved = self.store.add(record)
            return {"success": True, "message": "생산일지가 정상 등록되었습니다.", "record": saved}
        except Exception as exc:
            return {"success": False, "message": str(exc)}

    def list_records(self, item: Optional[str] = None, date: Optional[str] = None) -> Dict[str, Any]:
        return {"success": True, "records": self.store.list(item=item, date=date)}

    def summary_by_item(self) -> Dict[str, Any]:
        return {"success": True, "summary": self.store.summary_by_item()}

    def daily_report(self, date: Optional[str] = None) -> Dict[str, Any]:
        records = self.store.list(date=date)
        total_quantity = sum(int(row["quantity"]) for row in records)
        total_good = sum(int(row["good"]) for row in records)
        total_defect = sum(int(row["defect"]) for row in records)
        defect_rate = round((total_defect / total_quantity) * 100, 2) if total_quantity else 0.0
        yield_rate = round((total_good / total_quantity) * 100, 2) if total_quantity else 0.0

        return {
            "success": True,
            "date": date or "ALL",
            "total_quantity": total_quantity,
            "total_good": total_good,
            "total_defect": total_defect,
            "defect_rate": defect_rate,
            "yield_rate": yield_rate,
            "records": records,
        }
