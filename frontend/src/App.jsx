import { useState } from "react";
import "./App.css";

function App() {
  const [role, setRole] = useState("data_analyst");
  const [file, setFile] = useState(null);
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);

    const formData = new FormData();
    formData.append("role", role);
    formData.append("resume", file);

    const response = await fetch("http://127.0.0.1:8000/analyze", {
      method: "POST",
      body: formData,
    });

    const data = await response.json();
    setResult(data);
    setLoading(false);
  };

  return (
    <div className="container">
      <div className="header">
        <h1>AI Career Copilot</h1>
        <p>Personalized career guidance using AI</p>
      </div>

      <form className="form" onSubmit={handleSubmit}>
        <select value={role} onChange={(e) => setRole(e.target.value)}>
          <option value="data_analyst">Data Analyst</option>
          <option value="software_developer">Software Developer</option>
        </select>

        <input
          type="file"
          accept=".pdf"
          onChange={(e) => setFile(e.target.files[0])}
          required
        />

        <button type="submit">
          {loading ? "Analyzing..." : "Analyze Resume"}
        </button>
      </form>

      {result && (
        <>





        <div
  className={`score ${
    result.confidence_score >= 60 ? "good" : "bad"
  }`}
>
  Career Readiness Score: {result.confidence_score}%

  <div className="progress">
    <div
      className="progress-bar"
      style={{ width: `${result.confidence_score}%` }}
    ></div>
  </div>
</div>


          <div className="ai-message">{result.ai_message}</div>

          <Section title="Resume Skills">
            {result.resume_skills.map((s, i) => (
              <span key={i} className="tag">{s}</span>
            ))}
          </Section>

          <Section title="Matched Skills">
            {result.matched_skills.map((s, i) => (
              <span key={i} className="tag green">{s}</span>
            ))}
          </Section>

          <Section title="Missing Skills">
            {result.missing_skills.map((s, i) => (
              <span key={i} className="tag red">{s}</span>
            ))}
          </Section>

          <Section title="7-Day Learning Plan">
            <div className="cards">
              {Object.entries(result.learning_plan).map(([day, task], i) => (
                <div key={i} className="card">
                  <strong>{day}</strong>
                  <p>{task}</p>
                </div>
              ))}
            </div>
          </Section>
        </>
      )}
    </div>
  );
}

const Section = ({ title, children }) => (
  <div className="section">
    <h3>{title}</h3>
    <div className="tags">{children}</div>
  </div>
);

export default App;
