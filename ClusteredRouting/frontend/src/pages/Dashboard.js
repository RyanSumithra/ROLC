import React, { useState, useEffect } from "react";
import axios from "axios";

function Dashboard() {
  const [orders, setOrders] = useState([]);
  const [vehicles, setVehicles] = useState([]);

  useEffect(() => {
    fetchOrders();
    fetchVehicles();
  }, []);

  const fetchOrders = async () => {
    try {
      const response = await axios.get("http://localhost:5000/orders");
      setOrders(response.data);
    } catch (error) {
      console.error("Error fetching orders:", error);
    }
  };

  const fetchVehicles = async () => {
    try {
      const response = await axios.get("http://localhost:5000/vehicles");
      setVehicles(response.data);
    } catch (error) {
      console.error("Error fetching vehicles:", error);
    }
  };

  return (
    <div className="p-4">
      <h2 className="text-xl font-bold mb-4">Dashboard</h2>
      <div className="grid grid-cols-2 gap-4">
        <div className="border p-4 rounded">
          <h3 className="font-bold">Pending Orders</h3>
          {orders.length > 0 ? (
            <ul>
              {orders.map((order) => (
                <li key={order._id}>{order.customer_name} - {order.status}</li>
              ))}
            </ul>
          ) : (
            <p>No pending orders</p>
          )}
        </div>
        <div className="border p-4 rounded">
          <h3 className="font-bold">Available Vehicles</h3>
          {vehicles.length > 0 ? (
            <ul>
              {vehicles.map((vehicle) => (
                <li key={vehicle._id}>{vehicle.type} - {vehicle.status}</li>
              ))}
            </ul>
          ) : (
            <p>No available vehicles</p>
          )}
        </div>
      </div>
    </div>
  );
}

export default Dashboard;
