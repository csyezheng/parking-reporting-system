const API_URL = 'http://localhost:8000/peak_usage_records';

export const fetchPeakUsageRecords = async () => {
    const response = await fetch(API_URL);
    return response.json();
};
