import { api } from './index';

export const getMilestoneProgress = (userId) => api.get(`/milestone_progress/${userId}`);
export const createProgress = (data) => api.post('/milestone_progress', data);
export const updateProgress = (id, data) => api.put(`/milestone_progress/${id}`, data);
export const deleteProgress = (id) => api.delete(`/milestone_progress/${id}`);
