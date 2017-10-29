<!DOCTYPE html>
<html>
<head>
	<title>Login</title>
	<meta charset="utf-8">
	<link rel="stylesheet" type="text/css" href="CSS/styles.css">
</head>
<body>
	<h1>Login</h1>
	<form action = "/check", method="post">
		<label>Notendanafn:</label><br>
		<input type="text" name="notendanafn"><br>
		<label>Lykilorð:</label><br>
		<input type="password" name="password"><br>
		<input type="submit" name="login" value="Innskrá">
	</form>
	<h1>Sign Up</h1>
	<form action = "/signup", method="post">
		<label>Notendanafn:</label><br>
		<input type="text" name="notendanafn"><br>
		<label>Lykilorð:</label><br>
		<input type="password" name="password"><br>
		<input type="submit" name="login" value="Sign Up">
	</form>

</body>
</html>