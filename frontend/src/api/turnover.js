const API_URL = 'http://localhost:8000/turnover';

export const fetchTurnoverRecords = async () => {
    const response = await fetch(API_URL);
    return response.json();
};
