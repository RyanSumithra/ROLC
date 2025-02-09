import React, { useState, useEffect } from "react";
import axios from "axios";

const VehicleList = () => {
  const [vehicles, setVehicles] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    // Fetch vehicles from API
    axios
      .get("/api/vehicles")
      .then((response) => {
        setVehicles(response.data);
        setLoading(false);
      })
      .catch((error) => {
        console.error("There was an error fetching vehicles:", error);
        setLoading(false);
      });
  }, []);

  if (loading) {
    return <p>Loading vehicles...</p>;
  }

  return (
    <div>
      <h2>Vehicle List</h2>
      <table>
        <thead>
          <tr>
            <th>Vehicle ID</th>
            <th>Capacity</th>
            <th>Speed</th>
            <th>Current Location</th>
          </tr>
        </thead>
        <tbody>
          {vehicles.map((vehicle, index) => (
            <tr key={index}>
              <td>{vehicle.vehicle_id}</td>
              <td>{vehicle.capacity}</td>
              <td>{vehicle.speed}</td>
              <td>Lat: {vehicle.current_location.lat}, Lon: {vehicle.current_location.lon}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default VehicleList;
