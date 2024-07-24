const API_URL = 'http://localhost:8000/parking_lots';

export const fetchParkingLots = async () => {
    const response = await fetch(API_URL);
    return response.json();
};

export const fetchParkingLotById = async (id) => {
    const response = await fetch(`${API_URL}/${id}`);
    return response.json();
};
