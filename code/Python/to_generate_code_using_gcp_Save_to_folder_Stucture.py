import os
from google.cloud import aiplatform
from google.protobuf import json_format
from google.protobuf.struct_pb2 import Value  # Add this import

# Set the Google Cloud credentials path
credential_path = "C:\\Users\\bbaliram\\AppData\\Roaming\\gcloud\\application_default_credentials.json"
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = credential_path

# Initialize Vertex AI
vertexai.init(project="genai-loreal-sandbox", location="us-central1")

# Set your Vertex AI model name
model_name = "projects/{}/locations/us-central1/models/your-model".format(
    "your-project-id"
)

# Parameters for text generation model
parameters = {
    "candidate_count": 1,
    "max_output_tokens": 1000,
    "temperature": 0.2,
    "top_p": 0.8,
    "top_k": 40,
}

# Authenticate with Google Cloud
pipeline_client = aiplatform.gapic.PredictionServiceClient(
    client_options={"api_endpoint": "us-central1-prediction-aiplatform.googleapis.com"}
)


def generate_code_snippet(prompt, language):
    extension = ""
    if language == "Python":
        extension = ".py"
    elif language == "Java":
        extension = ".java"
    elif language == "C++":
        extension = ".cpp"
    elif language == "C#":
        extension = ".cs"
    elif language == "PHP":
        extension = ".php"
    elif language == "JavaScript":
        extension = ".js"
    # Add more cases for other programming languages if needed.

    code = ""
    while True:
        request_data = {
            "instances": [{"prompt": prompt, "language": language}],
            "parameters": parameters,  # Use the defined parameters
        }

        try:
            response = pipeline_client.predict(
                endpoint=model_name,
                instances=json_format.ParseDict(request_data, Value()),
            )
            code_fragment = response.predictions[0]["generated_code"]
            code += code_fragment

            if len(code) >= 4096:
                break  # Assume code is too long

        except Exception as e:
            print(f"Error generating code: {e}")
            break

    return code, extension


def save_code_snippet_to_folder(topic, language, extension, code):
    folder_name = f"{topic}_{language}_code"
    if not os.path.exists(folder_name):
        os.mkdir(folder_name)
    file_name = f"snippet{extension}"
    file_path = os.path.join(folder_name, file_name)
    with open(file_path, "w") as file:
        file.write(code)


if __name__ == "__main__":
    topic = input("Enter the topic for the code: ")

    languages = ["Python", "Java", "C++", "C#", "PHP", "JavaScript"]

    for language in languages:
        code, extension = generate_code_snippet(
            f"Generate a {language} code snippet for {topic}", language
        )
        if code:
            save_code_snippet_to_folder(topic, language, extension, code)
            print(
                f"{language} code snippet generated and saved in {topic}_{language}_code folder."
            )
        else:
            print(f"{language} code snippet generation failed.")
