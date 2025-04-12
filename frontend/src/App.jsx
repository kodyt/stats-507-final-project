import { useState, useEffect } from "react";
import "./App.css";
import axios from "axios";

function App() {
  const [codeInput, setCodeInput] = useState("");
  const [textInput, setTextInput] = useState("");
  const [response, setResponse] = useState("");
  const [loading, setLoading] = useState(false);
  const [darkMode, setDarkMode] = useState(true);

  useEffect(() => {
    document.body.className = darkMode ? "dark" : "light";
  }, [darkMode]);

  const handleSubmit = async () => {
    setLoading(true);
    console.log("Submitting code and question...");
    try {
      const res = await axios.post("http://localhost:8000/api/ask", {
        question: textInput,
        code: codeInput,
      });

      setResponse(res.data.answer || "No response");
    } catch (error) {
      console.error("Error submitting data:", error);
      setResponse("An error occurred while processing your request.");
    } finally {
      setLoading(false);
    }
  };


  return (
    <div className="app">
      <header className="header">
        <h1 className="title">AI Coding Tutor</h1>
        {/* <button className="mode-toggle" onClick={() => setDarkMode(!darkMode)}>
          {darkMode ? "🌞 Light" : "🌙 Dark"}
        </button> */}
      </header>

      <main className="main">
        <div className="input-section">
          <textarea
            className="code-box"
            value={codeInput}
            onChange={(e) => setCodeInput(e.target.value)}
            placeholder="Paste your code here..."
          />
          <input
            className="question-box"
            value={textInput}
            onChange={(e) => setTextInput(e.target.value)}
            placeholder="Ask a question about your code..."
          />
          <button className="submit-btn" onClick={handleSubmit} disabled={loading}>
            {loading ? "Thinking..." : "Submit"}
          </button>
        </div>

        <div className="output-section">
          <h2 className="response-title">AI Response</h2>
          <pre className="response-box">{response}</pre>
        </div>
      </main>
    </div>
  );
}

export default App;
