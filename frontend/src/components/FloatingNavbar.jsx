import React from "react";
import { Home, UserCircle, Settings } from "lucide-react";
import { useLocation } from "react-router-dom";

const FloatingNavbar = () => {
  const location = useLocation();

  const navItems = [
    { label: "Home", link: "/dashboard", icon: <Home size={22} /> },
    { label: "Profile", link: "/profile", icon: <UserCircle size={22} /> },
    { label: "Settings", link: "/settings", icon: <Settings size={22} /> },
  ];

  return (
    <>
      {/* 🌐 Desktop Floating Navbar (right-center) */}
      <div
        className="d-none d-md-flex flex-column align-items-center justify-content-around position-fixed shadow-lg"
        style={{
          top: "50%",
          right: "25px",
          transform: "translateY(-50%)",
          background: "rgba(255, 255, 255, 0.85)",
          backdropFilter: "blur(12px)",
          borderRadius: "30px",
          padding: "15px 10px",
          width: "65px",
          zIndex: 1000,
          boxShadow: "0 4px 20px rgba(0,0,0,0.25)",
          border: "1px solid rgba(255,255,255,0.6)",
        }}
      >
        {navItems.map((item, index) => {
          const isActive = location.pathname === item.link;
          return (
            <a
              key={index}
              href={item.link}
              className="d-flex flex-column align-items-center text-decoration-none fw-semibold mb-3"
              style={{
                color: isActive ? "#6040AB" : "#333",
                transition: "all 0.25s ease",
              }}
              onMouseOver={(e) => {
                e.currentTarget.style.transform = "scale(1.1)";
                e.currentTarget.style.color = "#6040AB";
              }}
              onMouseOut={(e) => {
                e.currentTarget.style.transform = "scale(1)";
                e.currentTarget.style.color = isActive ? "#6040AB" : "#333";
              }}
            >
              <div
                style={{
                  fontSize: "1.4rem",
                  marginBottom: "2px",
                }}
              >
                {item.icon}
              </div>
              <small style={{ fontSize: "0.7rem" }}>{item.label}</small>
            </a>
          );
        })}
      </div>

      {/* 📱 Mobile Floating Navbar (bottom-center) */}
      <footer
        className="d-md-none position-fixed bottom-0 start-50 translate-middle-x px-4 py-2 shadow-lg"
        style={{
          background: "rgba(255,255,255,0.85)",
          backdropFilter: "blur(15px)",
          borderRadius: "25px",
          width: "90%",
          maxWidth: "420px",
          zIndex: 9999,
          boxShadow: "0 4px 20px rgba(0,0,0,0.25)",
          border: "1px solid rgba(255,255,255,0.6)",
          transform: "translateX(-50%)",
          bottom: "20px",
        }}
      >
        <nav className="d-flex justify-content-around align-items-center py-1">
          {navItems.map((item, index) => {
            const isActive = location.pathname === item.link;
            return (
              <a
                key={index}
                href={item.link}
                className="d-flex flex-column align-items-center text-decoration-none fw-semibold"
                style={{
                  fontSize: "0.75rem",
                  color: isActive ? "#6040AB" : "#333",
                  transition: "all 0.25s ease",
                  transform: isActive ? "translateY(-2px)" : "none",
                }}
                onMouseOver={(e) => {
                  e.currentTarget.style.transform = "translateY(-4px)";
                  e.currentTarget.style.color = "#6040AB";
                }}
                onMouseOut={(e) => {
                  e.currentTarget.style.transform = isActive
                    ? "translateY(-2px)"
                    : "translateY(0)";
                  e.currentTarget.style.color = isActive ? "#6040AB" : "#333";
                }}
              >
                <div
                  style={{
                    fontSize: "1.5rem",
                    marginBottom: "3px",
                    transition: "color 0.3s ease",
                  }}
                >
                  {item.icon}
                </div>
                <small>{item.label}</small>
              </a>
            );
          })}
        </nav>
      </footer>
    </>
  );
};

export default FloatingNavbar;
