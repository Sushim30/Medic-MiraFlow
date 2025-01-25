from mira_sdk import MiraClient, Flow
import os

temp_result=""

# Initialize the client
client_health = MiraClient(config={"API_KEY": "sb-da7712c5542a2fcbaa0d336e42ca1a0a"})
client_extract = MiraClient(config={"API_KEY": "sb-2737248aa1b90f4e52dd568c7aeba00e"})
client_medP = MiraClient(config={"API_KEY": "sb-da7712c5542a2fcbaa0d336e42ca1a0a"})
version_extract = "1.0.0"
version_health = "1.0.0"

def update_inputs(input):
    input_data_health = {
        "name": input[0],
        "age": input[1],
        "sex": input[2],
        "weight": input[3],
        "symptom1": input[4],
        "symptom2": input[5],
        "symptom3": input[6]
    }
    return input_data_health

# If no version is provided, latest version is used by default
if version_health:
    flow_name_health = f"@ayush1204/health-check-generator/{version_health}"
else:
    flow_name_health = "@ayush1204/health-check-generator"

def print_screen(inputs):
    global diseases
    diseases = client_health.flow.execute(flow_name_health, update_inputs(inputs))
    disease_file = os.path.abspath("diseases.txt")
    with open('diseases.txt', 'w') as file:
        for key, value in diseases.items():
            file.write(f"{key}: {value}\n")
    os.startfile(disease_file)

    input_data_extract = {
        "text": diseases
    }

    # If no version is provided, latest version is used by default
    if version_extract:
        flow_name_extract = f"@random-nobody/text-extraction/{version_extract}"
    else:
        flow_name_extract = "@random-nobody/text-extraction"
    
    result = client_extract.flow.execute(flow_name_extract, input_data_extract)
    temp_result = result
    return result

version_medP = "1.0.0"

def update_disease(input,result):
    input_data_medP = {
        "age": input[1],
        "weight": input[3],
        "symptoms": result
    }
    return input_data_medP

# If no version is provided, latest version is used by default
if version_medP:
    flow_name_medP = f"@ayush1204/med-prescription-generator/{version_medP}"
else:
    flow_name_medP = "@ayush1204/med-prescription-generator"

def update_meds(inputs):
    global medicines
    medicines = client_medP.flow.execute(flow_name_medP, update_disease(inputs, temp_result))
    
    medP_file = os.path.abspath("medicine.txt")

    with open('medicine.txt', 'w') as file:
        for key, value in medicines.items():
            file.write(f"{key}: {value}\n")
    os.startfile(medP_file)
    return medicines
