import { useEffect, useState } from "react";
import API from "../api";
import Layout from "../components/Layout";
import { Link } from "react-router-dom";

function Jobs() {
  const [jobs, setJobs] = useState([]);

  useEffect(() => {
    fetchJobs();
  }, []);

  const fetchJobs = async () => {
    try {
      const response = await API.get("/jobs/");
      setJobs(response.data);
    } catch (error) {
      console.error("Error fetching jobs:", error);
          if (error.response?.status === 401) {
      localStorage.removeItem("token");
      window.location.href = "/";
    }

    }
  };

  const handleDelete = async (id) => {
    try {
      await API.delete(`/jobs/${id}`);
      fetchJobs(); // refresh list
    } catch (error) {
      console.error("Delete error:", error);
      alert("Failed to delete job");
    }
  };

  return (
    <Layout>
  
        <h2>All Jobs</h2>

        <br />

        <Link to="/add-job">
          <button>Add New Job</button>
        </Link>

        <br /><br />

        {jobs.length === 0 ? (
          <p>No jobs found</p>
        ) : (
          jobs.map((job) => (
            <div className="job-card" key={job.id}>
              <h4>{job.position}</h4>
              <p><strong>Company:</strong> {job.company_name}</p>
              <p><strong>Location:</strong> {job.location}</p>
              <p><strong>Status:</strong> {job.status}</p>
              <p><strong>Salary:</strong> {job.salary}</p>
              <p><strong>Applied:</strong> {job.applied_date}</p>
              {job.notes && (
                <p><strong>Notes:</strong> {job.notes}</p>
              )}

              <br />

              <button onClick={() => handleDelete(job.id)}>
                Delete
              </button>
            </div>
          ))
        )}
     
    </Layout>
  );
}

export default Jobs;