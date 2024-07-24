import React, { useEffect, useState } from 'react';
import { fetchRevenueRecords } from '../api/revenue';
import { Pie } from 'react-chartjs-2';
import "./RevenuePieChart.css"

const RevenuePieChart = () => {
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
                label: 'Revenue',
                data: data.map(record => parseFloat(record.total_revenue)),
                backgroundColor: ['rgba(75,192,192,0.2)', 'rgba(255,99,132,0.2)', 'rgba(255,159,64,0.2)'],
                borderColor: ['rgba(75,192,192,1)', 'rgba(255,99,132,1)', 'rgba(255,159,64,1)'],
                borderWidth: 1,
            },
        ],
    };

    return (
        <div className="revenue-piechart-container">
            <Pie 
                data={chartData} 
            />
        </div>
    );
};

export default RevenuePieChart;
