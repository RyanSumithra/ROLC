import React, { useState, useEffect } from "react";
import axios from "axios";
import { useParams } from "react-router-dom";

const Tracking = () => {
  const { vehicleId } = useParams(); // Get vehicleId from the URL params
  const [vehicle, setVehicle] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    // Fetch vehicle tracking data from API
    axios
      .get(`/api/vehicle/${vehicleId}`)
      .then((response) => {
        setVehicle(response.data);
        setLoading(false);
      })
      .catch((error) => {
        console.error("There was an error fetching the vehicle:", error);
        setLoading(false);
      });
  }, [vehicleId]);

  if (loading) {
    return <p>Loading tracking information...</p>;
  }

  if (!vehicle) {
    return <p>Vehicle not found.</p>;
  }

  return (
    <div>
      <h2>Tracking Information for Vehicle {vehicle.vehicle_id}</h2>
      <p>
        <strong>Capacity:</strong> {vehicle.capacity}
      </p>
      <p>
        <strong>Speed:</strong> {vehicle.speed}
      </p>
      <p>
        <strong>Current Location:</strong> Lat: {vehicle.current_location.lat}, Lon: {vehicle.current_location.lon}
      </p>
    </div>
  );
};

export default Tracking;
