import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Dashboard from './pages/Dashboard';
import Occupancy from './pages/Occupancy';
import Revenue from './pages/Revenue';
import Duration from './pages/Duration';
import Turnover from './pages/Turnover';
import PeakUsage from './pages/PeakUsage';
import Utilization from './pages/Utilization';
import RevenueDistribution from './pages/RevenueDistribution';
import Comparative from './pages/Comparative';

const App = () => {
    return (
        <Router>
            <Routes>
                <Route path="/" element={<Dashboard />} />
                <Route path="/occupancy" element={<Occupancy />} />
                <Route path="/revenue" element={<Revenue />} />
                <Route path="/duration" element={<Duration />} />
                <Route path="/turnover" element={<Turnover />} />
                <Route path="/peak-usage" element={<PeakUsage />} />
                <Route path="/utilization" element={<Utilization />} />
                <Route path="/revenue-distribution" element={<RevenueDistribution />} />
                <Route path="/comparative" element={<Comparative />} />
            </Routes>
        </Router>
    );
};

export default App;
