from transformers import pipeline

import wikipedia
import warnings
import streamlit as st

warnings.filterwarnings("ignore")


def get_context_from_wiki(query: str) -> str:
  "Given a query, return the summary about the query from wikipedia"
  results = wikipedia.search(query)
  # There could be more than 1 due to Disambiguation issue
  try:
    summary = wikipedia.summary(results[0], sentences=10)
  except wikipedia.DisambiguationError as e:
    ambiguous_terms = e.options
    # take the first one from the list of ambiguous terms and try again
    return wikipedia.summary(ambiguous_terms[0], sentences=10)
  return summary


def get_qa_pipeline():
    qa_pipeline = pipeline("question-answering")
    return qa_pipeline


def answer_question(pipeline, question, context):
    result = pipeline(question=question, context=context)
    #return f"Answer: {result['answer']}, score: {round(result['score'], 4)}, start: {result['start']}, end: {result['end']}"
    return result


if __name__ == '__main__':

    st.title("Extractive Question Answering")
    pipeline = get_qa_pipeline()

    add_select_option = st.sidebar.selectbox(
    "Exploration Options", ("Query Based", "Paragraph based")
    )

    if add_select_option == "Query Based":
        paragraph_slot = st.empty()
        query = st.text_area("WIKI SEARCH TERM", "")
        if query:
            context = get_context_from_wiki(query)
            paragraph_slot.markdown(context)
    elif add_select_option == "Paragraph based":
        question = st.empty()
        context = st.text_area("Enter the paragraph to explore", value="...")
    
    question = st.text_input("QUESTION", "")
    # print(f"Context: {context}\n")
    # print(f"Question: {question}\n")
    # print(answer_question(pipeline, question=question, context=context))
    if question: 
        try:
            answer = answer_question(pipeline, question=question, context=context)
            st.write(answer['answer'])
        except:
            st.write("Provide a valid paragraph")
