import React, { useEffect, useState } from "react";
import axios from "axios";
import { Search, Briefcase, Award } from "lucide-react";
import MobileNavbar from "../components/FloatingNavbar.jsx";
import ResumeUpload from "./ResumeUpload.jsx";
import CareerRoadmapPreview from "../components/CareerRoadmapPreview.jsx";
import AppSidebar from "../components/AppSidebar.jsx";

const Dashboard = () => {
  const [user, setUser] = useState(null);
  const [error, setError] = useState("");

  useEffect(() => {
    const fetchProfile = async () => {
      try {
        const token = localStorage.getItem("token");
        if (!token) {
          setError("No token found. Please login.");
          return;
        }

        const response = await axios.get("http://127.0.0.1:5000/api/auth/profile", {
          headers: { Authorization: `Bearer ${token}` },
        });
        setUser(response.data);
      } catch (err) {
        console.error(err);
        setError(err.response?.data?.error || "Failed to load profile");
      }
    };

    fetchProfile();
  }, []);

  if (error)
    return <p className="text-danger text-center mt-5 fw-semibold">{error}</p>;
  if (!user) return <p className="text-center mt-5">Loading...</p>;

  return (
    <main
      className="container-fluid p-0"
      style={{
        backgroundColor: "#F7F6FB",
        minHeight: "100vh",
        display: "flex",
        flexDirection: "column",
        paddingTop: "80px",
      }}
    >
      <div className="row g-0 flex-grow-1">
        {/* ===== LEFT SIDEBAR ===== */}
        <div className="col-12 col-md-3 p-0">
          <AppSidebar user={user} />
        </div>

        {/* ===== RIGHT PANEL ===== */}
        <div className="col-12 col-md-9 p-4 bg-light position-relative pt-5 pt-md-0">
          {/* Search bar */}
          <div
            className="d-flex align-items-center justify-content-center py-3 sticky-top"
            style={{
              background: "transparent",
              zIndex: 10,
            }}
          >
            <div
              className="d-flex align-items-center rounded-pill px-3 py-2 shadow-sm"
              style={{
                width: "90%",
                maxWidth: "600px",
                backgroundColor: "rgba(96, 64, 171, 0.9)",
                backdropFilter: "blur(8px)",
              }}
            >
              <Search size={18} color="white" className="me-2" />
              <input
                type="text"
                placeholder="Search..."
                className="form-control border-0 bg-transparent text-white"
                style={{
                  outline: "none",
                  boxShadow: "none",
                  fontSize: "0.9rem",
                }}
              />
            </div>
          </div>

          {/* ===== MAIN CONTENT ===== */}
          <div className="px-4 py-4 flex-grow-1 mb-5">
            <h2 className="fw-bold mb-3" style={{ color: "#6040AB" }}>
              Welcome back, {user.username} 👋
            </h2>

            <div className="row g-4">
              {/* Career Roadmap */}
              <div className="col-12 col-md-6 col-lg-6">
                <div className="card shadow-sm border-0 h-100">
                  <div className="card-body">
                    <h5 className="fw-bold mb-3" style={{ color: "#6040AB" }}>
                      🎯 Career Roadmap
                    </h5>
                    <CareerRoadmapPreview />
                    <div className="text-center mt-3">
                      <a
                        href="/careerRoadmap"
                        className="btn text-white fw-semibold px-4 py-2 shadow-sm"
                        style={{
                          backgroundColor: "#6040AB",
                          borderRadius: "10px",
                        }}
                      >
                        View Full Roadmap
                      </a>
                    </div>
                  </div>
                </div>
              </div>

              {/* Resume Upload */}
              <div className="col-12 col-md-6 col-lg-6">
                <div className="card shadow-sm border-0 h-100">
                  <div className="card-body">
                    <h5 className="fw-bold mb-3" style={{ color: "#6040AB" }}>
                      📄 Resume Upload
                    </h5>
                    <ResumeUpload existingResume={user?.resume_url} />
                  </div>
                </div>
              </div>

              {/* Job Recommendations */}
              <div className="col-12 col-md-6 col-lg-6">
                <div className="card shadow-sm border-0 h-100">
                  <div className="card-body">
                    <h5 className="fw-bold mb-3" style={{ color: "#6040AB" }}>
                      <Briefcase size={20} className="me-2" />
                      Job Recommendations
                    </h5>
                    <p className="text-muted">
                      Discover AI-curated jobs that match your skills, education, and career goals.
                    </p>
                    <div className="text-center mt-3">
                      <a
                        href="/JobRecommendations"
                        className="btn text-white fw-semibold px-4 py-2 shadow-sm"
                        style={{
                          backgroundColor: "#6040AB",
                          borderRadius: "10px",
                        }}
                      >
                        Explore Jobs
                      </a>
                    </div>
                  </div>
                </div>
              </div>

              {/* Certifications */}
              <div className="col-12 col-md-6 col-lg-6">
                <div className="card shadow-sm border-0 h-100">
                  <div className="card-body">
                    <h5 className="fw-bold mb-3" style={{ color: "#6040AB" }}>
                      <Award size={20} className="me-2" />
                      Certifications
                    </h5>
                    <p className="text-muted">
                      Manage your certifications and get AI suggestions for new ones to enhance your resume.
                    </p>
                    <div className="text-center mt-3">
                      <a
                        href="/certifications"
                        className="btn text-white fw-semibold px-4 py-2 shadow-sm"
                        style={{
                          backgroundColor: "#6040AB",
                          borderRadius: "10px",
                        }}
                      >
                        Manage Certifications
                      </a>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>

          {/* Mobile Navbar */}
          <MobileNavbar />
        </div>
      </div>
    </main>
  );
};

export default Dashboard;
