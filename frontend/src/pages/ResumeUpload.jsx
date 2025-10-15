import React, { useState } from "react";
import axios from "axios";

const ResumeUpload = ({ existingResume }) => {
  const [file, setFile] = useState(null);
  const [message, setMessage] = useState("");
  const [resumeUrl, setResumeUrl] = useState(existingResume || "");

  const handleUpload = async (e) => {
    e.preventDefault();
    if (!file) return setMessage("Please select a file");

    const token = localStorage.getItem("token");
    const formData = new FormData();
    formData.append("resume", file);

    try {
      const response = await axios.post("http://127.0.0.1:5000/api/profile/upload_resume", formData, {
        headers: {
          "Content-Type": "multipart/form-data",
          Authorization: `Bearer ${token}`,
        },
      });

      setResumeUrl(response.data.resume_url);
      setMessage("✅ Resume uploaded successfully!");
    } catch (err) {
      console.error(err);
      setMessage("❌ Upload failed");
    }
  };

  return (
    <div className="card p-4 shadow-sm border-0">
      <h5 className="fw-bold mb-3">Upload or Update Your Resume</h5>
      <form onSubmit={handleUpload}>
        <input
          type="file"
          accept=".pdf,.docx"
          className="form-control mb-3"
          onChange={(e) => setFile(e.target.files[0])}
        />
        <button className="btn btn-primary w-100" style={{ backgroundColor: "#6040AB" }}>
          Upload
        </button>
      </form>

      {message && <p className="text-center mt-3">{message}</p>}

      {resumeUrl && (
        <div className="text-center mt-3">
          <a href={resumeUrl} target="_blank" rel="noreferrer" className="btn btn-outline-secondary">
            📄 View Resume
          </a>
        </div>
      )}
    </div>
  );
};

export default ResumeUpload;
