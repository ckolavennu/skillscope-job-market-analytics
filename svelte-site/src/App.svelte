<script>
  let activeSection = 'home';

  const dashboardUrl = 'https://your-streamlit-app.streamlit.app';

  const metrics = [
    { label: 'Job Market Focus', value: 'Data Roles' },
    { label: 'Analytics Layer', value: 'Streamlit' },
    { label: 'Website Layer', value: 'Svelte' }
  ];

  const features = [
    'Skill demand analysis from job descriptions',
    'Hiring location and employer insights',
    'Salary analytics planned for the next milestone',
    'Future resume skill-gap analyzer'
  ];
</script>

<nav class="nav">
  <div class="brand">SkillScope</div>
  <div class="links">
    <button on:click={() => activeSection = 'home'}>Home</button>
    <button on:click={() => activeSection = 'method'}>Methodology</button>
    <button on:click={() => activeSection = 'dashboard'}>Dashboard</button>
  </div>
</nav>

{#if activeSection === 'home'}
  <main class="hero">
    <section class="heroText">
      <p class="eyebrow">Job Market Analytics Platform</p>
      <h1>Understand what employers actually want.</h1>
      <p class="subtitle">
        SkillScope analyzes job postings to identify in-demand skills, hiring locations,
        top employers, and future salary trends for data-related roles.
      </p>
      <div class="actions">
        <button class="primary" on:click={() => activeSection = 'dashboard'}>Open Dashboard</button>
        <button class="secondary" on:click={() => activeSection = 'method'}>View Methodology</button>
      </div>
    </section>

    <section class="panel">
      {#each metrics as metric}
        <div class="metric">
          <span>{metric.label}</span>
          <strong>{metric.value}</strong>
        </div>
      {/each}
    </section>
  </main>

  <section class="section">
    <h2>What this project demonstrates</h2>
    <div class="cards">
      {#each features as feature}
        <article class="card">{feature}</article>
      {/each}
    </div>
  </section>
{/if}

{#if activeSection === 'method'}
  <main class="section narrow">
    <p class="eyebrow">Methodology</p>
    <h1>From job postings to market intelligence</h1>
    <div class="timeline">
      <div><strong>1. Data Collection</strong><p>Collect job postings from manual samples first, then safer public APIs.</p></div>
      <div><strong>2. Data Cleaning</strong><p>Standardize titles, companies, locations, salary formats, and descriptions.</p></div>
      <div><strong>3. Skill Extraction</strong><p>Detect tools and technical skills such as SQL, Excel, Python, Power BI, and Tableau.</p></div>
      <div><strong>4. Dashboarding</strong><p>Present insights through Streamlit and embed the dashboard inside the Svelte site.</p></div>
    </div>
  </main>
{/if}

{#if activeSection === 'dashboard'}
  <main class="section">
    <p class="eyebrow">Interactive Dashboard</p>
    <h1>SkillScope Analytics Dashboard</h1>
    <p class="subtitle small">
      Replace the iframe URL after deploying the Streamlit app. For local testing, run Streamlit separately.
    </p>
    <div class="iframeWrap">
      <iframe title="SkillScope Streamlit Dashboard" src={dashboardUrl}></iframe>
    </div>
  </main>
{/if}
