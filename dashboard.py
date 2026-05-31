"""一人公司财务仪表盘"""

from datetime import datetime, timedelta
import json


class FinanceDashboard:
    """一人公司财务仪表盘，追踪收支流水并生成月度/年度统计。"""

    def __init__(self):
        """初始化仪表盘，创建空交易列表和类别统计字典。"""
        self.transactions = []
        self.income_categories = {}
        self.expense_categories = {}

    def add_transaction(self, date: str, amount: float, category: str,
                        ttype: str, note: str = ""):
        """添加一笔收支交易。

        Args:
            date: 交易日期，格式"YYYY-MM-DD"
            amount: 金额（元）
            category: 类别，如"咨询收入"、"办公设备"
            ttype: 类型，"收入"或"支出"
            note: 备注（可选）
        """
        self.transactions.append({
            "date": date, "amount": amount,
            "category": category, "type": ttype, "note": note,
        })
        target = self.income_categories if ttype == "收入" else self.expense_categories
        target[category] = target.get(category, 0) + amount

    def monthly_summary(self, year: int, month: int) -> dict:
        """生成指定月份的收支汇总。

        Args:
            year: 年份
            month: 月份（1-12）

        Returns:
            月度统计字典，包含收入、支出、净利润、利润率
        """
        income = sum(t["amount"] for t in self.transactions
                     if t["date"].startswith(f"{year}-{month:02d}") and t["type"] == "收入")
        expense = sum(t["amount"] for t in self.transactions
                      if t["date"].startswith(f"{year}-{month:02d}") and t["type"] == "支出")
        return {
            "month": f"{year}-{month:02d}",
            "收入": income,
            "支出": expense,
            "净利润": income - expense,
            "利润率": f"{(income - expense) / income * 100:.1f}%" if income > 0 else "0%",
        }

    def annual_summary(self, year: int) -> dict:
        """生成指定年份的收支汇总。

        Args:
            year: 年份

        Returns:
            年度统计字典，包含总收入、总支出、净利润、月均值、收支比
        """
        months = []
        for m in range(1, 13):
            ms = self.monthly_summary(year, m)
            if ms["收入"] > 0 or ms["支出"] > 0:
                months.append(ms)
        if not months:
            return {"year": year, "msg": "无数据"}
        total_income = sum(m["收入"] for m in months)
        total_expense = sum(m["支出"] for m in months)
        return {
            "year": year,
            "总收入": total_income,
            "总支出": total_expense,
            "净利润": total_income - total_expense,
            "月均收入": total_income / max(len(months), 1),
            "月均支出": total_expense / max(len(months), 1),
            "收支比": f"{total_expense/total_income*100:.1f}%" if total_income > 0 else "N/A",
        }

    def category_breakdown(self) -> dict:
        """生成收支类别构成分析。

        Returns:
            类别构成字典，包含"收入构成"和"支出构成"，按金额降序排列
        """
        return {
            "收入构成": dict(sorted(self.income_categories.items(), key=lambda x: -x[1])),
            "支出构成": dict(sorted(self.expense_categories.items(), key=lambda x: -x[1])),
        }


if __name__ == "__main__":
    db = FinanceDashboard()
    db.add_transaction("2026-05-01", 15000, "咨询收入", "收入")
    db.add_transaction("2026-05-01", 8000, "课程收入", "收入")
    db.add_transaction("2026-05-02", 2000, "办公设备", "支出")
    db.add_transaction("2026-05-03", 500, "软件订阅", "支出")
    print(json.dumps(db.monthly_summary(2026, 5), ensure_ascii=False, indent=2))
