from transformers import AutoTokenizer, pipeline, AutoModelForQuestionAnswering

model = AutoModelForQuestionAnswering.from_pretrained("./app/mobilebert-squad")
tokenizer = AutoTokenizer.from_pretrained("./app/mobilebert-squad")

qa_pipeline = pipeline(
    "question-answering",
    model=model,
    tokenizer=tokenizer
)

def get_answer(content, question):
    # content = _text.content
    print (question)
    predictions = qa_pipeline({
        'context': content,
        'question': question
    })
    print (predictions['score'])
    print (predictions['answer'])
    # if (predictions['score'] < 0.01):
    #     return "Sorry, Cannot find appropriate result."
    return (predictions['answer'])