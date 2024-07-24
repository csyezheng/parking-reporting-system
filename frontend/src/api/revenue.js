const API_URL = 'http://localhost:8000/revenue';

export const fetchRevenueRecords = async () => {
    const response = await fetch(API_URL);
    return response.json();
};
