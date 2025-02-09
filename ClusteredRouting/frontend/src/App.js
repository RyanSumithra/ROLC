import React from "react";
import Dashboard from "./pages/Dashboard";
@import './styles/tailwind.css';


function App() {
  return (
    <div className="container mx-auto p-4">
      <h1 className="text-2xl font-bold text-center mb-4">Logistics Management System</h1>
      <Dashboard />
    </div>
  );
}

export default App;
