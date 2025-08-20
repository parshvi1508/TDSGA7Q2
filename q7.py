import pandas as pd
import matplotlib.pyplot as plt

# Example dataset (you can replace this with your actual CSV/Excel load)
data = {
    "Name": ["A", "B", "C", "D", "E", "F", "G"],
    "Department": ["Operations", "HR", "Operations", "IT", "Finance", "Operations", "HR"]
}

# Load into DataFrame
df = pd.DataFrame(data)

# Frequency count for "Operations"
ops_count = (df["Department"] == "Operations").sum()
print("Frequency of Operations department:", ops_count)

# Histogram of departments
plt.figure(figsize=(6, 4))
df["Department"].value_counts().plot(kind="bar")
plt.title("Department Distribution")
plt.xlabel("Departments")
plt.ylabel("Count")

# Save the plot and data summary to HTML
html_content = f"""
<html>
<head><title>Employee Department Analysis</title></head>
<body>
<h2>Employee Data Department Distribution</h2>
<p><b>Email for verification:</b> 24f1001723@ds.study.iitm.ac.in</p>
<p><b>Frequency of Operations Department:</b> {ops_count}</p>
<img src="department_distribution.png" alt="Department Histogram">
</body>
</html>
"""

# Save plot image
plt.savefig("department_distribution.png")

# Write HTML file
with open("employee_analysis.html", "w") as f:
    f.write(html_content)
