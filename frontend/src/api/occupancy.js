const API_URL = 'http://localhost:8000/occupancy';

export const fetchOccupancyRecords = async () => {
    const response = await fetch(API_URL);
    return response.json();
};
