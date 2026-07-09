from __future__ import annotations

from dataclasses import dataclass, asdict
from datetime import date, datetime
from typing import Any, Dict


@dataclass(frozen=True)
class ProductionRecord:
    production_date: date
    item: str
    quantity: int
    good: int
    defect: int

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "ProductionRecord":
        raw_date = data.get("date") or data.get("production_date")
        if isinstance(raw_date, date):
            production_date = raw_date
        elif isinstance(raw_date, str):
            production_date = datetime.strptime(raw_date, "%Y-%m-%d").date()
        else:
            raise ValueError("date는 YYYY-MM-DD 형식이어야 합니다.")

        return cls(
            production_date=production_date,
            item=str(data.get("item", "")).strip(),
            quantity=int(data.get("quantity", 0)),
            good=int(data.get("good", 0)),
            defect=int(data.get("defect", 0)),
        )

    def validate(self) -> None:
        if not self.item:
            raise ValueError("품목(item)은 필수입니다.")
        if self.quantity < 0 or self.good < 0 or self.defect < 0:
            raise ValueError("수량, 양품, 불량은 0 이상이어야 합니다.")
        if self.good + self.defect != self.quantity:
            raise ValueError("총수량과 양품+불량 수량이 일치하지 않습니다.")

    @property
    def defect_rate(self) -> float:
        return round((self.defect / self.quantity) * 100, 2) if self.quantity else 0.0

    @property
    def yield_rate(self) -> float:
        return round((self.good / self.quantity) * 100, 2) if self.quantity else 0.0

    def to_dict(self) -> Dict[str, Any]:
        result = asdict(self)
        result["date"] = self.production_date.isoformat()
        result.pop("production_date", None)
        result["defect_rate"] = self.defect_rate
        result["yield_rate"] = self.yield_rate
        return result
