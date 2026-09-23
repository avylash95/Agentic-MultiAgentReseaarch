from src.tools.tools import web_search, scrape_url
from src.pipeline.pipeline import run_research_pipeline

#result = web_search.invoke("What is the latest research on using AI for climate change mitigation?")
#print(result)

topic = "What is the latest research on using AI for climate change mitigation?"
run_research_pipeline(topic)