// Load curriculum and render interactive phases
fetch('../curriculum.json')
  .then(res => res.json())
  .then(phases => {
    const container = document.getElementById('phasesContainer');
    container.innerHTML = '';

    phases.forEach(phase => {
      const card = document.createElement('div');
      card.className = 'phase-card';

      const weeksHtml = phase.weeks.map(w => `
        <div class="week-block">
          <div class="week-title">Week ${String(w.week_num).padStart(2, '0')}: ${w.week_title}</div>
          <div class="days-list">
            ${w.days.map(d => `
              <a href="../${phase.phase_id}/${w.week_id}/day-${String(d.day_num).padStart(3, '0')}/README.md" class="day-item" target="_blank">
                <span class="status-icon">⚪</span>
                <span><strong>Day ${String(d.day_num).padStart(3, '0')}:</strong> ${d.title}</span>
              </a>
            `).join('')}
          </div>
        </div>
      `).join('');

      card.innerHTML = `
        <div class="phase-header" onclick="this.nextElementSibling.classList.toggle('open')">
          <div class="phase-title-group">
            <h3>Phase ${String(phase.phase_num).padStart(2, '0')}: ${phase.phase_title}</h3>
            <span class="meta">${phase.weeks_range} • ${phase.days_range}</span>
          </div>
          <span class="expand-indicator">▼</span>
        </div>
        <div class="phase-body">
          ${weeksHtml}
        </div>
      `;
      container.appendChild(card);
    });

    // Search filter
    document.getElementById('daySearch').addEventListener('input', (e) => {
      const query = e.target.value.toLowerCase();
      document.querySelectorAll('.day-item').forEach(item => {
        const text = item.textContent.toLowerCase();
        if (text.includes(query)) {
          item.style.display = 'flex';
          item.closest('.phase-body').classList.add('open');
        } else {
          item.style.display = query ? 'none' : 'flex';
        }
      });
    });
  })
  .catch(err => console.error("Error loading curriculum.json", err));
