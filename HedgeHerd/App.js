// App.js

import React, { useState } from "react";
import "./App.css";

// Dummy logo, replace with your own if available
const logoUrl = "https://dummyimage.com/48x48/cccccc/000000&text=Logo";

const dummyDatabase = {
  "user@example.com": "password123"
};

function App() {
  const [isSignUp, setIsSignUp] = useState(false);
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");

  const handleAuth = (e) => {
    e.preventDefault();
    setError("");

    if (!email || !password) {
      setError("Please enter both email and password.");
      return;
    }

    // Simple email format validation
    if (!/\S+@\S+\.\S+/.test(email)) {
      setError("Please enter a valid email address.");
      return;
    }

    if (isSignUp) {
      if (dummyDatabase[email]) {
        setError("Email already registered.");
      } else {
        dummyDatabase[email] = password; // In production, hash the password!
        setError("");
        alert("Sign up successful! Redirecting to dashboard...");
        // Redirect logic here
      }
    } else {
      if (dummyDatabase[email] === password) {
        setError("");
        alert("Login successful! Redirecting to dashboard...");
        // Redirect logic here
      } else {
        setError("Invalid email or password.");
      }
    }
  };

  return (
    <div className="auth-container">
      <img src={logoUrl} alt="Logo" className="auth-logo" />
      <div className="auth-title">{isSignUp ? "Sign Up" : "Log In"}</div>
      <form onSubmit={handleAuth} style={{ width: "100%" }}>
        <input
          className="auth-input"
          type="email"
          placeholder="Email"
          value={email}
          onChange={e => setEmail(e.target.value)}
          autoComplete="username"
        />
        <input
          className="auth-input"
          type="password"
          placeholder="Password"
          value={password}
          onChange={e => setPassword(e.target.value)}
          autoComplete={isSignUp ? "new-password" : "current-password"}
        />
        {error && <div className="auth-error">{error}</div>}
        <button className="auth-button" type="submit">
          {isSignUp ? "Sign Up" : "Log In"}
        </button>
      </form>
      <div>
        {isSignUp ? (
          <span>
            Already have an account?
            <button className="auth-toggle" onClick={() => setIsSignUp(false)}>
              Log In
            </button>
          </span>
        ) : (
          <span>
            Don't have an account?
            <button className="auth-toggle" onClick={() => setIsSignUp(true)}>
              Sign Up
            </button>
          </span>
        )}
      </div>
    </div>
  );
}

export default App;


