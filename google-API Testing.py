from langchain_google_genai import ChatGoogleGenerativeAI

# Initialize the Gemini model using Vertex AI and your cloud credentials
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash", 
    vertexai=True,
    project="project-e8dae987-b246-4a9a-a28"  # Replace with your actual Google Cloud Project ID
)

# Test the model
response = llm.invoke("Hello, Gemini! write a 100 word story about a brave cat who saves its owner from a fire.")
print(response.content)