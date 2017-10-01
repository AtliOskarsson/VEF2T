	<!DOCTYPE html>
<html>
<head>
	<title>Skráning</title>
	<meta charset="utf-8">
	<link rel="stylesheet" type="text/css" href="CSS/styles.css">
</head>
<body>

	<form action = "/send", method="post">
	<h2>Notenda Upplýsingar</h2>
	<p>Villa: {{ villa }}</p>
		<label>Nafn:</label><br>
		<input type="text" name="nafn" value="{{ nafn }}" required=""><br>
		<label>Netfang:</label><br>
		<input type="email" name="email" value="{{ netfang }}" required=""><br>
		<label>Notendanafn:</label><br>
		<input type="text" name="notendanafn" value="{{ notendanafn }}" required=""><br>
		<label>Símanúmer:</label><br>
		<input type="number" name="simanumer" value="{{ simanumer }}" required=""><br>
		<label>Lykilorð:</label><br>
		<input type="password" name="password" value="{{ password }}" required=""><br>


		<input type="submit" name="skra" value="Skrá">
	</form>

</body>
</html>