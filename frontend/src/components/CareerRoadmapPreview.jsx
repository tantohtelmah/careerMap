// frontend/src/pages/CareerRoadmapPreview.jsx
import React from "react";

const CareerRoadmapPreview = ({ items = [] }) => {
  // simple fallback preview until you wire real data
  const sample = items.length
    ? items
    : [
        "✅ Complete final-year project",
        "💼 Apply for IT Support roles",
        "🧠 Learn AWS & DevOps fundamentals",
      ];

  return (
    <ul className="list-group small">
      {sample.map((text, idx) => (
        <li key={idx} className="list-group-item border-0 ps-0">
          {text}
        </li>
      ))}
    </ul>
  );
};

export default CareerRoadmapPreview;
