<!DOCTYPE html>
<html>
<head>
	<title></title>
</head>
<body>

	<form action = "/send", method="post">
	<h2>Notenda Upplýsingar</h2>
		<label>Nafn:</label><br>
		<input type="text" name="nafn" required=""><br>
		<label>Heimilisfang:</label><br>
		<input type="text" name="heimilisfang" required=""><br>
		<label>Netfang:</label><br>
		<input type="email" name="email" required="">

	<h2>Pizzastærð</h2>
		<label>9 tommu pizza - 1000 Kr</label><br>
		<input type="radio" name="staerd" value="9-tommu" checked><br>
		<label>12 tommu pizza - 1500 Kr</label><br>
		<input type="radio" name="staerd" value="12-tommu">
		<label>15 tommu pizza - 2000 Kr</label>
		<input type="radio" name="staerd" value="15-tommu">

		<input type="submit" name="Panta">
	</form>

</body>
</html>