fetch('AngelCityMatches.json')
  .then(response => response.json())
  .then(data => {
    const tableBody = document.getElementById('table-body');
    data.forEach(item => {
      const row = document.createElement('tr');
      row.innerHTML = `
        <td>${item.Team1}</td>
        <td>${item.ELO1}</td>
        <td>${item.Team2}</td>
        <td>${item.Elo2}</td>
        <td>${item.Result1}</td>
        <td>${item.Result2}</td>
        <td>${item.Elo1new}</td>
        <td>${item.Elo2new}</td>
      `;
      tableBody.appendChild(row);
    });
  })
  .catch(error => console.error('Error fetching JSON:', error));

fetch('AngelCityElo.json')
  .then(response => response.json())
  .then(data => {
    const teamName = data[0].team;
    const ranking = data[0].elo;
    const teamNameElement = document.createElement('h1');
    teamNameElement.textContent = `${teamName}`;
    const rankingElement = document.createElement('h2');
    rankingElement.textContent = `${ranking}`;
    const container = document.getElementById('team-data-container');
    container.appendChild(teamNameElement);
    container.appendChild(rankingElement);
  })
  .catch(error => console.error('Error fetching JSON:', error));
