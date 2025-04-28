import React from 'react';

function Teams() {
  return (
    <div>
      <h1 className="text-center">Teams</h1>
      <table className="table table-striped">
        <thead>
          <tr>
            <th>Team Name</th>
            <th>Members</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>Team Alpha</td>
            <td>5</td>
          </tr>
          <tr>
            <td>Team Beta</td>
            <td>4</td>
          </tr>
        </tbody>
      </table>
    </div>
  );
}

export default Teams;