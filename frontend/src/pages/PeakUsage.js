// src/pages/PeakUsage.js

import React from 'react';
import PeakUsageHeatmap from '../components/PeakUsageHeatmap'; // Adjust the path if necessary
import "./PeakUsage.css"

const PeakUsage = () => {
  return (
    <div>
      <h1>Peak Usage Analysis</h1>
      <PeakUsageHeatmap />
    </div>
  );
};

export default PeakUsage;
