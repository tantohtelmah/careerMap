import axios from "axios";

const API_URL = "http://127.0.0.1:5000/api";

export const api = axios.create({
  baseURL: API_URL,
  headers: {
    "Content-Type": "application/json",
  },
});

// Add getJobs function
export const getJobs = async (userId) => {
  const response = await api.get(`/jobs/${userId}`);
  return response.data;
};