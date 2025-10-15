import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import LoginPage from "./pages/loginPage";
import SignupPage from "./pages/signupPage";
import ProfilePage from "./pages/profilePage";
import Dashboard from "./pages/dashboardPage";
import CareerRoadmap from "./pages/careerRoadmap"
import SettingsPage from "./pages/Settings";
import JobRecommendations from "./pages/JobRecommendations";
import Certifications from "./pages/Certification";

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<LoginPage />} />
        <Route path="/signup" element={<SignupPage />} /> 
        <Route path="/profile" element={<ProfilePage />} />
        <Route path="/dashboard" element={<Dashboard />} />
        <Route path="/careerRoadmap" element={<CareerRoadmap />} />
        <Route path="/settings" element={<SettingsPage />} />
        <Route path="/jobRecommendations" element={<JobRecommendations />} />
        <Route path="/certifications" element={<Certifications />} />
      </Routes>
    </Router>
  );
}

export default App;
