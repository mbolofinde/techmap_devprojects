# Write your code here and merge with main branch 
import xml.etree.ElementTree as ET

# Load and parse the XML file
tree = ET.parse("sample.xml")
root = tree.getroot()

# Print root element
print("Root tag:", root.tag)

# Loop through elements
for employee in root.findall("employee"):
    emp_id = employee.get("id")
    name = employee.find("name").text
    department = employee.find("department").text
    salary = employee.find("salary").text

    print(f"ID: {emp_id}, Name: {name}, Department: {department}, Salary: {salary}")
