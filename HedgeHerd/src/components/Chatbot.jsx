import React, { useState } from "react";
import axios from "axios";

const ChatGPT = () => {
  const [message, setMessage] = useState("");
  const [reply, setReply] = useState("");

  const sendMessage = async () => {
    try {
      const res = await axios.post("http://localhost:5173/chat", {
        message: message,
      });
      setReply(res.data.reply);
    } catch (error) {
      setReply("Error: " + error.message);
    }
  };

  return (
    <div>
      <h2>Chat with GPT</h2>
      <input
        type="text"
        value={message}
        onChange={(e) => setMessage(e.target.value)}
        placeholder="Type your message..."
      />
      <button onClick={sendMessage}>Send</button>
      <p><strong>GPT:</strong> {reply}</p>
    </div>
  );
};

export default ChatGPT;
