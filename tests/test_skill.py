from production_log_skill import ProductionLogSkill


def test_add_record_success(tmp_path):
    skill = ProductionLogSkill(storage_path=str(tmp_path / "log.csv"))
    result = skill.add_record({"date": "2026-07-09", "item": "A-100", "quantity": 100, "good": 97, "defect": 3})
    assert result["success"] is True
    assert result["record"]["defect_rate"] == 3.0
    assert result["record"]["yield_rate"] == 97.0


def test_add_record_quantity_mismatch(tmp_path):
    skill = ProductionLogSkill(storage_path=str(tmp_path / "log.csv"))
    result = skill.add_record({"date": "2026-07-09", "item": "A-100", "quantity": 100, "good": 95, "defect": 10})
    assert result["success"] is False
    assert "일치하지 않습니다" in result["message"]


def test_summary_by_item(tmp_path):
    skill = ProductionLogSkill(storage_path=str(tmp_path / "log.csv"))
    skill.add_record({"date": "2026-07-09", "item": "A-100", "quantity": 100, "good": 97, "defect": 3})
    skill.add_record({"date": "2026-07-10", "item": "A-100", "quantity": 50, "good": 48, "defect": 2})
    summary = skill.summary_by_item()["summary"]
    assert summary[0]["quantity"] == 150
    assert summary[0]["good"] == 145
    assert summary[0]["defect"] == 5


def test_daily_report(tmp_path):
    skill = ProductionLogSkill(storage_path=str(tmp_path / "log.csv"))
    skill.add_record({"date": "2026-07-09", "item": "A-100", "quantity": 100, "good": 97, "defect": 3})
    skill.add_record({"date": "2026-07-09", "item": "B-200", "quantity": 250, "good": 245, "defect": 5})
    report = skill.daily_report(date="2026-07-09")
    assert report["success"] is True
    assert report["total_quantity"] == 350
    assert report["total_good"] == 342
    assert report["total_defect"] == 8
