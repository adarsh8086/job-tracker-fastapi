import { useState } from "react";
import API from "../api";
import Layout from "../components/Layout";
import { useNavigate } from "react-router-dom";

function AddJob() {
  const [companyName, setCompanyName] = useState("");
  const [position, setPosition] = useState("");
  const [location, setLocation] = useState("");
  const [salary, setSalary] = useState("");
  const [status, setStatus] = useState("Applied");
  const [appliedDate, setAppliedDate] = useState("");
  const [notes, setNotes] = useState("");

  const navigate = useNavigate();

  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      await API.post("/jobs/", {
        company_name: companyName,
        position: position,
        location: location,
        salary: salary,
        status: status,
        applied_date: appliedDate,
        notes: notes
      });

      alert("Job Added Successfully ✅");
      navigate("/jobs");

    } catch (error) {
      console.error("Error adding job:", error.response?.data);
      alert("Failed to add job ❌");
    }
  };

  return (
    <Layout>
    
      <h2>Add Job</h2>

      <form onSubmit={handleSubmit}>

        <input
          type="text"
          placeholder="Company Name"
          value={companyName}
          onChange={(e) => setCompanyName(e.target.value)}
          required
        />
        <br /><br />

        <input
          type="text"
          placeholder="Position"
          value={position}
          onChange={(e) => setPosition(e.target.value)}
          required
        />
        <br /><br />

        <input
          type="text"
          placeholder="Location"
          value={location}
          onChange={(e) => setLocation(e.target.value)}
          required
        />
        <br /><br />

        <input
          type="text"
          placeholder="Salary"
          value={salary}
          onChange={(e) => setSalary(e.target.value)}
        />
        <br /><br />

        <input
          type="date"
          value={appliedDate}
          onChange={(e) => setAppliedDate(e.target.value)}
          required
        />
        <br /><br />

        <select value={status} onChange={(e) => setStatus(e.target.value)}>
          <option value="Applied">Applied</option>
          <option value="Interview">Interview</option>
          <option value="Offer">Offer</option>
          <option value="Rejected">Rejected</option>
        </select>
        <br /><br />

        <textarea
          placeholder="Notes"
          value={notes}
          onChange={(e) => setNotes(e.target.value)}
        />
        <br /><br />

        <button type="submit">Add Job</button>

      </form>
    </Layout>
  );
}

export default AddJob;