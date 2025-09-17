import { api } from './index';

export const getCareerGoals = (userId) => api.get(`/career_goals/${userId}`);
export const createCareerGoal = (data) => api.post('/career_goals', data);
export const updateCareerGoal = (id, data) => api.put(`/career_goals/${id}`, data);
export const deleteCareerGoal = (id) => api.delete(`/career_goals/${id}`);
