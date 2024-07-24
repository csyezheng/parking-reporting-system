import React, { useEffect, useState } from 'react';
import { fetchRevenueRecords } from '../api/revenue';
import { Line } from 'react-chartjs-2';
import "./RevenueChart.css"

const RevenueChart = () => {
    const [data, setData] = useState([]);

    useEffect(() => {
        const getData = async () => {
            const result = await fetchRevenueRecords();
            setData(result);
        };
        getData();
    }, []);

    const chartData = {
        labels: data.map(record => new Date(record.date).toLocaleDateString()),
        datasets: [
            {
                label: 'Total Revenue',
                data: data.map(record => parseFloat(record.total_revenue)),
                borderColor: 'rgba(255,99,132,1)',
                backgroundColor: 'rgba(255,99,132,0.2)',
            },
        ],
    };

    return (
        <div className="revenue-chart-container">
            <Line 
                data={chartData} 
            />
        </div>
    );
};

export default RevenueChart;
