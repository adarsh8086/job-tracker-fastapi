import { BrowserRouter as Router, Routes, Route, Navigate } from "react-router-dom";
import { useEffect } from "react";
import API from "./api";
import Login from "./pages/Login"
import Register from "./pages/Register";
import Jobs from "./pages/Jobs";
import AddJob from "./pages/AddJob";
import ProtectedRoute from "./components/ProtectedRoute";
import Navbar from "./components/Navbar";

function App() {
    useEffect(() => {
    API.get("/docs")
      .then((res) => console.log("Connected to backend"))
      .catch((err) => console.error("Error:", err));
  }, []);

  return (
     <Router>
      <Navbar />
    <Routes>

      <Route
          path="/"
          element={
            localStorage.getItem("token")
            ? <Navigate to="/jobs" />
            : <Login />
           }
      />
      <Route path="/register" element={<Register />} />

      <Route
        path="/jobs"
        element={
          <ProtectedRoute>
            <Jobs />
          </ProtectedRoute>
        }
      />

      <Route
        path="/add-job"
        element={
          <ProtectedRoute>
            <AddJob />
          </ProtectedRoute>
        }
      />

    </Routes>
  </Router>
);
}

export default App
