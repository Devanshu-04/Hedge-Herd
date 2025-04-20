/*
import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import smallLogo from "Small.png";
import accountIcon from "HedgeHerdOfficial.png";

// Dummy database for demonstration
const dummyDatabase = {
  "user@example.com": "password123"
};

// Main landing page component
const LandingPage = () => {
  return (
    <div className="landing-container">
      <header className="gradient-header">
        <img 
          src={mainLogo} 
          alt="HedgeHerd Logo" 
          className="main-logo" 
        />
      </header>
      <main className="landing-content">
        <h1>Welcome to HedgeHerd!</h1>
        <div className="button-container">
          <Link to="/login">
            <button className="login-button">Log In</button>
          </Link>
          <Link to="/signup">
            <button className="signup-button">Sign Up</button>
          </Link>
        </div>
      </main>
    </div>
  );
};

// Authentication component (used for both login and signup)
const AuthPage = ({ isSignUp }) => {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");
  const [redirectToHome, setRedirectToHome] = useState(false);

  const handleAuth = (e) => {
    e.preventDefault();
    setError("");

    if (!username || !password) {
      setError("Please enter both username and password.");
      return;
    }

    if (isSignUp) {
      if (dummyDatabase[username]) {
        setError("Username already registered.");
      } else {
        dummyDatabase[username] = password; // In production, hash the password!
        setError("");
        alert("Sign up successful!");
        setRedirectToHome(true);
      }
    } else {
      if (dummyDatabase[username] === password) {
        setError("");
        alert("Login successful!");
        setRedirectToHome(true);
      } else {
        setError("Invalid username or password.");
      }
    }
  };

  if (redirectToHome) {
    return <Navigate to="/home" />;
  }

  return (
    <div className="auth-container">
      <header className="light-header">
        <img 
          src={smallLogo} 
          alt="HedgeHerd Small Logo" 
          className="small-logo" 
        />
      </header>
      <main className="auth-content">
        <h2>{isSignUp ? "Sign Up" : "Log In"}</h2>
        <form onSubmit={handleAuth}>
          {error && <div className="error-message">{error}</div>}
          <div className="form-group">
            <label htmlFor="username">Username</label>
            <input
              type="text"
              id="username"
              value={username}
              onChange={(e) => setUsername(e.target.value)}
              required
            />
          </div>
          <div className="form-group">
            <label htmlFor="password">Password</label>
            <input
              type="password"
              id="password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              required
            />
          </div>
          <button type="submit" className="auth-button">
            {isSignUp ? "Sign Up" : "Log In"}
          </button>
        </form>
      </main>
    </div>
  );
};

// Home page component (blank as required)
const HomePage = () => {
  return (
    <div className="home-container">
      <header className="light-header">
        <img 
          src={smallLogo} 
          alt="HedgeHerd Small Logo" 
          className="small-logo" 
        />
      </header>
      <main className="home-content">
        <h2>Welcome to HedgeHerd Dashboard</h2>
      </main>
    </div>
  );
};

export default MainPageContent;


*/