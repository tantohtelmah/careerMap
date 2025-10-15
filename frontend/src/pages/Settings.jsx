import React, { useEffect, useState } from "react";
import AppSidebar from "../components/AppSidebar";
import MobileNavbar from "../components/FloatingNavbar";
import { Sun, Moon, Bell, Shield, Monitor } from "lucide-react";
import axios from "axios";


const SettingsPage = () => {
  const [theme, setTheme] = useState("light");
  const [accentColor, setAccentColor] = useState("#6040AB");
  const [fontSize, setFontSize] = useState("medium");
  const [notifications, setNotifications] = useState(true);
  const [doNotDisturb, setDoNotDisturb] = useState(false);  

  // Load saved settings
  useEffect(() => {
    const savedTheme = localStorage.getItem("theme");
    const savedAccent = localStorage.getItem("accentColor");
    const savedFont = localStorage.getItem("fontSize");
    const savedNotif = localStorage.getItem("notifications");
    const savedDnd = localStorage.getItem("doNotDisturb");

    if (savedTheme) setTheme(savedTheme);
    if (savedAccent) setAccentColor(savedAccent);
    if (savedFont) setFontSize(savedFont);
    if (savedNotif) setNotifications(savedNotif === "true");
    if (savedDnd) setDoNotDisturb(savedDnd === "true");
  }, []);

  // Save settings to localStorage
  useEffect(() => {
    localStorage.setItem("theme", theme);
    localStorage.setItem("accentColor", accentColor);
    localStorage.setItem("fontSize", fontSize);
    localStorage.setItem("notifications", notifications);
    localStorage.setItem("doNotDisturb", doNotDisturb);
  }, [theme, accentColor, fontSize, notifications, doNotDisturb]);

  const [user, setUser] = useState(null);
  const [error, setError] = useState("");

  useEffect(() => {
    const fetchProfile = async () => {
      try {
        const token = localStorage.getItem("token");
        if (!token) return setError("No token found");

        const res = await axios.get("http://127.0.0.1:5000/api/auth/profile", {
          headers: { Authorization: `Bearer ${token}` },
        });
        setUser(res.data);
      } catch (err) {
        setError("Failed to load profile");
      }
    };

    fetchProfile();
  }, []);

  if (!user) return <p className="text-center mt-5">Loading...</p>;

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
        {/* LEFT SIDEBAR */}
        <div className="col-12 col-md-3">
          <AppSidebar user={user} />
        </div>

        {/* MAIN CONTENT */}
        <div
          className="col-12 col-md-9 p-4 bg-light position-relative pt-5 pt-md-4"
          style={{ overflowY: "auto", minHeight: "100vh" }}
        >
          <h2 className="fw-bold mb-4" style={{ color: "#6040AB" }}>
            ⚙️ Settings
          </h2>

          {/* THEME SETTINGS */}
          <section className="card border-0 shadow-sm p-4 mb-4">
            <h5 className="fw-semibold mb-3 d-flex align-items-center">
              <Sun className="me-2" size={18} /> Theme & Appearance
            </h5>
            <div className="d-flex flex-wrap gap-3">
              {/* Theme Toggle */}
              <div>
                <label className="fw-medium">Mode:</label>
                <select
                  className="form-select"
                  value={theme}
                  onChange={(e) => setTheme(e.target.value)}
                >
                  <option value="light">Light</option>
                  <option value="dark">Dark</option>
                  <option value="system">System Default</option>
                </select>
              </div>

              {/* Accent Color Picker */}
              <div>
                <label className="fw-medium">Accent Color:</label>
                <input
                  type="color"
                  value={accentColor}
                  onChange={(e) => setAccentColor(e.target.value)}
                  className="form-control form-control-color"
                />
              </div>

              {/* Font Size */}
              <div>
                <label className="fw-medium">Font Size:</label>
                <select
                  className="form-select"
                  value={fontSize}
                  onChange={(e) => setFontSize(e.target.value)}
                >
                  <option value="small">Small</option>
                  <option value="medium">Medium</option>
                  <option value="large">Large</option>
                </select>
              </div>
            </div>
          </section>

          {/* DASHBOARD PREFERENCES */}
          <section className="card border-0 shadow-sm p-4 mb-4">
            <h5 className="fw-semibold mb-3 d-flex align-items-center">
              <Monitor className="me-2" size={18} /> Dashboard Preferences
            </h5>
            <div className="form-check">
              <input className="form-check-input" type="checkbox" id="showCareerTips" />
              <label className="form-check-label" htmlFor="showCareerTips">
                Show Career Insights Widget
              </label>
            </div>
            <div className="form-check">
              <input className="form-check-input" type="checkbox" id="compactLayout" />
              <label className="form-check-label" htmlFor="compactLayout">
                Enable Compact Layout
              </label>
            </div>
          </section>

          {/* NOTIFICATION SETTINGS */}
          <section className="card border-0 shadow-sm p-4 mb-4">
            <h5 className="fw-semibold mb-3 d-flex align-items-center">
              <Bell className="me-2" size={18} /> Notifications
            </h5>
            <div className="form-check form-switch mb-2">
              <input
                className="form-check-input"
                type="checkbox"
                checked={notifications}
                onChange={(e) => setNotifications(e.target.checked)}
              />
              <label className="form-check-label">Enable Notifications</label>
            </div>
            <div className="form-check form-switch">
              <input
                className="form-check-input"
                type="checkbox"
                checked={doNotDisturb}
                onChange={(e) => setDoNotDisturb(e.target.checked)}
              />
              <label className="form-check-label">Do Not Disturb Mode</label>
            </div>
          </section>

          {/* PRIVACY SETTINGS */}
          <section className="card border-0 shadow-sm p-4 mb-5">
            <h5 className="fw-semibold mb-3 d-flex align-items-center">
              <Shield className="me-2" size={18} /> Privacy & Data
            </h5>
            <button className="btn btn-outline-primary mb-2 w-100">
              Download My Data (JSON)
            </button>
            <button className="btn btn-outline-danger w-100">
              Delete Account
            </button>
          </section>

          {/* Bottom Spacer for Mobile Navbar */}
          <div className="mb-5 d-md-none"></div>
        </div>
      </div>

      {/* MOBILE NAVBAR */}
      <MobileNavbar />
    </main>
  );
};

export default SettingsPage;
