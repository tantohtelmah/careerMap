import React, { useState } from "react";
import { loginUser } from "../api/auth";
import { useNavigate } from "react-router-dom";



const LoginPage = ({ onLogin }) => {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");
  const navigate = useNavigate();

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError("");

    try {
      const response = await loginUser({ email, password });
      const user = response.data.user;
      const token = response.data.token;

      // Store token
      localStorage.setItem("token", token);
      console.log(localStorage.getItem("token"));


      // Alert success
      // alert("Login successful!");

      // Navigate to profile page
      
      navigate("/profile");

      // Call parent callback
      onLogin && onLogin(user);
    } catch (err) {
      console.error(err);
      setError(err.response?.data?.error || "Login failed");
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
          backgroundImage: "url('bgImg.png')", // Replace with your image
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

          <h4 className="mb-4">Welcome Back</h4>

          <form style={{ fontSize: "14px" }} onSubmit={handleSubmit}>
            {error && <p className="text-danger">{error}</p>}

            {/* Email input */}
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

            {/* Password input */}
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

            {/* Forgot password / Sign Up links */}
            <div
              className="mb-3 d-flex justify-content-between"
              style={{ fontSize: "14px" }}
            >
              <a
                href="/forgot-password"
                style={{
                  color: "#0d6efd",
                  textDecoration: "none",
                  fontWeight: 500,
                }}
              >
                <u>Forgot password?</u>
              </a>
              <a
                href="/signup"
                style={{
                  color: "#0d6efd",
                  textDecoration: "none",
                  fontWeight: 500,
                }}
              >
                <u>Sign Up</u>
              </a>
            </div>

            {/* Login button */}
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
              Login
            </button>
          </form>
        </div>
      </div>
    </main>
  );
};

export default LoginPage;
