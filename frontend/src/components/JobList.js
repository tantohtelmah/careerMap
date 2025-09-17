import React, { useEffect, useState } from "react";
import { getJobs } from "../api";

const JobList = ({ userId }) => {
  const [jobs, setJobs] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchJobs = async () => {
      try {
        const data = await getJobs(userId);
        setJobs(data);
      } catch (error) {
        console.error("Error fetching jobs:", error);
      } finally {
        setLoading(false);
      }
    };

    fetchJobs();
  }, [userId]);

  if (loading) return <p>Loading jobs...</p>;
  if (jobs.length === 0) return <p>No jobs found.</p>;

  return (
    <ul>
      {jobs.map((job) => (
        <li key={job.job_id}>
          <strong>{job.title}</strong> at {job.company} - {job.status}
        </li>
      ))}
    </ul>
  );
};

export default JobList;
