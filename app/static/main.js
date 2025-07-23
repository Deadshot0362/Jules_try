document.addEventListener('DOMContentLoaded', () => {
    const form = document.querySelector('form');
    form.addEventListener('submit', async (event) => {
        event.preventDefault();
        const url = document.querySelector('#url').value;
        const response = await fetch('/generate', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
            },
            body: `url=${encodeURIComponent(url)}`,
        });
        const chatbot = await response.json();
        const chatbotContainer = document.querySelector('#chatbot');
        const codeContainer = document.querySelector('#code');

        // Display the chatbot
        chatbotContainer.innerHTML = '';
        for (const [key, value] of Object.entries(chatbot)) {
            chatbotContainer.innerHTML += `<p><strong>${key}:</strong> ${value}</p>`;
        }

        // Display the code
        codeContainer.textContent = JSON.stringify(chatbot, null, 2);

        // Handle export button clicks
        const exportFlaskButton = document.querySelector('#export-flask');
        exportFlaskButton.addEventListener('click', () => {
            const code = generateFlaskCode(chatbot);
            downloadFile('app.py', code);
        });

        const exportStreamlitButton = document.querySelector('#export-streamlit');
        exportStreamlitButton.addEventListener('click', () => {
            const code = generateStreamlitCode(chatbot);
            downloadFile('app.py', code);
        });
    });
});

function generateFlaskCode(chatbot) {
    const chatbot_dict = JSON.stringify(chatbot, null, 2);
    return `
from flask import Flask, request, jsonify

app = Flask(__name__)

chatbot = ${chatbot_dict}

@app.route('/chat', methods=['POST'])
def chat():
    message = request.json['message'].lower()
    for key in chatbot:
        if key in message:
            return jsonify({'response': chatbot[key]})
    return jsonify({'response': "I'm sorry, I don't understand."})

if __name__ == '__main__':
    app.run(debug=True)
`;
}

function generateStreamlitCode(chatbot) {
    const chatbot_dict = JSON.stringify(chatbot, null, 2);
    return `
import streamlit as st

chatbot = ${chatbot_dict}

st.title("My Chatbot")

message = st.text_input("Enter your message:")

if message:
    for key in chatbot:
        if key in message.lower():
            st.write(chatbot[key])
            break
    else:
        st.write("I'm sorry, I don't understand.")
`;
}

function downloadFile(filename, text) {
    const element = document.createElement('a');
    element.setAttribute('href', 'data:text/plain;charset=utf-8,' + encodeURIComponent(text));
    element.setAttribute('download', filename);
    element.style.display = 'none';
    document.body.appendChild(element);
    element.click();
    document.body.removeChild(element);
}
