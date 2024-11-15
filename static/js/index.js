let currentMatch = 0;
let statsVisible = false;

function formatTeamName(url) {
    return url.split('/').pop().replace(/-/g, ' ').replace(/\b\w/g, char => char.toUpperCase());
}

function getLogoFileName(teamName) {
    const formattedName = teamName.toLowerCase().replace(/\s+/g, '-');
    return `nfl-${formattedName}-team-logo-2-300x300.png`;
}

function displayMatch() {
    const match = matches[currentMatch];
    const container = document.getElementById("match-container");
    const matchNumber = document.getElementById("matchNumber");

    const awayTeamName = formatTeamName(match.away_team.url);
    const homeTeamName = formatTeamName(match.home_team.url);
    const awayLogo = getLogoFileName(awayTeamName);
    const homeLogo = getLogoFileName(homeTeamName);

    matchNumber.innerText = `${match.match_number}`;

    container.innerHTML = `
        <div class="col-md-10">
            <div class="row text-center">
                <div class="col-md-5 card p-3 mb-3 text-center">
                    <img src="/static/images/${awayLogo}" alt="${awayTeamName} Logo" class="team-logo">
                    <h4>${awayTeamName}</h4>
                    ${generateRankings(match.away_team.rankings)}
                </div>
                <div class="col-md-2 d-flex align-items-center justify-content-center">
                    <h2>@</h2>
                </div>
                <div class="col-md-5 card p-3 mb-3 text-center">
                    <img src="/static/images/${homeLogo}" alt="${homeTeamName} Logo" class="team-logo">
                    <h4>${homeTeamName}</h4>
                    ${generateRankings(match.home_team.rankings)}
                </div>
            </div>
            <div class="card p-3">
                <h5 class="text-center">Last 5 Encounters</h5>
                <table class="table table-bordered text-center fixed-table">
                    <thead class="thead-dark">
                        <tr>
                            <th>Date</th>
                            <th>Visitor Team</th>
                            <th>Visitor Score</th>
                            <th>Home Team</th>
                            <th>Home Score</th>
                            <th>Result</th>
                        </tr>
                    </thead>
                    <tbody>
                        ${generateGameHistory(match.games)}
                    </tbody>
                </table>
            </div>
        </div>
    `;
}

function generateRankings(rankings) {
    let html = "<ul class='list-group list-group-flush'>";
    for (const [key, value] of Object.entries(rankings)) {
        html += `<li class="list-group-item"><strong>${key}:</strong> ${value.offense} / ${value.defense}</li>`;
    }
    return html + "</ul>";
}

function generateGameHistory(games) {
    return games.map(game => `
        <tr>
            <td>${game.date}</td>
            <td>${game.visitor_team}</td>
            <td>${game.visitor_score}</td>
            <td>${game.home_team}</td>
            <td>${game.home_score}</td>
            <td class="${game.result.startsWith('W') ? 'result-win' : 'result-loss'}">${game.result}</td>
        </tr>
    `).join("");
}

function generateStatsTable(stats, statType) {
    if (!stats || stats.length === 0) return "<p>No data available</p>";

    const statHeaders = {
        passing: ["Player", "Att", "Cmp", "Pct", "Yds", "YPA", "TD", "TD%", "Int", "Int%", "Lg", "Sack", "Loss", "Rate"],
        rushing: ["Player", "Gms", "Att", "Yds", "Avg", "YPG", "Lg", "TD", "FD"],
        receiving: ["Player", "Gms", "Rec", "Yds", "Avg", "YPG", "Lg", "TD", "FD", "Tar", "YAC"]
    };

    const headers = statHeaders[statType];

    let html = `
        <table class="table table-sm table-striped text-left">
            <thead class="thead-light">
                <tr>${headers.map(header => `<th>${header}</th>`).join("")}</tr>
            </thead>
            <tbody>
                ${stats.map(player => `
                    <tr>${headers.map(header => `<td>${player[header]}</td>`).join("")}</tr>
                `).join("")}
            </tbody>
        </table>
    `;
    return html;
}

function toggleStats() {
    statsVisible = !statsVisible;
    document.getElementById("statisticsSection").style.display = statsVisible ? "block" : "none";
    document.getElementById("toggleStatsButton").innerText = statsVisible ? "Hide Stats" : "Show Stats";

    if (statsVisible) {
        const match = matches[currentMatch];
        document.getElementById("statisticsSection").innerHTML = `
            <h5>Passing (Away Team)</h5>
            ${generateStatsTable(match.away_team.statistics.passing, "passing")}
            <h5>Passing (Home Team)</h5>
            ${generateStatsTable(match.home_team.statistics.passing, "passing")}
            <h5>Rushing (Away Team)</h5>
            ${generateStatsTable(match.away_team.statistics.rushing, "rushing")}
            <h5>Rushing (Home Team)</h5>
            ${generateStatsTable(match.home_team.statistics.rushing, "rushing")}
            <h5>Receiving (Away Team)</h5>
            ${generateStatsTable(match.away_team.statistics.receiving, "receiving")}
            <h5>Receiving (Home Team)</h5>
            ${generateStatsTable(match.home_team.statistics.receiving, "receiving")}
        `;
    }
}

function showPreviousMatch() {
    currentMatch = (currentMatch > 0) ? currentMatch - 1 : matches.length - 1;
    displayMatch();
}

function showNextMatch() {
    currentMatch = (currentMatch < matches.length - 1) ? currentMatch + 1 : 0;
    displayMatch();
}

displayMatch();