import React from 'react';

function Workouts() {
  return (
    <div>
      <h1 className="text-center">Workouts</h1>
      <table className="table table-striped">
        <thead>
          <tr>
            <th>Workout</th>
            <th>Description</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>Yoga</td>
            <td>Relaxing and stretching exercises</td>
          </tr>
          <tr>
            <td>HIIT</td>
            <td>High-intensity interval training</td>
          </tr>
        </tbody>
      </table>
    </div>
  );
}

export default Workouts;