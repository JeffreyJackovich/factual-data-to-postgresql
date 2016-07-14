

<p><a href="http://developer.factual.com/" target="_blank"><img width="355" alt="fact_whitespace" src="https://cloud.githubusercontent.com/assets/8240612/16720322/209fd664-4703-11e6-8cc3-3d6d7d458889.png"></a>  <img width="55" alt="right_arrow" src="https://cloud.githubusercontent.com/assets/8240612/16720229/f207b458-4701-11e6-8e76-1fe563fb861d.png">       <a  href="https://www.postgresql.org/" target="_blank"><img width="266" alt="post_whitespace" src="https://cloud.githubusercontent.com/assets/8240612/16720326/2f373956-4703-11e6-8228-a71489c5e0ef.png"></a> </p>



<ul><h2><strong>What do these scripts accomplish?</strong></h2> 
<ul>Python scripts to create a postgresql table, pull restaurant data by location (latitude/longitude) coordinates from factual.com, and export the data to the created table.</ul>

<h2><strong>How to operate?</strong></h2> 
<ul>1. Create a postgresql table with: <a href="https://github.com/JeffreyJackovich/factual_data_to_postgresql/blob/master/create_table.py"><strong>create_table.py</strong></a> </ul>
<ul>2. Query restaurant data and export to the postgresql table with: <a href="https://github.com/JeffreyJackovich/factual_data_to_postgresql/blob/master/restaurant_data_to_postgresql.py"><strong>restaurant_data_to_postgres.py</strong></a> </ul>

<h2><strong>Why is this interesting?</strong></h2>
<ul>This provides a basic framework to obtain data and store it for further analysis!</ul>

<h2><strong>My Next Steps?</strong></h2>
<ul>I am re-factoring the code for the following:</ul>
<ul>Command line access with Argparse and a code re-factor to allow access to all of factual's data categories.</ul>

<h2><strong>Dependencies</strong></h2>
<ul><h4>1. factual-api</h4></ul>
<ul><h4>How to install factual-api ?</h4></ul>
<ul><ul>pip install factual-api</ul></ul>
<ul><h4>2. psycopg2</h4></ul> 
<ul><h4>How to install psycopg2 ?</h4></ul>
<ul><ul>pip install psycopg2</ul></ul>
