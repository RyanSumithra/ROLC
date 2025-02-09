import axios from "axios";

const API_BASE_URL = "http://localhost:5000";

export const fetchOrders = async () => {
  try {
    const response = await axios.get(`${API_BASE_URL}/orders`);
    return response.data;
  } catch (error) {
    console.error("Error fetching orders:", error);
    return [];
  }
};

export const fetchVehicles = async () => {
  try {
    const response = await axios.get(`${API_BASE_URL}/vehicles`);
    return response.data;
  } catch (error) {
    console.error("Error fetching vehicles:", error);
    return [];
  }
};

export const placeOrder = async (customerName, itemId, deliveryLat, deliveryLon) => {
  try {
    await axios.post(`${API_BASE_URL}/order`, {
      customer_name: customerName,
      item_id: itemId,
      delivery_lat: parseFloat(deliveryLat),
      delivery_lon: parseFloat(deliveryLon),
      quantity: 1,
    });
  } catch (error) {
    console.error("Error placing order:", error);
  }
};

export const optimizeRoutes = async () => {
  try {
    await axios.post(`${API_BASE_URL}/optimize-route`);
  } catch (error) {
    console.error("Error optimizing routes:", error);
  }
};
