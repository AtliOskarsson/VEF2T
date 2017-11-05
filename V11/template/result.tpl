<!DOCTYPE html>
<html>
<head>
	<title>Bíllinn</title>
	<meta charset="utf-8">
	<link rel="stylesheet" type="text/css" href="CSS/styles.css">
</head>
<body>
<form action="/edit", method="post">
	<h1>Skraningarnumer: <input type="radio" name="choice">{{ skraningarnumer }}</h1>
	<p><b>Tegund:</b> <input type="radio" name="choice"> {{ tegund }}</p>
	<p><b>Verksmidjunumer:</b> <input type="radio" name="choice"> {{ verksmidjunumer }}</p>
	<p><b>Skraningadagur:</b> <input type="radio" name="choice"> {{ skraningadagur }}</p>
	<p><b>CO2 losun:</b> <input type="radio" name="choice"> {{ co2 }}</p>
	<p><b>Þyngd:</b> <input type="radio" name="choice"> {{ þyngd }}</p>
	<p><b>Skoðun:</b> <input type="radio" name="choice"> {{ skodun }}</p>
	<p><b>Staða:</b> <input type="radio" name="choice"> {{ stada }}</p>
	<input type="submit" name="submit" value="Breyta">
</form>
<form action="/eyda" method="post">
	<input type="submit" name="submit" value="Eyda">
</form>
</body>
</html>