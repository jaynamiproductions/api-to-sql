#api-to-sql
<h2>Import large datasets into SQLite database.</h2>
<p>This program will:</p>
<ul>
    <li>Paginate API response.</li>
    <li>Create pandas dataframe with JSON data from API response.</li>
    <li>Write data from dataframe to SQLite database.</li>
</ul>
<br/>
<p>This program is currently designed for APIs that follow standard limit/size and offset query parameters (ex. .gov APIs).</p>
<p><a href="https://dev.socrata.com/docs/endpoints.html">Socrata-SODA API Documentation</a></p>
<p><a href="https://data.cms.gov/sites/default/files/2022-08/API%20FAQ%20v1_0.pdf">Centers for Medicare and Medicaid Services API FAQ</a></p>