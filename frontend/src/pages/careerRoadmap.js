import React, { useState } from "react";
import axios from "axios";
import { motion } from "framer-motion";
import { ArrowDownCircle } from "lucide-react";
import { useNavigate } from "react-router-dom";


const CareerRoadmap = () => {
  const [form, setForm] = useState({
    career_goal: "",
    education: "",
    skills: "",
  });
  const [roadmap, setRoadmap] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");
  const [success, setSuccess] = useState("");
  const navigate = useNavigate();


  const handleChange = (e) =>
    setForm({ ...form, [e.target.name]: e.target.value });

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setError("");
    setSuccess("");
    setRoadmap([]);

    try {
      const token = localStorage.getItem("token");
      if (!token) {
        setError("You must log in first.");
        setLoading(false);
        return;
      }

      const response = await axios.post(
        "http://127.0.0.1:5000/api/roadmap",
        form,
        {
          headers: {
            "Content-Type": "application/json",
            Authorization: `Bearer ${token}`,
          },
        }
      );

      if (response.data?.roadmap?.length > 0) {
        setRoadmap(response.data.roadmap);
        setSuccess("✅ Career roadmap generated successfully!");
      } else {
        setError("No roadmap data received from the server.");
      }
    } catch (err) {
      console.error("Error generating roadmap:", err);
      setError("Network or server error. Please try again later.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="container py-5 px-3">
      <div className="text-start mb-3">
        <button
          onClick={() => navigate("/dashboard")}
          className="btn btn-sm text-white fw-semibold shadow-sm"
          style={{
            backgroundColor: "#6040AB",
            borderRadius: "8px",
          }}
        >
          ← Back to Dashboard
        </button>
      </div>


      <div className="text-center mb-4">
        <h2 className="fw-bold text-purple-700 text-3xl md:text-4xl">
          Career Roadmap Generator
        </h2>
        <p className="text-gray-500 mt-2">
          Get a personalized roadmap — with courses, schools, and milestones to
          reach your goal
        </p>
      </div>

      <form
        onSubmit={handleSubmit}
        className="mx-auto bg-white shadow-md rounded-2xl p-4 md:p-5"
        style={{ maxWidth: "600px" }}
      >
        <div className="mb-3">
          <label className="form-label fw-semibold">Career Goal</label>
          <input
            type="text"
            name="career_goal"
            className="form-control"
            placeholder="e.g. Software Engineer"
            onChange={handleChange}
            required
          />
        </div>

        <div className="mb-3">
          <label className="form-label fw-semibold">Education</label>
          <input
            type="text"
            name="education"
            className="form-control"
            placeholder="e.g. Bachelor's in Computer Science"
            onChange={handleChange}
            required
          />
        </div>

        <div className="mb-4">
          <label className="form-label fw-semibold">
            Skills (comma separated)
          </label>
          <input
            type="text"
            name="skills"
            className="form-control"
            placeholder="e.g. Python, JavaScript, SQL"
            onChange={handleChange}
            required
          />
        </div>

        <button
          type="submit"
          className="btn w-100 text-white py-2 fw-semibold"
          style={{
            backgroundColor: "#6040AB",
            borderRadius: "10px",
            letterSpacing: "0.5px",
          }}
          disabled={loading}
        >
          {loading ? "Generating roadmap..." : "Generate Roadmap"}
        </button>
      </form>

      {error && (
        <div className="alert alert-danger text-center mt-4">{error}</div>
      )}
      {success && (
        <div className="alert alert-success text-center mt-4">{success}</div>
      )}

      {/* Display Roadmap */}
      {roadmap.length > 0 && (
        <div className="mt-5">
          <h4 className="text-center mb-4 text-purple-700 fw-bold">
            Your Personalized Career Roadmap
          </h4>

          <div className="d-flex flex-column align-items-center position-relative">
            {roadmap.map((step, index) => (
              <React.Fragment key={index}>
                <motion.div
                  initial={{ opacity: 0, y: 20 }}
                  animate={{ opacity: 1, y: 0 }}
                  transition={{ delay: index * 0.2 }}
                  className="card shadow-lg border-0 mb-4 w-100"
                  style={{
                    maxWidth: "700px",
                    borderRadius: "16px",
                    background:
                      "linear-gradient(145deg, #ffffff, #f8f9fa 80%, #f0e8ff)",
                  }}
                >
                  <div className="card-body p-4">
                    <h5 className="card-title text-purple-700 fw-bold">
                      Step {step.step || index + 1}: {step.milestone}
                    </h5>
                    {step.details && (
                      <p className="card-text text-muted mb-2">{step.details}</p>
                    )}

                    {/* Optional course or school recommendations */}
                    {step.suggestions && (
                      <div className="mt-3">
                        <h6 className="fw-semibold text-secondary">
                          Recommended Paths:
                        </h6>
                        <ul className="mb-0">
                          {step.suggestions.map((s, i) => (
                            <li key={i} className="text-sm text-muted">
                              🎓 {s}
                            </li>
                          ))}
                        </ul>
                      </div>
                    )}
                  </div>
                </motion.div>

                {/* Dotted connecting arrow */}
                {index < roadmap.length - 1 && (
                  <div className="d-flex justify-content-center mb-3">
                    <ArrowDownCircle
                      size={30}
                      color="#6040AB"
                      strokeWidth={1.5}
                      style={{ opacity: 0.7, borderBottom: "2px dotted #6040AB" }}
                    />
                  </div>
                )}
              </React.Fragment>
            ))}
          </div>
        </div>
      )}
    </div>
  );
};

export default CareerRoadmap;
