<!DOCTYPE html>
<html>
<head>
	<title>Currency</title>
	<link rel="stylesheet" type="text/css" href="CSS/styles.css">
</head>
<body>
	%for x in posts["results"]:
		<h1>Currency</h1>
		<h2>{{ x["longName"] }}/{{ x["shortName"] }}</h2>
		<p>virði: {{ x["value"] }}</p>
		<p>Kaup: {{ x["askValue"] }}</p>
		<p>Sala: {{ x["bidValue"] }}</p>
		<p>Breyting: {{ x["changeCur"] }}</p>
		<p>Breyting?: {{ x["changePer"] }}</p>
</body>
</html>