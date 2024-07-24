import React, { useEffect, useState } from 'react';
import { Bar } from 'react-chartjs-2';
import { Chart as ChartJS, CategoryScale, LineElement, LinearScale, BarElement, PointElement, Title, Tooltip, Legend } from 'chart.js';
import { getComparativeData } from '../api/comparative';
import './ComparativeBarChart.css';

// Register ChartJS components
ChartJS.register(CategoryScale, LinearScale, LineElement, BarElement, PointElement, Title, Tooltip, Legend);

const ComparativeBarChart = () => {
    const [data, setData] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);

    useEffect(() => {
        const fetchData = async () => {
            try {
                const result = await getComparativeData();
                setData(result);
                setLoading(false);
            } catch (error) {
                console.error('Error fetching comparative data:', error);
                setError(error);
                setLoading(false);
            }
        };

        fetchData();
    }, []);

    const chartData = {
        labels: data.map(record => record.date), // Assuming 'date' is a property in your data
        datasets: [
            {
                label: 'Occupancy Rate',
                data: data.map(record => record.occupancy_rate), // Assuming 'occupancy_rate' is a property in your data
                backgroundColor: 'rgba(75, 192, 192, 0.2)',
                borderColor: 'rgba(75, 192, 192, 1)',
                borderWidth: 1,
            },
            {
                label: 'Total Revenue',
                data: data.map(record => record.total_revenue), // Assuming 'total_revenue' is a property in your data
                backgroundColor: 'rgba(153, 102, 255, 0.2)',
                borderColor: 'rgba(153, 102, 255, 1)',
                borderWidth: 1,
            }
        ],
    };

    const options = {
        responsive: true,
        plugins: {
            legend: {
                position: 'top',
            },
            tooltip: {
                callbacks: {
                    label: function (context) {
                        let label = context.dataset.label || '';
                        if (label) {
                            label += ': ';
                        }
                        if (context.parsed.y !== null) {
                            label += context.parsed.y;
                        }
                        return label;
                    },
                },
            },
        },
    };

    if (loading) return <p>Loading...</p>;
    if (error) return <p>Error loading data</p>;

    return (
        <div className="comparative-barchart-container">
            <h2>Comparative Bar Chart</h2>
            <Bar data={chartData} options={options} />
        </div>
      );
};

export default ComparativeBarChart;
