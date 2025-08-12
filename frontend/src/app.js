import React from "react";
import "./app.css";

function App() {
  return (
    <div className="app-container">
      <header>
        <h1>📊 InsightStream</h1>
        <p>Real-time product insights and analytics.</p>
      </header>

      <section className="content">
        <div className="card">
          <h2>API Status</h2>
          <p>Connected to backend for live updates.</p>
        </div>
        <div className="card">
          <h2>Event Tracking</h2>
          <p>Track user events in real-time with precision.</p>
        </div>
        <div className="card">
          <h2>Data Visualization</h2>
          <p>Turn data into actionable insights instantly.</p>
        </div>
      </section>

      <footer>
        <p>© {new Date().getFullYear()} InsightStream</p>
      </footer>
    </div>
  );
}

export default App;