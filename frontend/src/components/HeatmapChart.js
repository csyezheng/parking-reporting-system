// src/components/HeatmapChart.js
import React from 'react';
import Plot from 'react-plotly.js';
import './HeatmapChart.css';

const HeatmapChart = ({ data, layout }) => {
  return (
    <div>
      <h2>Heatmap Chart</h2>
      <Plot
        data={data}
        layout={layout}
      />
    </div>
  );
};

export default HeatmapChart;
