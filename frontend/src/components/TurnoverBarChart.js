import React, { useEffect, useState } from 'react';
import { fetchTurnoverRecords } from '../api/turnover';
import { Bar } from 'react-chartjs-2';
import "./TurnoverBarChart.css"

const TurnoverBarChart = () => {
    const [data, setData] = useState([]);

    useEffect(() => {
        const getData = async () => {
            const result = await fetchTurnoverRecords();
            setData(result);
        };
        getData();
    }, []);

    const chartData = {
        labels: data.map(record => new Date(record.timestamp).toLocaleDateString()),
        datasets: [
            {
                label: 'Entries',
                data: data.map(record => record.entries),
                backgroundColor: 'rgba(75,192,192,0.2)',
                borderColor: 'rgba(75,192,192,1)',
                borderWidth: 1,
            },
            {
                label: 'Exits',
                data: data.map(record => record.exits),
                backgroundColor: 'rgba(255,99,132,0.2)',
                borderColor: 'rgba(255,99,132,1)',
                borderWidth: 1,
            },
        ],
    };

    return (
        <div className="turnover-bar-chart-container">
            <Bar 
                data={chartData} 
            />
        </div>
    );
};

export default TurnoverBarChart;
