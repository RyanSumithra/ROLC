import React, { useState, useEffect } from "react";
import axios from "axios";

const OrderList = () => {
  const [orders, setOrders] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    // Fetch orders from API
    axios
      .get("/api/orders")
      .then((response) => {
        setOrders(response.data);
        setLoading(false);
      })
      .catch((error) => {
        console.error("There was an error fetching orders:", error);
        setLoading(false);
      });
  }, []);

  if (loading) {
    return <p>Loading orders...</p>;
  }

  return (
    <div>
      <h2>Orders List</h2>
      <table>
        <thead>
          <tr>
            <th>Customer Name</th>
            <th>Item ID</th>
            <th>Quantity</th>
            <th>Delivery Location</th>
            <th>Order Timestamp</th>
          </tr>
        </thead>
        <tbody>
          {orders.map((order, index) => (
            <tr key={index}>
              <td>{order.customer_name}</td>
              <td>{order.item_id}</td>
              <td>{order.quantity}</td>
              <td>Lat: {order.delivery_lat}, Lon: {order.delivery_lon}</td>
              <td>{new Date(order.order_timestamp).toLocaleString()}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default OrderList;
