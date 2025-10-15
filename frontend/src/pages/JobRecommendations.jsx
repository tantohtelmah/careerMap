import React, { useEffect, useState } from "react";
import axios from "axios";
import { Briefcase, Loader2 } from "lucide-react";
import AppSidebar from "../components/AppSidebar";
import MobileNavbar from "../components/FloatingNavbar";

const JobRecommendations = () => {
  const [user, setUser] = useState(null);
  const [jobs, setJobs] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");

  // Fetch user + recommendations
  useEffect(() => {
	const fetchRecommendations = async () => {
		try {
		const response = await axios.get("http://127.0.0.1:5000/api/jobs/recommended");
		setJobs(response.data.recommendations || []); // ✅ store job data
		setLoading(false); // ✅ stop loading spinner
		} catch (error) {
		console.error("Error fetching job recommendations:", error);
		setError("Failed to load job recommendations.");
		setLoading(false); // ✅ stop loading even on error
		}
	};

	fetchRecommendations();
	}, []);


  if (loading)
    return (
      <div className="d-flex justify-content-center align-items-center vh-100">
        <Loader2 className="spin" size={28} color="#6040AB" />
        <span className="ms-2 fw-semibold text-muted">Loading recommendations...</span>
      </div>
    );

  if (error)
    return (
      <div className="d-flex justify-content-center align-items-center vh-100 text-danger fw-semibold">
        {error}
      </div>
    );

  return (
    <main
      className="container-fluid p-0"
      style={{
        backgroundColor: "#F7F6FB",
        minHeight: "100vh",
        display: "flex",
        flexDirection: "column",
      }}
    >
      <div className="row g-0 flex-grow-1">
        {/* ===== Left Sidebar ===== */}
        <div className="col-12 col-md-3 p-0">
          <AppSidebar user={user} />
        </div>

        {/* ===== Right Panel ===== */}
        <div className="col-12 col-md-9 p-4 bg-light position-relative pt-5 pt-md-0">
          <h2 className="fw-bold mb-4" style={{ color: "#6040AB" }}>
            <Briefcase size={26} className="me-2" />
            Job Recommendations
          </h2>

          {jobs.length === 0 ? (
            <p className="text-muted text-center">No recommendations available yet.</p>
          ) : (
            <div className="row g-4">
              {jobs.map((job, index) => (
                <div key={index} className="col-12 col-md-6">
                  <div
                    className="card shadow-sm border-0 h-100 hover-zoom"
                    style={{
                      borderRadius: "14px",
                      transition: "transform 0.2s ease, box-shadow 0.2s ease",
                    }}
                    onMouseEnter={(e) => {
                      e.currentTarget.style.transform = "translateY(-5px)";
                      e.currentTarget.style.boxShadow =
                        "0 8px 18px rgba(0,0,0,0.1)";
                    }}
                    onMouseLeave={(e) => {
                      e.currentTarget.style.transform = "translateY(0)";
                      e.currentTarget.style.boxShadow =
                        "0 4px 10px rgba(0,0,0,0.05)";
                    }}
                  >
                    <div className="card-body">
                      <h5
                        className="fw-bold mb-1"
                        style={{ color: "#6040AB" }}
                      >
                        {job.title}
                      </h5>
                      <p className="text-muted mb-2">{job.company}</p>
                      <p className="small">{job.description}</p>

                      <div className="mt-3">
                        <strong>Required Skills:</strong>
                        <div className="mt-1">
                          {(job.required_skills || []).map((skill, idx) => (
                            <span
                              key={idx}
                              className="badge bg-secondary me-1"
                              style={{
                                backgroundColor: "#EAE6F8",
                                color: "#6040AB",
                              }}
                            >
                              {skill}
                            </span>
                          ))}
                        </div>
                      </div>

                      <div className="mt-3 small text-muted">
                        Experience Level:{" "}
                        <span className="fw-semibold">
                          {job.experience_level || "N/A"}
                        </span>
                      </div>

                      {job.link && (
                        <div className="mt-3">
                          <a
                            href={job.link}
                            target="_blank"
                            rel="noreferrer"
                            className="btn btn-sm text-white fw-semibold"
                            style={{
                              backgroundColor: "#6040AB",
                              borderRadius: "10px",
                            }}
                          >
                            Apply Now
                          </a>
                        </div>
                      )}
                    </div>
                  </div>
                </div>
              ))}
            </div>
          )}

          {/* Spacer for mobile navbar */}
          <div className="mb-5 d-md-none"></div>
        </div>
      </div>

      {/* ===== Floating Navbar for Mobile ===== */}
      <MobileNavbar />
    </main>
  );
};

export default JobRecommendations;
