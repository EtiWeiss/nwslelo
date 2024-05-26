fetch('output.json')
  .then(response => response.json())
  .then(data => {
    const tableBody = document.getElementById('table-body');
    data.forEach(item => {
      const row = document.createElement('tr');
      row.innerHTML = `
        <td>${item.Team}</td>
        <td>${item.Elo}</td>
      `;
      tableBody.appendChild(row);
    });
  })
  .catch(error => console.error('Error fetching JSON:', error));