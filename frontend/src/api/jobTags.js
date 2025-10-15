import { api } from './index';

export const linkJobTag = (data) => api.post('/job_tags/link', data);
export const unlinkJobTag = (data) => api.post('/job_tags/unlink', data);
