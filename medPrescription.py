from mira_sdk import MiraClient, Flow

# Initialize the client
client = MiraClient(config={"API_KEY": "sb-da7712c5542a2fcbaa0d336e42ca1a0a"})
answer = ""
version = "1.0.0"
def updateInputs(input):
    input_data = {
        "age": input[1],
        "weight": input[3],
        "symptoms": input[5]
    }
    return input_data

# If no version is provided, latest version is used by default
if version:
    flow_name = f"@ayush1204/med-prescription-generator/{version}"
else:
    flow_name = "@ayush1204/med-prescription-generator"

def printMedPresc(inputs):
    print(inputs)
    result = client.flow.execute(flow_name, updateInputs(inputs))
    print(result)
    answer = result



with open('output2.txt', 'w') as file:
    for key, value in answer.items():
        file.write(f"{key}: {value}\n")