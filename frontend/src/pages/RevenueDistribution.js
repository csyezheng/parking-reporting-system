import React from 'react';
import RevenuePieChart from '../components/RevenuePieChart';
import "./RevenueDistribution.css"

const RevenueDistribution = () => {
    return (
        <div>
            <h1>Revenue Distribution</h1>
            <RevenuePieChart />
        </div>
    );
};

export default RevenueDistribution;
