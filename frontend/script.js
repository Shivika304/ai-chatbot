const sendBtn = document.getElementById("send-btn");

const userInput = document.getElementById("user-input");

const chatBox = document.getElementById("chat-box");


// ----------------------------------
// Add Message To Chat UI
// ----------------------------------
function addMessage(message, className) {

    const messageDiv = document.createElement("div");

    messageDiv.classList.add("message", className);

    messageDiv.textContent = message;

    chatBox.appendChild(messageDiv);

    // Auto scroll to latest message
    chatBox.scrollTop = chatBox.scrollHeight;
}


// ----------------------------------
// Send Message To Backend
// ----------------------------------
async function sendMessage() {

    const message = userInput.value.trim();

    if (message === "") return;

    // Add user message
    addMessage(message, "user-message");

    // Clear input
    userInput.value = "";

    try {

        // Send request to Flask backend
        const response = await fetch("http://127.0.0.1:5000/chat", {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                message: message
            })

        });

        const data = await response.json();

        // Add bot response
        addMessage(data.response, "bot-message");

    } catch (error) {

        addMessage("Error connecting to server.", "bot-message");

        console.log(error);
    }
}


// ----------------------------------
// Button Click Event
// ----------------------------------
sendBtn.addEventListener("click", sendMessage);


// ----------------------------------
// Enter Key Support
// ----------------------------------
userInput.addEventListener("keypress", function(event) {

    if (event.key === "Enter") {
        sendMessage();
    }

});