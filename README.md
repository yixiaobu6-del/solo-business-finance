# 一人公司财务仪表盘

> 独立开发者/自由职业者专属财务管理系统，收支分析与数据导出

---

## Features / 功能特点

| 功能 | 说明 |
|------|------|
| 收入/支出录入 | 按产品和运营等分类记录流水 |
| 自动分类 | 收入和支出各6大子分类自动归类 |
| 仪表盘展示 | 总收入/总支出/现金流概览卡片 |
| 支出饼图 | 各类支出占比可视化分析 |
| 月度趋势图 | 月度收支对比柱状图 |
| 年度统计表 | 按月查看收入/支出/结余明细 |
| 导出 CSV | 一键导出全部流水数据 |
| 本地存储 | localStorage 数据持久化 |

## Installation / 安装

无需安装，直接在浏览器中打开 `index.html` 即可使用。

```bash
# 克隆仓库
git clone https://github.com/yourusername/one-person-financial-dashboard.git

cd one-person-financial-dashboard
open index.html
```

## Usage / 使用方法

### 基础用法

1. 在浏览器中打开 `index.html`
2. 点击「新增」Tab 录入收入或支出流水
3. 切换到「仪表盘」查看自动更新的卡片和图表
4. 「流水记录」Tab 可按类型和分类筛选查看
5. 点击「导出CSV」下载完整数据

### 分类说明

```javascript
// 收入分类
const incomeCategories = [
  "产品销售",
  "咨询服务",
  "课程收入",
  "广告收入",
  "合作分成",
  "其他收入"
];

// 支出分类
const expenseCategories = [
  "产品开发",
  "营销推广",
  "运营成本",
  "生活开支",
  "工具订阅",
  "其他支出"
];
```

### 数据结构

```javascript
// 流水记录示例
{
  id: 1704067200000,
  type: "收入",                 // 收入/支出
  category: "产品销售",         // 分类
  amount: 5000,                // 金额
  date: "2024-01-01",          // 日期
  note: "1月产品销售",          // 备注
  createdAt: "2024-01-01T00:00:00.000Z"
}
```

### 导出 CSV 格式

```csv
类型,分类,金额,日期,备注
收入,产品销售,5000,2024-01-01,1月产品销售
支出,工具订阅,99,2024-01-05, 云服务器费用
支出,运营成本,300,2024-01-10,办公用品
收入,咨询服务,2000,2024-01-15,咨询费
```

## Contributing / 贡献

参见 [CONTRIBUTING.md](CONTRIBUTING.md)

## License / 许可证

MIT License - 参见 [LICENSE](LICENSE)

---

> 版本：1.0.0 | 更新日期：2026-05-30