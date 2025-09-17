import { api } from './index';

export const getJobs = (userId) => api.get(`/jobs/${userId}`);
export const createJob = (data) => api.post('/jobs', data);
export const updateJob = (jobId, data) => api.put(`/jobs/${jobId}`, data);
export const deleteJob = (jobId) => api.delete(`/jobs/${jobId}`);
