import React, { useEffect, useState } from 'react';
import { fetchOccupancyRecords } from '../api/occupancy';
import { Line } from 'react-chartjs-2';
import './OccupancyChart.css';

const OccupancyChart = () => {
    const [data, setData] = useState([]);

    useEffect(() => {
        const getData = async () => {
            const result = await fetchOccupancyRecords();
            setData(result);
        };
        getData();
    }, []);

    const chartData = {
        labels: data.map(record => new Date(record.timestamp).toLocaleDateString()),
        datasets: [
            {
                label: 'Occupied Spaces',
                data: data.map(record => record.occupied_spaces),
                borderColor: 'rgba(75,192,192,1)',
                backgroundColor: 'rgba(75,192,192,0.2)',
            },
        ],
    };

    return (
        <div className="occupancy-chart-container">
            <Line 
                data={chartData} 
            />
        </div>
    );
};

export default OccupancyChart;
