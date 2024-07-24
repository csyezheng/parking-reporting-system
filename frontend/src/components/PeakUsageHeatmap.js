import React, { useEffect, useState } from 'react';
import { fetchPeakUsageRecords } from '../api/peak_usage';
import Plot from 'react-plotly.js';
import "./PeakUsageHeatmap.css"

const PeakUsageHeatmap = () => {
    const [heatmapData, setHeatmapData] = useState({
      z: [],
      x: [],
      y: [],
    });
  
    useEffect(() => {
      const getData = async () => {
        const result = await fetchPeakUsageRecords();
        // Process the result to match the format needed for the heatmap
        setHeatmapData({
          z: result.z,
          x: result.x,
          y: result.y,
        });
      };
      getData();
    }, []);
  
    const layout = {
      title: 'Peak Usage Heatmap',
      xaxis: {
        title: 'Time Slots' // Customize the X-axis title
      },
      yaxis: {
        title: 'Days' // Customize the Y-axis title
      },
      width: 600, // Adjust the width as needed
      height: 400, // Adjust the height as needed
    };
  
    return (
      <div>
        <h2>Peak Usage Heatmap</h2>
        <Plot
          data={[
            {
              z: heatmapData.z,
              x: heatmapData.x,
              y: heatmapData.y,
              type: 'heatmap',
              colorscale: 'Viridis', // You can change the color scale
              colorbar: {
                title: 'Intensity'
              }
            }
          ]}
          layout={layout}
        />
      </div>
    );
  };
  
  export default PeakUsageHeatmap;
