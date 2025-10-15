import React, { useState } from "react";
import { Menu, X, LogOut } from "lucide-react";
import { motion, AnimatePresence } from "framer-motion";
import { useNavigate } from "react-router-dom";

const AppSidebar = ({ user }) => {
  const [menuOpen, setMenuOpen] = useState(false);
  const navigate = useNavigate();

  const handleLogout = () => {
    localStorage.removeItem("token");
    navigate("/"); // redirect to login page
  };

  return (
    <>
      {/* ======= Desktop View ======= */}
      <aside
        className="d-none d-md-flex text-white flex-column justify-content-between p-3"
        style={{
          background: "linear-gradient(135deg, #6040AB, #7A5EEA)",
          height: "100vh",
          width: "260px",
          position: "fixed", // ✅ keeps it stuck in place
          top: 0,
          left: 0,
          zIndex: 1000,
          boxShadow: "2px 0 8px rgba(0,0,0,0.1)",
        }}
      >
        {/* Top Logo */}
        <div className="w-100 text-start mb-3">
          <h4 className="fw-bold mb-0">CareerMap</h4>
        </div>

        {/* Center Profile */}
        <div className="d-flex flex-column align-items-center">
          <img
            src={
              user?.profile_image
                ? `http://127.0.0.1:5000${user.profile_image}`
                : "default-avatar.png"
            }
            alt="User Avatar"
            style={{
              width: "110px",
              height: "110px",
              borderRadius: "50%",
              border: "3px solid #fff",
              objectFit: "cover",
              marginBottom: "10px",
            }}
          />
          <div className="text-center small">
            <h6 className="fw-semibold mb-1">{user?.username || "User"}</h6>
            <p className="mb-1">{user?.email || "email@example.com"}</p>
            <p className="mb-1">{user?.phone || "No phone"}</p>
            <p className="mb-2">{user?.address || "No address"}</p>
          </div>
        </div>

        {/* Bottom Menu */}
        <div
          className="w-100 d-flex justify-content-center align-items-center gap-4 pb-3 mt-auto"
          style={{ fontSize: "0.9rem" }}
        >
          {["Help", "Options"].map((item, idx) => (
            <button
              key={idx}
              className="btn btn-link text-white p-0 text-decoration-none fw-semibold"
              style={{
                cursor: "pointer",
                fontSize: "0.9rem",
                transition: "opacity 0.2s ease-in-out",
              }}
              onMouseEnter={(e) => (e.target.style.opacity = "0.8")}
              onMouseLeave={(e) => (e.target.style.opacity = "1")}
            >
              {item}
            </button>
          ))}

          <button
            onClick={handleLogout}
            className="btn btn-link text-white p-0 text-decoration-none fw-semibold d-flex align-items-center gap-1"
            style={{
              cursor: "pointer",
              fontSize: "0.9rem",
              transition: "opacity 0.2s ease-in-out",
            }}
            onMouseEnter={(e) => (e.target.style.opacity = "0.8")}
            onMouseLeave={(e) => (e.target.style.opacity = "1")}
          >
            <LogOut size={16} /> Logout
          </button>
        </div>
      </aside>

      {/* ======= Mobile View ======= */}
      <nav
        className="d-md-none text-white px-3 py-2"
        style={{
          backgroundColor: "#6040AB",
          position: "fixed",
          top: 0,
          left: 0,
          right: 0,
          width: "100%",
          zIndex: 1050,
          boxShadow: "0 2px 6px rgba(0,0,0,0.15)",
        }}
      >
        <div className="d-flex justify-content-between align-items-center">
          <h5 className="fw-bold mb-0">CareerMap</h5>
          <button
            className="btn text-white p-0"
            onClick={() => setMenuOpen(!menuOpen)}
          >
            {menuOpen ? <X size={28} /> : <Menu size={28} />}
          </button>
        </div>

        {/* Animated dropdown */}
        <AnimatePresence>
          {menuOpen && (
            <motion.div
              initial={{ opacity: 0, y: -10 }}
              animate={{ opacity: 1, y: 0 }}
              exit={{ opacity: 0, y: -10 }}
              transition={{ duration: 0.3, ease: "easeInOut" }}
              className="bg-white text-dark rounded shadow p-3 mt-2"
              style={{
                zIndex: 1100,
                position: "absolute",
                top: "58px",
                left: 0,
                right: 0,
                margin: "0 10px",
                maxHeight: "80vh",
                overflowY: "auto",
              }}
            >
              <div className="text-center mb-3">
                <img
                  src={
                    user?.profile_image
                      ? `http://127.0.0.1:5000${user.profile_image}`
                      : "default-avatar.png"
                  }
                  alt="User Avatar"
                  style={{
                    width: "80px",
                    height: "80px",
                    borderRadius: "50%",
                    objectFit: "cover",
                    border: "2px solid #6040AB",
                  }}
                />
              </div>

              <div className="text-center mb-3">
                <h6 className="fw-semibold mb-1">{user?.username}</h6>
                <p className="small mb-1">{user?.email}</p>
                <p className="small mb-1">{user?.phone}</p>
                <p className="small mb-2">{user?.address}</p>
              </div>

              <div className="w-100 d-flex justify-content-center gap-3 pb-2">
                <button className="btn btn-link text-dark p-0 small text-decoration-none">
                  Help
                </button>
                <button className="btn btn-link text-dark p-0 small text-decoration-none">
                  Options
                </button>
                <button
                  onClick={handleLogout}
                  className="btn btn-link text-danger p-0 small text-decoration-none d-flex align-items-center gap-1"
                >
                  <LogOut size={14} /> Logout
                </button>
              </div>
            </motion.div>
          )}
        </AnimatePresence>
      </nav>
    </>
  );
};

export default AppSidebar;
