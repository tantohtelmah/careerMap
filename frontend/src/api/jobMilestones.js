import { api } from './index';

export const linkJobMilestone = (data) => api.post('/job_milestones/link', data);
export const unlinkJobMilestone = (data) => api.post('/job_milestones/unlink', data);
