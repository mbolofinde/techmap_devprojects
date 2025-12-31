import xml.etree.ElementTree as ET
import pandas as pd

# -------------------------------------------------
# 1. Load and Parse XML File
# -------------------------------------------------
xml_file = "DataStage_Job_Inventory.xml"
tree = ET.parse(xml_file)
root = tree.getroot()

jobs_data = []

# -------------------------------------------------
# 2. Extract Job-Level Data
# -------------------------------------------------
for job in root.findall("Job"):
    job_record = {
        "Job ID": job.findtext("JobID"),
        "Job Name": job.findtext("JobName"),
        "Job Type": job.findtext("JobType"),
        "Category": job.findtext("Category"),

        "Source System": job.find("Source/System").text if job.find("Source/System") is not None else None,
        "Source Type": job.find("Source/Type").text if job.find("Source/Type") is not None else None,

        "Target System": job.find("Target/System").text if job.find("Target/System") is not None else None,
        "Target Type": job.find("Target/Type").text if job.find("Target/Type") is not None else None,

        "Transformations Used": job.find("TechnicalDetails/Transformations").text if job.find("TechnicalDetails/Transformations") is not None else None,
        "Stages Used": job.find("TechnicalDetails/StagesUsed").text if job.find("TechnicalDetails/StagesUsed") is not None else None,
        "Reusable Components": job.find("TechnicalDetails/ReusableComponents").text if job.find("TechnicalDetails/ReusableComponents") is not None else None,
        "Error Handling": job.find("TechnicalDetails/ErrorHandling").text if job.find("TechnicalDetails/ErrorHandling") is not None else None,

        "Dependencies": job.find("Operations/Dependencies").text if job.find("Operations/Dependencies") is not None else None,
        "Scheduling Tool": job.find("Operations/SchedulingTool").text if job.find("Operations/SchedulingTool") is not None else None,
        "Frequency": job.find("Operations/Frequency").text if job.find("Operations/Frequency") is not None else None,
        "Avg Runtime (mins)": job.find("Operations/AverageRuntimeMinutes").text if job.find("Operations/AverageRuntimeMinutes") is not None else None,
        "Data Volume": job.find("Operations/DataVolume").text if job.find("Operations/DataVolume") is not None else None,

        "Target Platform": job.find("Migration/TargetPlatform").text if job.find("Migration/TargetPlatform") is not None else None,
        "Migration Readiness": job.find("Migration/Readiness").text if job.find("Migration/Readiness") is not None else None,
        "Estimated Effort (Days)": job.find("Migration/EstimatedEffortDays").text if job.find("Migration/EstimatedEffortDays") is not None else None,
        "Migration Wave": job.find("Migration/MigrationWave").text if job.find("Migration/MigrationWave") is not None else None,
        "Risk Level": job.find("Migration/RiskLevel").text if job.find("Migration/RiskLevel") is not None else None,

        "Remarks": job.findtext("Remarks")
    }

    jobs_data.append(job_record)

# -------------------------------------------------
# 3. Write Parsed Data to Excel
# -------------------------------------------------
df = pd.DataFrame(jobs_data)

excel_output = "Parsed_DataStage_Job_Inventory.xlsx"
df.to_excel(excel_output, index=False, sheet_name="DataStage Job Inventory")

print("✔ XML successfully parsed and written to Excel")
print(f"✔ Output file: {excel_output}")
