import React, { useState } from "react";
import axios from "axios";

const ChatGPT = () => {
  const [message, setMessage] = useState("");
  const [chatHistory, setChatHistory] = useState([
    { role: "system", content: "You are a helpful assistant." }
  ]);

  const sendMessage = async () => {
    if (!message.trim()) return;

    // Add the user's message to the history
    const updatedHistory = [
      ...chatHistory,
      { role: "user", content: message }
    ];

    try {
      const res = await axios.post("http://localhost:5000/chat", {
        messages: updatedHistory
      });

      // Add the assistant's reply to the history
      const newHistory = [
        ...updatedHistory,
        { role: "assistant", content: res.data.reply }
      ];

      setChatHistory(newHistory);
      setMessage(""); // clear input
    } catch (error) {
      const errorReply = { role: "assistant", content: "Error: " + error.message };
      setChatHistory([...updatedHistory, errorReply]);
    }
  };

  return (
    <div>
      <h2>Chat with GPT</h2>

      <div style={{ border: "1px solid #ccc", padding: "1em", height: "300px", overflowY: "auto", marginBottom: "1em" }}>
        {chatHistory
          .filter(msg => msg.role !== "system")
          .map((msg, index) => (
            <div key={index}>
              <strong>{msg.role === "user" ? "You" : "GPT"}:</strong> {msg.content}
            </div>
          ))}
      </div>

      <input
        type="text"
        value={message}
        onChange={(e) => setMessage(e.target.value)}
        placeholder="Type your message..."
      />
      <button onClick={sendMessage}>Send</button>
    </div>
  );
};

export default ChatGPT;
