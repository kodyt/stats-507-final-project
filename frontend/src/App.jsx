import { useState } from "react";
import "./App.css";
import axios from "axios";
import TutorIcon from "./assets/tutor_icon.svg";

function App() {
  const [codeInput, setCodeInput] = useState("");
  const [textInput, setTextInput] = useState("");
  const [response, setResponse] = useState("");
  const [loading, setLoading] = useState(false);

  document.body.className = "dark";

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

  const handleExampleClick = (code, question) => {
    setCodeInput(code);
    setTextInput(question);
    setResponse("");
  };

  return (
    <div className="app">
      {loading && <div className="loading-bar" />}
      <header className="header">
        <div className="title-container">
          <img src={TutorIcon} alt="AI Coding Tutor Icon" className="tutor-icon" />
          <h1 className="title">AI Python Coding Tutor</h1>
        </div>
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

        <div className="example-panel">
          <h3>Examples</h3>

          <div
            className="example"
            onClick={() =>
              handleExampleClick(
                `def factorial(n):\n  if n == 0:\n    return 1\n  return n * factorial(n - 1)`,
                "What does this function do?"
              )
            }
          >
            <pre>
{`def factorial(n):
  if n == 0:
    return 1
  return n * factorial(n - 1)`}
            </pre>
            <p><strong>Question:</strong> What does this function do?</p>
          </div>

          <div
            className="example"
            onClick={() =>
              handleExampleClick(
                `def is_even(n):\n  return n % 2 == 0`,
                "How does this function work?"
              )
            }
          >
            <pre>
{`def is_even(n):
    return n % 2 == 0`}
            </pre>
            <p><strong>Question:</strong> How does this function work?</p>
          </div>
        </div>
      </main>
    </div>
  );
}

export default App;
