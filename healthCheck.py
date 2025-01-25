from mira_sdk import MiraClient
import asyncio

# Initialize the client
client = MiraClient(config={"API_KEY": "sb-da7712c5542a2fcbaa0d336e42ca1a0a"})

version = "1.0.0"

def update_inputs(input):
    input_data = {
        "name": input[0],
        "age": input[1],
        "sex": input[2],
        "weight": input[3],
        "symptom1": input[4],
        "symptom2": "",
        "symptom3": ""
    }
    return input_data

# Determine the flow name
flow_name = f"@ayush1204/health-check-generator/{version}" if version else "@ayush1204/health-check-generator"

def print_screen(inputs):
    try:
        print("ok")
        result = client.flow.execute(flow_name, update_inputs(inputs))
        with open('output1.txt', 'w') as file:
            file.write(f"Flow execution result:")
            for key, value in result.items():
                file.write(f"{key}: {value}\n")
    except Exception as e:
        print("Error executing flow:", e)



