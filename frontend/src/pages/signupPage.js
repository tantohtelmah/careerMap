import React, { useState } from "react";
import { Link } from "react-router-dom";
import axios from "axios";

const SignupPage = () => {
  const [username, setUsername] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");
  const [success, setSuccess] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError("");
    setSuccess("");

    try {
      const { data } = await axios.post("http://127.0.0.1:5000/api/auth/signup", {
        username,
        email,
        password,
      });

      setSuccess(data.message || "Signup successful! You can now login.");
      setUsername("");
      setEmail("");
      setPassword("");
    } catch (err) {
      console.error(err);
      setError(err.response?.data?.error || "Signup failed");
    }
  };

  return (
    <main
      style={{
        position: "relative",
        height: "100vh",
        overflow: "hidden",
      }}
    >
      {/* Background image with blur */}
      <div
        style={{
          position: "absolute",
          inset: 0,
          backgroundImage: "url('bgImg.png')", // replace with your image
          backgroundSize: "cover",
          backgroundPosition: "center",
          filter: "blur(8px)",
          zIndex: 1,
        }}
      ></div>

      {/* Dark overlay */}
      <div
        style={{
          position: "absolute",
          inset: 0,
          backgroundColor: "rgba(0,0,0,0.4)",
          zIndex: 2,
        }}
      ></div>

      {/* Form card */}
      <div
        className="d-flex justify-content-center align-items-center vh-100"
        style={{ position: "relative", zIndex: 3 }}
      >
        <div className="col-11 col-sm-8 col-md-6 col-lg-4 p-4 shadow bg-white rounded text-center">
          {/* Logo */}
          <img
            src="logo.png"
            alt="Logo"
            style={{ width: "100px", marginBottom: "20px" }}
          />

          <h4 className="mb-4">Create Account</h4>

          {error && <p className="text-danger">{error}</p>}
          {success && <p className="text-success">{success}</p>}

          <form style={{ fontSize: "14px" }} onSubmit={handleSubmit}>
            <div className="mb-3 text-start">
              <label htmlFor="username" className="form-label">
                Username
              </label>
              <input
                id="username"
                type="text"
                className="form-control"
                value={username}
                onChange={(e) => setUsername(e.target.value)}
                required
              />
            </div>

            <div className="mb-3 text-start">
              <label htmlFor="email" className="form-label">
                Email
              </label>
              <input
                id="email"
                type="email"
                className="form-control"
                value={email}
                onChange={(e) => setEmail(e.target.value)}
                required
              />
            </div>

            <div className="mb-3 text-start">
              <label htmlFor="password" className="form-label">
                Password
              </label>
              <input
                id="password"
                type="password"
                className="form-control"
                value={password}
                onChange={(e) => setPassword(e.target.value)}
                required
              />
            </div>

            <div
              className="mb-3 d-flex justify-content-between"
              style={{ fontSize: "14px" }}
            >
              <Link
                to="/"
                style={{
                  color: "#0d6efd",
                  textDecoration: "none",
                  fontWeight: 500,
                }}
              >
                Back to Login
              </Link>
            </div>

            <button
              type="submit"
              className="btn w-100 mb-3 rounded"
              style={{
                backgroundColor: "#6040AB",
                borderColor: "#6040AB",
                color: "#fff",
                fontWeight: 500,
              }}
            >
              Sign Up
            </button>
          </form>
        </div>
      </div>
    </main>
  );
};

export default SignupPage;
