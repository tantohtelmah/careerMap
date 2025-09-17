import { api } from './index';

export const getJobHistory = (userId) => api.get(`/job_history/${userId}`);
export const createJobHistory = (data) => api.post('/job_history', data);
export const updateJobHistory = (id, data) => api.put(`/job_history/${id}`, data);
export const deleteJobHistory = (id) => api.delete(`/job_history/${id}`);
