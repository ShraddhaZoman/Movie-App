# =========================
# Software Quality Management Script for MERN Movies App
# =========================

import datetime

project_name = "MERN Movies App"
total_lines_of_code = 8000  # Example LOC for frontend + backend

# Defects aligned with your app modules
defects = [
    {"id": 1, "module": "Register", "severity": "High", "description": "Name field allows invalid characters", "status": "Closed"},
    {"id": 2, "module": "Login", "severity": "High", "description": "Login fails with correct credentials intermittently", "status": "Open"},
    {"id": 3, "module": "CreateMovie", "severity": "Medium", "description": "Image upload fails for large files", "status": "Open"},
    {"id": 4, "module": "GenreList", "severity": "Low", "description": "Delete confirmation modal not shown", "status": "Closed"},
    {"id": 5, "module": "MoviesList", "severity": "Medium", "description": "Sorting by rating not working", "status": "Open"},
]

# Function to calculate defect density
def calculate_defect_density(total_defects, loc):
    return total_defects / loc * 1000  # defects per KLOC

# Function to generate SQM report
def generate_quality_report(defects, loc):
    total_defects = len(defects)
    open_defects = len([d for d in defects if d['status'] == "Open"])
    closed_defects = len([d for d in defects if d['status'] == "Closed"])
    defect_density = calculate_defect_density(total_defects, loc)

    report = f"""
    ================================
    Software Quality Management Report
    Project: {project_name}
    Date: {datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
    ================================

    Total Lines of Code (LOC): {loc}
    Total Defects Logged: {total_defects}
    Open Defects: {open_defects}
    Closed Defects: {closed_defects}
    Defect Density (per KLOC): {defect_density:.2f}

    Defect Details:
    """
    for d in defects:
        report += f"\n  - ID: {d['id']}, Module: {d['module']}, Severity: {d['severity']}, Status: {d['status']}, Description: {d['description']}"

    return report

# Generate and print the quality report
print(generate_quality_report(defects, total_lines_of_code))
