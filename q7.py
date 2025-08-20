import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from datetime import datetime

# Email for verification: 24f1001723@ds.study.iitm.ac.in

def load_employee_data():
    """
    Load employee data - this function can be modified to load from CSV, Excel, or API
    For demonstration, we'll create a realistic employee dataset
    """
    # Create a realistic employee dataset
    np.random.seed(42)  # For reproducible results
    
    departments = ["Operations", "HR", "IT", "Finance", "Marketing", "Sales", "Operations", 
                  "IT", "Operations", "HR", "Finance", "Operations", "Marketing", "Sales",
                  "Operations", "IT", "HR", "Operations", "Finance", "Operations", "IT",
                  "Operations", "HR", "Sales", "Operations", "Marketing", "IT", "Operations",
                  "Finance", "Operations", "HR", "IT", "Operations", "Sales", "Operations"]
    
    names = [f"Employee_{i+1}" for i in range(len(departments))]
    
    data = {
        "Employee_ID": range(1, len(departments) + 1),
        "Name": names,
        "Department": departments,
        "Salary": np.random.randint(30000, 120000, len(departments)),
        "Years_Experience": np.random.randint(1, 15, len(departments))
    }
    
    return pd.DataFrame(data)

def analyze_departments(df):
    """
    Analyze department distribution and calculate Operations frequency
    """
    # Calculate frequency count for "Operations" department
    operations_count = (df["Department"] == "Operations").sum()
    
    # Get department distribution
    dept_distribution = df["Department"].value_counts()
    
    return operations_count, dept_distribution

def create_visualizations(df, dept_distribution):
    """
    Create various visualizations for department analysis
    """
    # Set style for better looking plots
    plt.style.use('seaborn-v0_8')
    
    # Create figure with subplots
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(15, 12))
    
    # 1. Bar chart of department distribution
    dept_distribution.plot(kind='bar', ax=ax1, color='skyblue', edgecolor='black')
    ax1.set_title('Department Distribution', fontsize=14, fontweight='bold')
    ax1.set_xlabel('Departments', fontsize=12)
    ax1.set_ylabel('Number of Employees', fontsize=12)
    ax1.tick_params(axis='x', rotation=45)
    
    # Add value labels on bars
    for i, v in enumerate(dept_distribution.values):
        ax1.text(i, v + 0.1, str(v), ha='center', va='bottom', fontweight='bold')
    
    # 2. Pie chart
    colors = plt.cm.Set3(np.linspace(0, 1, len(dept_distribution)))
    ax2.pie(dept_distribution.values, labels=dept_distribution.index, autopct='%1.1f%%', 
            colors=colors, startangle=90)
    ax2.set_title('Department Distribution (Percentage)', fontsize=14, fontweight='bold')
    
    # 3. Horizontal bar chart
    dept_distribution.plot(kind='barh', ax=ax3, color='lightcoral', edgecolor='black')
    ax3.set_title('Department Distribution (Horizontal)', fontsize=14, fontweight='bold')
    ax3.set_xlabel('Number of Employees', fontsize=12)
    
    # 4. Salary distribution by department
    df.boxplot(column='Salary', by='Department', ax=ax4, grid=False)
    ax4.set_title('Salary Distribution by Department', fontsize=14, fontweight='bold')
    ax4.set_xlabel('Department', fontsize=12)
    ax4.set_ylabel('Salary ($)', fontsize=12)
    ax4.tick_params(axis='x', rotation=45)
    
    plt.tight_layout()
    plt.savefig('department_distribution.png', dpi=300, bbox_inches='tight')
    plt.show()

def generate_html_report(operations_count, dept_distribution, df):
    """
    Generate comprehensive HTML report
    """
    # Calculate additional statistics
    total_employees = len(df)
    operations_percentage = (operations_count / total_employees) * 100
    avg_salary_by_dept = df.groupby('Department')['Salary'].mean().round(2)
    
    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Employee Department Analysis Report</title>
        <style>
            body {{
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                line-height: 1.6;
                margin: 0;
                padding: 20px;
                background-color: #f5f5f5;
            }}
            .container {{
                max-width: 1200px;
                margin: 0 auto;
                background-color: white;
                padding: 30px;
                border-radius: 10px;
                box-shadow: 0 0 20px rgba(0,0,0,0.1);
            }}
            h1 {{
                color: #2c3e50;
                text-align: center;
                border-bottom: 3px solid #3498db;
                padding-bottom: 10px;
            }}
            h2 {{
                color: #34495e;
                margin-top: 30px;
            }}
            .highlight {{
                background-color: #ecf0f1;
                padding: 15px;
                border-radius: 5px;
                border-left: 4px solid #3498db;
                margin: 20px 0;
            }}
            .email-verification {{
                background-color: #e8f5e8;
                border: 1px solid #27ae60;
                padding: 10px;
                border-radius: 5px;
                margin: 20px 0;
            }}
            table {{
                width: 100%;
                border-collapse: collapse;
                margin: 20px 0;
            }}
            th, td {{
                border: 1px solid #ddd;
                padding: 12px;
                text-align: left;
            }}
            th {{
                background-color: #3498db;
                color: white;
            }}
            tr:nth-child(even) {{
                background-color: #f2f2f2;
            }}
            .visualization {{
                text-align: center;
                margin: 30px 0;
            }}
            .visualization img {{
                max-width: 100%;
                height: auto;
                border-radius: 10px;
                box-shadow: 0 4px 8px rgba(0,0,0,0.1);
            }}
            .footer {{
                text-align: center;
                margin-top: 40px;
                padding-top: 20px;
                border-top: 1px solid #ddd;
                color: #7f8c8d;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>📊 Employee Department Analysis Report</h1>
            
            <div class="email-verification">
                <strong>🔐 Email for Verification:</strong> 24f1001723@ds.study.iitm.ac.in
            </div>
            
            <div class="highlight">
                <h2>🎯 Key Findings</h2>
                <p><strong>Total Employees:</strong> {total_employees}</p>
                <p><strong>Operations Department Frequency:</strong> {operations_count} employees</p>
                <p><strong>Operations Department Percentage:</strong> {operations_percentage:.1f}%</p>
            </div>
            
            <h2>📈 Department Distribution</h2>
            <table>
                <tr>
                    <th>Department</th>
                    <th>Number of Employees</th>
                    <th>Percentage</th>
                </tr>
    """
    
    # Add department rows
    for dept, count in dept_distribution.items():
        percentage = (count / total_employees) * 100
        html_content += f"""
                <tr>
                    <td>{dept}</td>
                    <td>{count}</td>
                    <td>{percentage:.1f}%</td>
                </tr>
        """
    
    html_content += f"""
            </table>
            
            <h2>💰 Average Salary by Department</h2>
            <table>
                <tr>
                    <th>Department</th>
                    <th>Average Salary ($)</th>
                </tr>
    """
    
    # Add salary rows
    for dept, avg_salary in avg_salary_by_dept.items():
        html_content += f"""
                <tr>
                    <td>{dept}</td>
                    <td>${avg_salary:,.2f}</td>
                </tr>
        """
    
    html_content += f"""
            </table>
            
            <div class="visualization">
                <h2>📊 Department Distribution Visualizations</h2>
                <img src="department_distribution.png" alt="Department Distribution Charts">
            </div>
            
            <h2>📋 Raw Data Sample</h2>
            <table>
                <tr>
                    <th>Employee ID</th>
                    <th>Name</th>
                    <th>Department</th>
                    <th>Salary ($)</th>
                    <th>Years Experience</th>
                </tr>
    """
    
    # Add sample data rows (first 10 employees)
    for _, row in df.head(10).iterrows():
        html_content += f"""
                <tr>
                    <td>{row['Employee_ID']}</td>
                    <td>{row['Name']}</td>
                    <td>{row['Department']}</td>
                    <td>${row['Salary']:,.2f}</td>
                    <td>{row['Years_Experience']}</td>
                </tr>
        """
    
    html_content += f"""
            </table>
            
            <div class="footer">
                <p><strong>Report Generated:</strong> {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>
                <p>This analysis was performed using Python with pandas, matplotlib, and seaborn.</p>
            </div>
        </div>
    </body>
    </html>
    """
    
    return html_content

def main():
    """
    Main function to execute the complete analysis
    """
    print("🚀 Starting Employee Department Analysis...")
    print("📧 Email for verification: 24f1001723@ds.study.iitm.ac.in")
    print("-" * 50)
    
    # Load data
    print("📊 Loading employee data...")
    df = load_employee_data()
    print(f"✅ Loaded {len(df)} employee records")
    
    # Analyze departments
    print("🔍 Analyzing department distribution...")
    operations_count, dept_distribution = analyze_departments(df)
    
    # Print results to console
    print(f"\n📈 ANALYSIS RESULTS:")
    print(f"Total Employees: {len(df)}")
    print(f"Operations Department Frequency: {operations_count}")
    print(f"Operations Department Percentage: {(operations_count/len(df)*100):.1f}%")
    print(f"\nDepartment Distribution:")
    for dept, count in dept_distribution.items():
        print(f"  {dept}: {count} employees")
    
    # Create visualizations
    print("\n🎨 Creating visualizations...")
    create_visualizations(df, dept_distribution)
    print("✅ Visualizations saved as 'department_distribution.png'")
    
    # Generate HTML report
    print("📄 Generating HTML report...")
    html_content = generate_html_report(operations_count, dept_distribution, df)
    
    with open("employee_analysis.html", "w", encoding="utf-8") as f:
        f.write(html_content)
    
    print("✅ HTML report saved as 'employee_analysis.html'")
    print("\n🎉 Analysis complete! Files generated:")
    print("  - employee_analysis.html (Interactive report)")
    print("  - department_distribution.png (Visualizations)")
    print("\n📧 Email for verification: 24f1001723@ds.study.iitm.ac.in")

if __name__ == "__main__":
    main()
