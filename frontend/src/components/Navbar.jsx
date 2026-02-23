import { Link, useNavigate } from "react-router-dom";

function Navbar() {
  const navigate = useNavigate();
  const token = localStorage.getItem("token");

  const handleLogout = () => {
    localStorage.removeItem("token");
    navigate("/");
  };

 return (
  <nav className="navbar">
    <h3>JobTracker</h3>

    <div className="nav-links">
      {!token ? (
        <>
          <Link to="/">Login</Link>
          <Link to="/register">Register</Link>
        </>
      ) : (
        <>
          <Link to="/jobs">Jobs</Link>
          <Link to="/add-job">Add Job</Link>
          <button onClick={handleLogout} className="logout-btn">
            Logout
          </button>
        </>
      )}
    </div>
  </nav>
);
}

export default Navbar;