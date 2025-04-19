/*
import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import smallLogo from "Small.png";
import accountIcon from "HedgeHerdOfficial.png";

// For demo purposes only! Never store passwords like this in production.
const dummyDatabase = {
  "user@example.com": "password123"
};

const MainPageContent = () => {
  const navigate = useNavigate();
  const [isSignUp, setIsSignUp] = useState(false);
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");

  const handleAuth = () => {
    setError(""); // Clear previous errors

    if (!email || !password) {
      setError("Please enter both email and password.");
      return;
    }

    if (isSignUp) {
      if (dummyDatabase[email]) {
        setError("Email already registered.");
      } else {
        dummyDatabase[email] = password; // In production, hash the password!
        navigate("/dashboard");
      }
    } else {
      if (dummyDatabase[email] === password) {
        navigate("/dashboard");
      } else {
        setError("Invalid email or password");
      }
    }
  };

  return (
    <div>
      <img src={smallLogo} alt="Logo" />
      <img src={accountIcon} alt="Account" />
      <h2>{isSignUp ? "Sign Up" : "Log In"}</h2>
      <input
        type="email"
        placeholder="Email"
        value={email}
        onChange={e => setEmail(e.target.value)}
      />
      <input
        type="password"
        placeholder="Password"
        value={password}
        onChange={e => setPassword(e.target.value)}
      />
      {error && <div style={{ color: "red" }}>{error}</div>}
      <button onClick={handleAuth}>
        {isSignUp ? "Sign Up" : "Log In"}
      </button>
      <div>
        {isSignUp ? (
          <span>
            Already have an account?{" "}
            <button onClick={() => setIsSignUp(false)}>Log In</button>
          </span>
        ) : (
          <span>
            Don't have an account?{" "}
            <button onClick={() => setIsSignUp(true)}>Sign Up</button>
          </span>
        )}
      </div>
    </div>
  );
};

export default MainPageContent;


*/