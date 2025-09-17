import { api } from './index';

export const getNotifications = (userId) => api.get(`/notifications/${userId}`);
export const createNotification = (data) => api.post('/notifications', data);
export const deleteNotification = (id) => api.delete(`/notifications/${id}`);
