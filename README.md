#api-to-sql
<h2>Import large Socrata datasets into SQLite database.</h2>
<p>This program will:</p>
<ul>
    <li>Paginate API response with limit and offset query parameters.</li>
    <li>Create pandas dataframe with JSON data from API response.</li>
    <li>Write data from dataframe to SQLite database.</li>
</ul>
<br/>
<p>This program is currently designed for SODA API endpoints.</p>