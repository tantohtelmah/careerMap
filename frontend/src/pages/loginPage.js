import React, { useState } from "react";

const LoginPage = ({ onLogin }) => {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  const handleSubmit = (e) => {
    e.preventDefault();
    console.log("Logging in with", { email, password });
    onLogin && onLogin({ email });
  };

  return (
    <main
      style={{
        position: "relative",
        height: "100vh",
        overflow: "hidden",
      }}
    >
      {/* Background with blur */}
      <div
        style={{
          backgroundImage: "url('/bgImg.png')", 
          backgroundSize: "cover",
          backgroundPosition: "center",
          filter: "blur(6px)",
          position: "absolute",
          top: 0,
          left: 0,
          right: 0,
          bottom: 0,
          zIndex: 1,
        }}
      ></div>

      {/* Dark overlay */}
      <div
        style={{
          backgroundColor: "rgba(0,0,0,0.4)",
          position: "absolute",
          top: 0,
          left: 0,
          right: 0,
          bottom: 0,
          zIndex: 2,
        }}
      ></div>

      {/* Login Card */}
      <div
        className="d-flex justify-content-center align-items-center vh-100 "
        style={{ position: "relative", zIndex: 3 }}
      >
        <div className="col-11 col-sm-8 col-md-6 col-lg-4 p-4 shadow bg-white rounded">
          {/* Logo + Heading */}
          <header className="d-flex flex-column align-items-center mb-4">
            <div className="ratio ratio-1x1 mb-3" style={{ width: "80px" }}>
              <img
                src="/logo.png"
                alt="CareerMap Logo"
                className="img-fluid rounded"
              />
            </div>

            <h5 className="mb-1 text-center fw-bold">Welcome to CareerMap</h5>
            <p
              className="text-muted text-center mb-3"
              style={{ fontSize: "14px" }}
            >
              Your personal guide to your future
            </p>
            <h6 className="text-start w-100">Login</h6>
          </header>

          {/* Form */}
          <form style={{ fontSize: "14px" }} onSubmit={handleSubmit}>
            <div className="mb-3">
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

            <div className="mb-3">
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

            {/* Login button */}
            <button
              type="submit"
              className="btn w-100 mb-3 rounded"
              style={{
                backgroundColor: "#6040AB",
                borderColor: "#6040AB",
                color: "#fff",
              }}
            >
              Login
            </button>

            {/* Links */}
            <div
              className="d-flex justify-content-between"
              style={{ fontSize: "13px" }}
            >
              <a
                href="#"
                className="text-primary text-decoration-underline"
              >
                Forgot Password
              </a>
              <p className="mb-0">
                No Account?{" "}
                <a href="#" className="text-primary text-decoration-underline">
                  Sign up
                </a>
              </p>
            </div>
          </form>
        </div>
      </div>
    </main>
  );
};

export default LoginPage;
