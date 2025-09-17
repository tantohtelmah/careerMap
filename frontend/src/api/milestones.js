import { api } from './index';

export const getMilestones = (userId) => api.get(`/milestones/${userId}`);
export const createMilestone = (data) => api.post('/milestones', data);
export const updateMilestone = (id, data) => api.put(`/milestones/${id}`, data);
export const deleteMilestone = (id) => api.delete(`/milestones/${id}`);
