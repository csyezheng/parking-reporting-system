import React, { useEffect, useState } from 'react';
import { fetchUtilizationRecords } from '../api/utilization';
import { Chart, ArcElement } from 'chart.js';
import { Line } from 'react-chartjs-2';
import "./UtilizationLineChart.css"

Chart.register(ArcElement);

const UtilizationLineChart = () => {
    const [data, setData] = useState([]);

    useEffect(() => {
        const getData = async () => {
            const result = await fetchUtilizationRecords();
            setData(result);
        };
        getData();
    }, []);

    const chartData = {
        labels: data.map(record => new Date(record.timestamp).toLocaleDateString()),
        datasets: [
            {
                label: 'Utilization Rate',
                data: data.map(record => (record.occupied_spaces / 100) * 100), // Assuming 100 is the max capacity
                borderColor: 'rgba(54,162,235,1)',
                backgroundColor: 'rgba(54,162,235,0.2)',
            },
        ],
    };

    return (
        <div className="utilization-linechart-container">
            <Line 
                data={chartData} 
            />
        </div>
    );
};

export default UtilizationLineChart;
