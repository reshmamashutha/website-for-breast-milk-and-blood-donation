const express = require("express");
const cookieParser = require("cookie-parser");
const path = require("path");
const fileUpload = require("express-fileupload");

const HomeRoutes = require("./routes/homeRoutes");
const AuthRoutes = require("./routes/authRoutes");

const app = express();

app.set("view engine", "ejs");
app.use(express.json());
app.use(fileUpload());
app.use(cookieParser());
app.use(express.urlencoded({ extended: true }));
app.set("views", path.join(__dirname, "views"));
app.use(express.static(path.join(__dirname, "public")));

app.listen(8000);
console.log('Listening - http://localhost:8000/')

app.use("/", HomeRoutes)
app.use("/authentication", AuthRoutes);