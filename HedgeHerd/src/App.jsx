import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';

function Home() {
  return <h2>Home Page</h2>;
}

function Tab1() {
  return <h2>Tab 1 (Empty)</h2>;
}

function Tab2() {
  return <h2>Tab 2 (Empty)</h2>;
}

function LoginSignup() {
  return <h2>Login / Signup Page</h2>;
}

function App() {
  return (
    <Router>
      <nav style={{
        padding: '12px 24px',
        background: '#f0f0f0',
        display: 'flex',
        justifyContent: 'space-between',
        alignItems: 'center',
        boxShadow: '0 2px 4px rgba(0,0,0,0.1)'
      }}>
        {/* Left buttons */}
        <div style={{ display: 'flex', gap: '10px' }}>
          <Link to="/" style={bubbleStyle}>Home</Link>
          <Link to="/tab1" style={bubbleStyle}>Tab 1</Link>
          <Link to="/tab2" style={bubbleStyle}>Tab 2</Link>
        </div>

        {/* Right button */}
        <Link to="/login" style={{ ...bubbleStyle, background: '#007bff', color: 'white' }}>
          Login / Signup
        </Link>
      </nav>

      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/tab1" element={<Tab1 />} />
        <Route path="/tab2" element={<Tab2 />} />
        <Route path="/login" element={<LoginSignup />} />
      </Routes>
    </Router>
  );
}

// Bubble style
const bubbleStyle = {
  padding: '8px 16px',
  borderRadius: '20px',
  background: '#e0e0e0',
  textDecoration: 'none',
  color: 'black',
  fontWeight: 'bold',
  transition: '0.3s',
};

export default App;