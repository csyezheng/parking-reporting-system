// src/components/DurationHistogram.js

import React, { useEffect, useState } from 'react';
import { Bar } from 'react-chartjs-2';
import axios from 'axios';

const DurationHistogram = () => {
    const [data, setData] = useState({});

    useEffect(() => {
        async function fetchData() {
            const API_URL2 = 'http://localhost:8000/transactions/durations';
            const result = await axios.get(API_URL2);
            const labels = result.data.map(item => `${item.hours} hours`);
            const values = result.data.map(item => item.count);

            setData({
                labels,
                datasets: [{
                    label: 'Parking Duration',
                    data: values,
                    backgroundColor: 'rgba(75,192,192,0.6)',
                    borderColor: 'rgba(75,192,192,1)',
                    borderWidth: 1,
                }]
            });
        }

        fetchData();
    }, []);

    return (
        <div>
            <Bar data={data} options={{
                scales: {
                    x: { beginAtZero: true },
                    y: { beginAtZero: true }
                },
                responsive: true,
                plugins: {
                    legend: {
                        position: 'top',
                    },
                },
            }} />
        </div>
    );
};

export default DurationHistogram;
