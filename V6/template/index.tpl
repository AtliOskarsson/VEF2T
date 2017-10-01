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
		<label>Nafn:</label><br>
		<input type="text" name="nafn" required=""><br>
		<label>Netfang:</label><br>
		<input type="email" name="email" required=""><br>
		<label>Notendanafn:</label><br>
		<input type="text" name="notendanafn" required=""><br>
		<label>Símanúmer:</label><br>
		<input type="number" name="simanumer" required=""><br>
		<label>Lykilorð:</label><br>
		<input type="password" name="password" pattern=".{5,}" title="Þarf að hafa 5 eða fleiri stafi" required=""><br>

		<input type="submit" name="skra" value="Skrá">
	</form>

</body>
</html>