#Project1
# 1 Plot sales over time (line charts) and monthly/quarterly aggregation.
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("sales.csv")

data["Date"] = pd.to_datetime(data["Date"])

data = data.sort_values("Date")

plt.figure()
plt.plot(data["Date"], data["Sales"])
plt.title("Sales Trend")
plt.xlabel("Date")
plt.ylabel("Sales")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("trend.png")
plt.show()

monthly = data.groupby(data["Date"].dt.to_period("M"))["Sales"].sum()
monthly.index = monthly.index.astype(str)

plt.figure()
plt.plot(monthly.index, monthly.values)
plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("monthly.png")
plt.show()

quarterly = data.groupby(data["Date"].dt.to_period("Q"))["Sales"].sum()
quarterly.index = quarterly.index.astype(str)

plt.figure()
plt.plot(quarterly.index, quarterly.values)
plt.title("Quarterly Sales")
plt.xlabel("Quarter")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("quarterly.png")
plt.show()

#2 Use bar charts to compare categories and pie charts for share.

import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("my_sales.csv")

category_total = data.groupby("Category")["Sales"].sum()

plt.figure()
plt.bar(category_total.index, category_total.values)
plt.xlabel("Category")
plt.ylabel("Total Sales")
plt.title("Comparison of Sales by Category")
plt.tight_layout()
plt.show()

plt.figure()
plt.pie(category_total.values, labels=category_total.index, autopct="%1.1f%%")
plt.title("Sales Share by Category")
plt.tight_layout()
plt.show()

# 3 Save charts to PNG and export a short summary.

import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("my_sales.csv")

category_total = data.groupby("Category")["Sales"].sum()

plt.figure()
plt.bar(category_total.index, category_total.values)
plt.xlabel("Category")
plt.ylabel("Total Sales")
plt.title("Comparison of Sales by Category")
plt.tight_layout()
plt.savefig("category_bar.png")
plt.close()

plt.figure()
plt.pie(category_total.values, labels=category_total.index, autopct="%1.1f%%")
plt.title("Sales Share by Category")
plt.tight_layout()
plt.savefig("category_pie.png")
plt.close()

total_sales = category_total.sum()
top_category = category_total.idxmax()

summary_text = f"""
Total Sales: {total_sales}

Top Performing Category: {top_category}

Category-wise Sales:
{category_total.to_string()}
"""

with open("summary.txt", "w") as f:
    f.write(summary_text)

print("Charts saved as PNG and summary exported.")

#4 Discuss chart choice and label/legend/axis formatting.

# Bar Chart:
# Bar chart is used to compare sales of different categories. It clearly shows which category has higher or lower sales.

# Pie Chart:
# Pie chart is used to show the share of each category in total sales. It shows percentage contribution of every category.

# Labels and Axis:
# X-axis shows category names and Y-axis shows total sales. Titles are added to explain the chart. Percentage is displayed in pie chart for better understanding.

