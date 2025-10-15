import axios from "axios";

export const api = axios.create({
  baseURL: "http://127.0.0.1:5000/api/auth", // your Flask backend
  headers: { "Content-Type": "application/json" },
});

// Register user
export const signup= (data) => api.post("/signup", data);

// Login user
export const loginUser = (data) => api.post("/login", data);
