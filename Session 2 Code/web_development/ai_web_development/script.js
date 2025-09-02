// Get elements
const chatOutput = document.getElementById("chat-output");
const userInput = document.getElementById("user-input");
const sendButton = document.getElementById("send-button");

// Event listener for the send button
sendButton.addEventListener("click", sendMessage);

// Function to send a message
function sendMessage() {
  const message = userInput.value.trim();
  if (message === "") return;

  // Display user's message
  const userMessageElement = document.createElement("div");
  userMessageElement.className = "message user-message";
  userMessageElement.textContent = "You: " + message;
  chatOutput.appendChild(userMessageElement);

  // Clear input
  userInput.value = "";

  // Simulate AI response
  // ... existing code ...

// Simulate AI response
setTimeout(() => {
  // Text response
  const aiMessageElement = document.createElement("div");
  aiMessageElement.className = "message ai-message";
  aiMessageElement.textContent = "AI: Here's an image for you.";
  chatOutput.appendChild(aiMessageElement);

  // Image response
  const aiImageElement = document.createElement("img");
  aiImageElement.src = "https://via.placeholder.com/150";
  aiImageElement.alt = "Dummy AI Image";
  aiImageElement.style.maxWidth = "100%";
  chatOutput.appendChild(aiImageElement);

  // Scroll to the bottom
  chatOutput.scrollTop = chatOutput.scrollHeight;
}, 500);

}

// Allow pressing Enter to send a message
userInput.addEventListener("keypress", function (e) {
  if (e.key === "Enter") {
    sendMessage();
  }
});
