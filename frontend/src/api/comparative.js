import axios from 'axios';

// Define the base URL for your API. Adjust if your API is hosted on a different base URL.
const BASE_URL = 'http://localhost:8000'; // Change to your actual API URL

// Function to fetch comparative data
export const getComparativeData = async () => {
    try {
        const response = await axios.get(`${BASE_URL}/comparative`);
        return response.data;
    } catch (error) {
        console.error('Error fetching comparative data:', error);
        throw error;
    }
};

// Function to add new comparative record
export const addComparativeRecord = async (record) => {
    try {
        const response = await axios.post(`${BASE_URL}/comparative`, record);
        return response.data;
    } catch (error) {
        console.error('Error adding comparative record:', error);
        throw error;
    }
};

// Function to update an existing comparative record
export const updateComparativeRecord = async (id, updatedRecord) => {
    try {
        const response = await axios.put(`${BASE_URL}/comparative/${id}`, updatedRecord);
        return response.data;
    } catch (error) {
        console.error('Error updating comparative record:', error);
        throw error;
    }
};

// Function to delete a comparative record
export const deleteComparativeRecord = async (id) => {
    try {
        const response = await axios.delete(`${BASE_URL}/comparative/${id}`);
        return response.data;
    } catch (error) {
        console.error('Error deleting comparative record:', error);
        throw error;
    }
};
