<!DOCTYPE html>
<html>
<head>
	<title>PIZZA!</title>
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
		<label>Símanúmer:</label><br>
		<input type="number" name="simanumer" required=""><br>
		<label>Heimilisfang:</label><br>
		<input type="text" name="heimilisfang" title="Þarf að hafa einn tölustaf" required="">

	<h2>Pizzastærð</h2>
		<input type="radio" name="staerd" value="9-tommu" checked>
		<label>9 tommu pizza - 1000 Kr</label><br>
		<input type="radio" name="staerd" value="12-tommu">
		<label>12 tommu pizza - 1500 Kr</label><br>
		<input type="radio" name="staerd" value="15-tommu">
		<label>15 tommu pizza - 2000 Kr</label><br>

	<h2>Álegg</h2>
		<p>Hvert álegg er 200kr</p>

		<input type="checkbox" name="alegg" value="skinka">
		<label>Skinka</label><br>
		<input type="checkbox" name="alegg" value="ananas">
		<label>Ananas</label><br>
		<input type="checkbox" name="alegg" value="pepperoni">
		<label>Pepperoni</label><br>


		<input type="submit" name="Panta" value="Panta">
	</form>

</body>
</html>