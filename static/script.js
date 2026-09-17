const form = document.getElementById('chat-form');
const input = document.getElementById('message');
const chat = document.getElementById('chat');

function addMessage(text, type) {
  const div = document.createElement('div');
  div.className = `message ${type}`;
  div.textContent = text;
  chat.appendChild(div);
  chat.scrollTop = chat.scrollHeight;
}

function useSuggestion(text) {
  input.value = text;
  form.requestSubmit();
}

form.addEventListener('submit', async (event) => {
  event.preventDefault();
  const message = input.value.trim();
  if (!message) return;

  addMessage(message, 'user');
  input.value = '';

  try {
    const response = await fetch('/api/chat', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ message })
    });
    const data = await response.json();
    addMessage(data.reply || 'Sorry, I could not process that request.', 'bot');
  } catch (error) {
    addMessage('Connection error. Please try again.', 'bot');
  }
});
