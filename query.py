import argparse

from chromadb import PersistentClient
from langchain_community.vectorstores import Chroma
from langchain_core.prompts import PromptTemplate
from langchain_openai import OpenAIEmbeddings, OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

CHROMA_PATH = "chroma"

PROMPT_TEMPLATE_EN = """
Answer the question based only on the following context:

{context}

---

Answer the question based on the above context: {question}
"""

PROMPT_TEMPLATE_AR = """
اجب عن هذا السؤال باستخدام السياق الآتي:

{context}

---

السؤال المراد الاجابة عليه كالتالى: {question}
"""

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("query_text", type=str, help="The query text.")
    parser.add_argument("lang", type=str, help="The language to answer.")
    args = parser.parse_args()

    query_text = args.query_text
    lang = "en" if args.lang == "en" else "ar"

    embedding_function = OpenAIEmbeddings(model="text-embedding-3-small",
                                          openai_api_key=os.environ['OPENAI_KEY'])
    # Load the existing database.
    db = Chroma(
        client=PersistentClient(),
        persist_directory=CHROMA_PATH,
        embedding_function=embedding_function
    )
    # Search the DB.
    results = db.similarity_search_with_relevance_scores(query_text, k=5)

    context_text = "\n\n---\n\n".join([doc.page_content for doc, _score in results])
    prompt_template = PromptTemplate.from_template(PROMPT_TEMPLATE_EN if lang == "en" else PROMPT_TEMPLATE_AR)
    prompt = prompt_template.format(context=context_text, question=query_text)
    print(prompt)

    model = OpenAI(
        openai_api_key=os.environ['OPENAI_KEY'],
    )
    response_text = model.invoke(prompt)

    sources = [doc.metadata.get("source", None) for doc, _score in results]
    formatted_response = f"Response: {response_text}\nSources: {sources}"
    print(formatted_response)


if __name__ == "__main__":
    main()
