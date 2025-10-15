import React, { useState, useEffect } from "react";
import axios from "axios";
import { Award } from "lucide-react";

const Certifications = () => {
  const [certs, setCerts] = useState([]);
  const [suggestions, setSuggestions] = useState([]);

  useEffect(() => {
    const fetchCerts = async () => {
    //   const token = localStorage.getItem("token");
      const res = await axios.get("http://127.0.0.1:5000/api/certifications/");
      setCerts(res.data.certs || []);
      setSuggestions(res.data.suggestions || []);
    };
    fetchCerts();
  }, []);

  return (
    <div className="container py-5">
      <h3 className="fw-bold mb-4" style={{ color: "#6040AB" }}>
        <Award className="me-2" /> Certifications
      </h3>

      <h5 className="fw-semibold">Your Certifications</h5>
      {certs.length ? (
        certs.map((c, i) => (
          <div key={i} className="card p-3 mb-3 shadow-sm">
            <h6>{c.name}</h6>
            <p className="small text-muted">Issued by {c.issuer}</p>
            <p className="small">
              <strong>Expires:</strong> {c.expiry || "No expiry"}
            </p>
          </div>
        ))
      ) : (
        <p className="text-muted">No certifications added yet.</p>
      )}

      <h5 className="fw-semibold mt-4">Recommended Certifications</h5>
      {suggestions.length ? (
        suggestions.map((s, i) => (
          <div key={i} className="border p-3 rounded mb-2 bg-light">
            <strong>{s.name}</strong> — {s.provider}
          </div>
        ))
      ) : (
        <p>No AI suggestions yet.</p>
      )}
    </div>
  );
};

export default Certifications;
