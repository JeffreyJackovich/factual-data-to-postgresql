

<p><a href="http://developer.factual.com/" target="_blank"><img width="355" alt="fact_whitespace" src="https://cloud.githubusercontent.com/assets/8240612/16720322/209fd664-4703-11e6-8cc3-3d6d7d458889.png"></a>  <img width="55" alt="right_arrow" src="https://cloud.githubusercontent.com/assets/8240612/16720229/f207b458-4701-11e6-8e76-1fe563fb861d.png">       <a  href="https://www.postgresql.org/" target="_blank"><img width="266" alt="post_whitespace" src="https://cloud.githubusercontent.com/assets/8240612/16720326/2f373956-4703-11e6-8228-a71489c5e0ef.png"></a> </p>



<ul><h2><strong>What do these scripts accomplish?</strong></h2> 
<ul>Python scripts to create a postgresql table, pull restaurant data by location (latitude/longitude) coordinates from <a href="http://developer.factual.com/">developer.factual.com</a>, and export the data to the created table.</ul>

<h2><strong>How to operate?</strong></h2> 
<ul>1. Create a postgresql table with: <a href="https://github.com/JeffreyJackovich/factual_data_to_postgresql/blob/master/create_table.py"><strong>create_table.py</strong></a> </ul>
<ul>2. Modify latitude/longitude coordinates and search radius (see "Current lat./long. setting below") then query restaurant data and export to the postgresql table with: <a href="https://github.com/JeffreyJackovich/factual_data_to_postgresql/blob/master/restaurant_data_to_postgresql.py"><strong>restaurant_data_to_postgresql.py</strong></a> </ul>
<ul><ul>a. Current lat./long. setting (see: line 54) is: "<a href="https://www.google.com/maps/place/37%C2%B019'58.5%22N+121%C2%B053'18.8%22W/@37.3424183,-121.8953795,13.75z/data=!4m5!3m4!1s0x0:0x0!8m2!3d37.332915!4d-121.888558">37.332915, -121.888558</a>, 1000" ; thus, San Jose, CA and a 1000 meter (0.62 mile) radius. </ul></ul>


<h2><strong>Why is this interesting?</strong></h2>
<ul>This provides a basic framework to obtain data and store it for further analysis!</ul>

<h2><strong>Dependencies</strong></h2>
<ul><h4>1. factual-api</h4></ul>
<ul><h4>2. psycopg2</h4></ul> 

<h2><strong>My Next Steps?</strong></h2>
<ul>Command line access with Argparse and a code re-factor to allow access to all of factual's data categories.</ul>
