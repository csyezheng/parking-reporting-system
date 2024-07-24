const API_URL = 'http://localhost:8000/revenue_distribution_records';

export const fetchRevenueDistributionRecords = async () => {
    const response = await fetch(API_URL);
    return response.json();
};
