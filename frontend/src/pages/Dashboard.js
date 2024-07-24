import React from 'react';
import OccupancyChart from '../components/OccupancyChart';
import RevenueChart from '../components/RevenueChart';
import "./Dashboard.css"

const Dashboard = () => {
    return (
        <div>
            <h1>Dashboard</h1>
            <OccupancyChart />
            <RevenueChart />
        </div>
    );
};

export default Dashboard;
