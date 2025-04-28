import gradio as gr
def load_function_from_file(filepath, func_name):
    local_vars = {}
    with open(filepath, 'r', encoding='utf-8') as file:
        code = file.read()
    exec(code, {}, local_vars)
    return local_vars.get(func_name)
answer_question_gemini = load_function_from_file(
    r'C:\Users\KIIT\Desktop\Projects\Summarise and Ask\q_a.py',
    'answer_question_gemini'
)
summarize_text = load_function_from_file(
    r'C:\Users\KIIT\Desktop\Projects\Summarise and Ask\summarize.py',
    'summarize_text'
)

def load_api_key(filepath=r'C:\Users\KIIT\Desktop\Projects\Summarise and Ask\gemini_api_key.txt'):
    try:
        with open(filepath, 'r') as f:
            return f.read().strip()
    except Exception as e:
        return f"Error loading API Key: {e}"
api_key = load_api_key()

def qa_interface(question):
    if not api_key:
        return "API Key not loaded."
    return answer_question_gemini(question, api_key)

def summarize_interface(text):
    return summarize_text(text)

with gr.Blocks() as demo:
    gr.Markdown("Text Assistant: Q&A and Summarization")

    with gr.Tab("Question Answering"):
        question_input = gr.Textbox(label="Enter your question:", lines=2)
        answer_output = gr.Textbox(label="Answer")
        ask_button = gr.Button("Get Answer")
        ask_button.click(fn=qa_interface, inputs=question_input, outputs=answer_output)

    with gr.Tab("Summarization"):
        text_input = gr.Textbox(label="Enter text to summarize:", lines=8)
        summary_output = gr.Textbox(label="Summary")
        summarize_button = gr.Button("Summarize")
        summarize_button.click(fn=summarize_interface, inputs=text_input, outputs=summary_output)
demo.launch(inbrowser=True)