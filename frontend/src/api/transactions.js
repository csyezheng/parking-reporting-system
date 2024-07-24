const API_URL = 'http://localhost:8000/transactions';

export const fetchTransactions = async () => {
    const response = await fetch(API_URL);
    return response.json();
};

const API_URL2 = 'http://localhost:8000/transactions/durations';

export const fetchDurationHistogram = async () => {
    const response = await fetch(API_URL2);
    return response.json();
};