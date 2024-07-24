const API_URL = 'http://localhost:8000/utilization';

export const fetchUtilizationRecords = async () => {
    const response = await fetch(API_URL);
    return response.json();
};
