import React, { useEffect, useState } from "react";
import axios from "axios";
import MobileNavbar from "../components/FloatingNavbar";
import AppSidebar from "../components/AppSidebar";
import { UserCircle } from "lucide-react";


const ProfilePage = () => {
  const [user, setUser] = useState(null);
  const [error, setError] = useState("");
  const [loading, setLoading] = useState(true);
  const [formData, setFormData] = useState({
    username: "",
    email: "",
    skills: "",
    education: "",
    experience: "",
    preferences: "",
  });

  useEffect(() => {
    const fetchProfile = async () => {
      try {
        const token = localStorage.getItem("token");
        if (!token) {
          setError("No token found. Please login.");
          setLoading(false);
          return;
        }
        const response = await axios.get("http://127.0.0.1:5000/api/auth/profile", {
          headers: { Authorization: `Bearer ${token}` },
        });
        const data = response.data;
        setUser(data);
        setFormData({
          username: data.username || data.name || "",
          email: data.email || "",
          skills: Array.isArray(data.skills || data.skillset)
            ? (data.skills || data.skillset).join(", ")
            : data.skills || data.skillset || "",
          education: Array.isArray(data.education)
            ? data.education.join(", ")
            : data.education || "",
          experience: Array.isArray(data.experience)
            ? data.experience.join(", ")
            : data.experience || "",
          preferences: JSON.stringify(data.preferences || {}, null, 2),
        });
      } catch (err) {
        console.error(err);
        setError(err.response?.data?.error || "Failed to load profile");
      } finally {
        setLoading(false);
      }
    };
    fetchProfile();
  }, []);

  const handleChange = (e) => setFormData({ ...formData, [e.target.name]: e.target.value });

  const handleUpdate = async () => {
    try {
      const token = localStorage.getItem("token");
      const payload = {
        username: formData.username,
        email: formData.email,
        skills: formData.skills.split(",").map((s) => s.trim()).filter(Boolean),
        education: formData.education.split(",").map((e) => e.trim()).filter(Boolean),
        experience: formData.experience.split(",").map((ex) => ex.trim()).filter(Boolean),
        preferences: JSON.parse(formData.preferences || "{}"),
      };
      const response = await axios.put("http://127.0.0.1:5000/api/auth/update-profile", payload, {
        headers: { Authorization: `Bearer ${token}` },
      });

      setUser(response.data.user);
      alert("Profile updated successfully!");
    } catch (err) {
      console.error(err);
      alert(err.response?.data?.error || "Update failed");
    }
  };

  if (loading) return <p className="text-center mt-5">Loading...</p>;
  if (error) return <p className="text-danger text-center mt-5">{error}</p>;

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
        {/* LEFT PANEL */}
        <div className="col-12 col-md-3 p-0">
          <AppSidebar user={user} />
        </div>
        {/* RIGHT PANEL */}
        <div className="col-12 col-md-9 p-4 bg-light position-relative pt-5 pt-md-0">
          <h2 className="fw-bold mb-4" style={{ color: "#6040AB" }}>
            User Profile
          </h2>

          <div
            className="card shadow-sm border-0 p-4 mb-5"
            style={{ borderRadius: "16px" }}
          >
            {[
              { label: "Username", name: "username", type: "text" },
              { label: "Email", name: "email", type: "email" },
            ].map((field, idx) => (
              <div className="mb-3" key={idx}>
                <label className="form-label fw-semibold">{field.label}</label>
                <input
                  type={field.type}
                  name={field.name}
                  className="form-control"
                  value={formData[field.name]}
                  onChange={handleChange}
                />
              </div>
            ))}

            {[
              { label: "Skills (comma separated)", name: "skills", rows: 2 },
              { label: "Education (comma separated)", name: "education", rows: 2 },
              { label: "Experience (comma separated)", name: "experience", rows: 2 },
              { label: "Preferences (JSON)", name: "preferences", rows: 4 },
            ].map((field, idx) => (
              <div className="mb-3" key={idx}>
                <label className="form-label fw-semibold">{field.label}</label>
                <textarea
                  name={field.name}
                  className="form-control"
                  rows={field.rows}
                  value={formData[field.name]}
                  onChange={handleChange}
                />
              </div>
            ))}

            <div className="d-flex justify-content-between align-items-center">
              <button
                onClick={handleUpdate}
                className="btn text-white fw-semibold"
                style={{
                  backgroundColor: "#6040AB",
                  borderRadius: "10px",
                  letterSpacing: "0.5px",
                }}
              >
                💾 Save Changes
              </button>
            </div>
          </div>

          {/* Spacer for mobile navbar */}
          <div className="mb-5 d-md-none"></div>
        </div>
      </div>
      {/* Floating Mobile Bottom Navbar */}
      <MobileNavbar />
    </main>
  );
};

export default ProfilePage;
