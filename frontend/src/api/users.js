//  src/api/users.js
import { api } from './index';

export const getUsers = () => api.get('/users');
export const createUser = (data) => api.post('/users', data);
export const updateUser = (userId, data) => api.put(`/users/${userId}`, data);
export const deleteUser = (userId) => api.delete(`/users/${userId}`);
